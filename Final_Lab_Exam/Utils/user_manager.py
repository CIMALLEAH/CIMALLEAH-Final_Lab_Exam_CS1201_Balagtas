import os

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
                username, password = line.strip().split(",")
                self.users[username] = password

    def save_users(self):
        with open("data/users.txt", "w") as file:
            for username, password in self.users.items():
                file.write(f"{username}, {password}\n")

    def validate_username(self, username):
        pass

    def validate_password(self, password):
        pass
    
    def register(self, username, password):
        pass

    def login(self, username, password):
        pass