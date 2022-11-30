import csv
#from model.team import Team
from model.player import Player

class Team_Data:
    def __init__(self):
        self.file_name = 'files/teams.csv'

    def create_team(self, team):
        with open(self.file_name, 'a', newline='', encoding = 'utf-8') as csvfile:
            fieldnames = ['player', 'id', 'name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'player': team.player, 'id': team.id, 'name': team.name})

    def list_all_teams(self):
        return_list = []
        with open(self.file_name, newline='', encoding = 'utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                return_list.append(Player(row['player'], row['id'], row['name']))
        return return_list