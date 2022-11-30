#from model.player import Player
import uuid

class Team:
    def __init__(self, player="", team_name=""): 
        self.player = player
        self.team_name = team_name
        self.id = uuid.uuid4()

    def __str__(self):
        return f"{self.player}, {self.team_name}"