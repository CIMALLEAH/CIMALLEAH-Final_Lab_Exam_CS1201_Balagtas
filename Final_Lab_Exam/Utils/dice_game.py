import os
from random import randint
import datetime
from Utils.score import Score


class DiceGame:
    
    def __init__(self, username, game_id=None):
        self.username = username
        self.current_user = username
        self.game_id = game_id if game_id is not None else datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.score = Score(username, self.game_id)
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
                    self.score = Score(username, game_id)
                    self.score.username = username
                    self.score.game_id = game_id
                    self.score.points = int(points)
                    self.score.stages_won = int(stages_won)
                    break

    def save_scores(self, username, game_id, points, wins):
        with open("data/rankings.txt", "a") as file:
            file.write(f"{username}, {game_id}, {points}, {wins}\n")
        if not isinstance(self.score.points, dict):
            self.score.points = {}

        if username not in self.score.points:
            self.score.points[username] = {}
        
        if game_id not in self.score.points[username]:
            self.score.points[username][game_id] = {"points": points, "stages_won": wins}
        
        else:
            self.score.points[username][game_id]["points"] = max(self.score.points[username][game_id]["points"], points)
            self.score.points[username][game_id]["stages_won"] = max(self.score.points[username][game_id]["stages_won"], wins)
  

    def play_game(self, username):
        print (f"\n Starting game as, {username}...")
        self.score.points = 0
        self.score.stages_won = 0
        rounds = 0 

        player_points = 0
        won_once =  False

        while rounds < 3:
            print ("-"*60)
            print(f"\n  Stage {self.score.stages_won + 1}: Best out of Three")
            player_score = 0
            cpu_score = 0
            round_tie = False

            for _ in range(3):
                user_roll = randint(1, 6)
                cpu_roll = randint(1, 6)
                print(f"\n   {username} rolled: {user_roll}")
                print(f"   CPU rolled: {cpu_roll}")

                if user_roll > cpu_roll:
                    player_points += 1
                    player_score += 1
                    print(f"   {username}, you win this round!")
                elif user_roll < cpu_roll:
                    cpu_score += 1
                    print("   CPU wins this round!")
                else:
                    print("   It's a tie! Roll again...")
                    round_tie = True
            
            if round_tie:
                continue
            elif player_score > cpu_score:
                won_once = True
                print(f"\n You win this stage, {username}!")
                player_points += 3
                self.score.points = player_points
                self.score.stages_won += 1
                print (f"\n {username}")
                print(f" Total points: {self.score.points}, Stages won: {self.score.stages_won}")
                try:
                    choice = input("\n Enter 1 to continue to the next stage, 0 to stop: ")
                    if choice != '1':
                        with open("data/rankings.txt", "a") as file:
                            file.write(f"{username},{self.game_id},{player_points},{self.score.stages_won}\n")
                        print("\n Returning to Menu. Thanks for playing!\n")
                        break

                except ValueError as e:
                    print(f"\nError. {e}")

            elif cpu_score > player_score:
                print("\n CPU wins this stage.")
                print("\n Game over.")
                print (f"\n {username}")
                print(f" Total points: {self.score.points}, Stages won: {self.score.stages_won}")
                if won_once:
                    self.save_scores(username, self.game_id, player_points, self.score.stages_won)
                print("\n Returning to Menu. Thanks for playing!")
                break

    def show_top_scores(self):
        scores = []
        with open("data/rankings.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    username, self.score.game_id, points, self.score.stages_won = parts
                    scores.append((username, int(points), int(self.score.stages_won)))

        if scores:
            scores.sort(key=lambda x: x[1], reverse=True)
            print ("\t\t    Top 10 Highest Scores")
            print ("="*60)
            print ("\n Scores:")
            for i, (username, points, self.score.stages_won) in enumerate(scores[:10], 1):
                print (f"  {i}. {username}: Points: {points}, Stages: {self.score.stages_won}")
        else:
            print ("No scores yet.")

    def logout(self):
        self.current_user = None

    def menu(self, username):

        while True:
            try:
                print ("="*60)
                print ("\t\t\tDice Roll Game")
                print ("="*60)
                print (f"\n  Welcome, {username}!")
                print ("\n     Menu:")
                print ("       1. Start Game")
                print ("       2. Show Top Scores")
                print ("       3. Logout")

                choice = input ("\n  Enter your choice: ")
                print ("="*60)

                if choice == '1':
                    self.play_game(username)

                elif choice == '2':
                    with open("data/rankings.txt", "r") as file:
                        if not any(username in line for line in file):
                            print (" You can't view the top 10 scores yet.\n You must first win at least 1 stage.")
                        else:
                            self.show_top_scores()

                elif choice == '3':
                    self.logout()
                    return "logout"

                else:
                    raise ValueError
        
            except ValueError as e:
                print (f"Invalid choice. Please try again.{e}")
