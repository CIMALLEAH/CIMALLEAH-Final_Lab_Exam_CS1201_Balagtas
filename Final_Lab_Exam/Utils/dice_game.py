import os
from Utils.score import Score
from Utils.user_manager import UserManager

class DiceGame:
    
    def __init__(self):
        self.user_manager = UserManager()
        self.current_user = None
        self.load_scores()

    def load_scores(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists("data/rankings.txt"):
            open("data/rankings.txt", "w").close() 

    def save_scores(self, username, game_id, points, wins):
        with open("data/rankings.txt", "a") as file:
            file.write(f"{username}, {game_id}, {points}, {wins}\n")

    def play_game(self):
        pass

    def show_top_scores(self):
        pass

    def logout(self):
        self.current_user = None

    def menu(self):
        pass