from data.player_data import PlayerData
from model.player import Player

class PlayerLogic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_player(self, player):
        self.data_wrapper.create_player(player)

    def list_all_players(self):
        return self.data_wrapper.list_all_players()
