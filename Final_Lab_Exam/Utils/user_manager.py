import os
import uuid
from Utils.dice_game import DiceGame

class UserManager:

    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists("data/users.txt"):
            open("data/users.txt", "w").close()

        with open("data/users.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    username,password = parts
                    self.users[username] = password

    def save_users(self):
        with open("data/users.txt", "w") as file:
            for username, password in self.users.items():
                file.write(f"{username},{password}\n")

    def validate_username(self, username):
        return len(username) >= 4

    def validate_password(self, password):
        return len(password) >= 8
    
    def register(self):
        print("Registration")

        while True: 
            username = input ("Enter Username (atleast 4 characters long): ")

            if not username:
                print("Registration canceled. Returning to Main Menu.")
                return
            
            elif username in self.users:
                print ("Username already exists. Please choose another username.")
            
            elif not self.validate_username(username):
                print ("Username must be atleast 4 characters long.")
            
            else:
                break

        while True:
            password = input ("Enter Password (atleast 8 characters long): ")
            if not password:
                print("Registration canceled. Returning to main menu.")
                return
                
            elif not self.validate_password(password):
                print ("Password must be atleast 8 characters long.")
                
            else:
                break

        self.users[username] = password
        self.save_users()
    
        print("Registration successful!")

    def login(self):
        print ("Login")
        username = input ("Enter Username: ")
        password = input ("Enter Password: ")

        if username in self.users:

            if self.users[username] == password:
                print ("Login successful!")
                dice_game = DiceGame(username, None)
                while True:
                    result = dice_game.menu(username)
                    if result == "logout":
                        print (f"Goodbye, {username}!")
                        print ("You have logged out successfully!")
                        break
            
            else:
                print ("Incorrect password. Please try again.")
        
        else:
            print ("User not found.")
        
        return False
