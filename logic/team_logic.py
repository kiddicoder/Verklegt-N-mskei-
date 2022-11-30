from data.team_data import Team_Data
from model.team import Team

class TeamLogic:
    def __init__(self, team_connection):
        self.data_wrapper = team_connection

    def create_team(self, team):
        self.data_wrapper.create_team(team)
    
    def list_all_teams(self):
        return self.data_wrapper.list_all_teams()