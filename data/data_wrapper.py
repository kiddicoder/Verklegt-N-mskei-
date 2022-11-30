from data.player_data import PlayerData
from data.tournament_data import TournamentData

class DataWrapper:
    def __init__(self):
        self.player_data = PlayerData()
        self.tournament_data = TournamentData()

    def list_all_players(self):
        return self.player_data.list_all_players()

    def create_player(self, player):
        return self.player_data.create_player(player)

    def create_tournament(self, tournament):
        return self.tournament_data.create_tournament(tournament)
        