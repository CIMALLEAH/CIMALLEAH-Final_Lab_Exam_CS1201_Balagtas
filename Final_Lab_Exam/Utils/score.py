class Score:
    
    def __init__(self, username, game_id):
        self.username = username
        self.game_id = game_id
        self.points = {}
        self.stages_won = 0 