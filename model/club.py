from model.player import Player
from model.team import Team
import uuid

class Club():
    def __init__(self, club_name="", club_address="", club_phone=0, team=""):
        self.club_name = club_name
        self.club_address = club_address 
        self.club_phone = club_phone
        self.team = Team(self.team).id()  
        self.id = uuid.uuid4()

    def __str__(self):
        return f"{self.club_name}, {self.club_address}, {self.club_phone}, {self.team}"