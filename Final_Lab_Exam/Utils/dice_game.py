import os
from random import randint
from Utils.score import Score
from Utils.user_manager import UserManager

class DiceGame:
    
    def __init__(self, username, game_id):
        self.user_manager = UserManager()
        self.current_user = username
        self.game_id = game_id
        self.score = Score(username, game_id)
        self.load_scores()

    def load_scores(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists("data/rankings.txt"):
            open("data/rankings.txt", "w").close() 
        
        with open("data/rankings.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    username, game_id, points, stages_won = parts
                    self.score = Score(username, game_id, int(points), int(stages_won))


    def save_scores(self, username, game_id, points, wins):
        with open("data/rankings.txt", "a") as file:
            file.write(f"{username}, {game_id}, {points}, {wins}\n")

    def play_game(self, username):
        print (f"Starting game as, {username}...")
        self.score.points = 0
        self.score.stages_won = 0

        rounds = 0

        while rounds < 3:
            print(f"\nStage {self.score.stages_won + 1}: Best out of Three")
            player_points = 0
            cpu_points = 0

            for _ in range(3):
                user_roll = randint(1, 6)
                cpu_roll = randint(1, 6)
                print(f"\n{username} rolled: {user_roll}")
                print(f"CPU rolled: {cpu_roll}")

                if user_roll > cpu_roll:
                    player_points += 1
                    print(f"{username}, you win this round!")
                elif user_roll < cpu_roll:
                    cpu_points += 1
                    print("CPU wins this round!")
                elif user_roll == cpu_roll:
                    print("It's a tie! Roll again...")
                    rounds += 1
            
            rounds += 1

            if player_points > cpu_points:
                print(f"You win this stage, {username}!")
                self.score.points += 3
                self.score.stages_won += 1
                print(f"Total points: {self.score.points}, Stages won: {self.score.stages_won}")
                choice = input("Enter 1 to continue to the next stage, 0 to stop: ")
                if choice == '1':
                    continue
                else:
                    break
            else:
                print("Game over. You didn’t win any stages.")
                break

        print("Returning to Menu. Thanks for playing!")

    def show_top_scores(self):
        pass

    def logout(self):
        self.current_user = None

    def menu(self, username):

        while True:
            try:

                print (f"Welcome, {username}!")
                print (" Menu:")
                print ("  1. Start Game")
                print ("  2. Show Top Scores")
                print ("  3. Logout")

                choice = input (" Enter your choice: ")

                if choice == '1':
                    self.play_game(username)

                elif choice == '2':
                    self.show_top_scores()

                elif choice == '3':
                    self.logout()
                    return "logout"

                else:
                    raise ValueError
        
            except ValueError as e:
                print (f"Invalid choice. Please try again.{e}")
