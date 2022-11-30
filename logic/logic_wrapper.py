#from logic.club_logic import ClubLogic
#from logic.match_logic import MatchLogic
from logic.player_logic import PlayerLogic
from logic.team_logic import TeamLogic
#from logic.tournament_logic import TournamentLogic
from data.data_wrapper import DataWrapper

class LogicWrapper:
    def __init__(self):
        self.data_wrapper = DataWrapper()
        #self.club_logic = ClubLogic(self.data_wrapper)
        #self.match_logic = MatchLogic(self.data_wrapper)
        self.player_logic = PlayerLogic(self.data_wrapper)
        self.team_logic = TeamLogic(self.data_wrapper)
        #self.tournament_logic = TournamentLogic(self.data_wrapper)
    
    def create_player(self, player):
        return self.player_logic.create_player(player)

    def list_all_players(self):
        return self.player_logic.list_all_players()
    
    #def create_tournament(self, tournament):
    #    return self.tournament_logic.create_tournament()


    #def create_team(self, team):
    #    return self.team_logic.create_team()
