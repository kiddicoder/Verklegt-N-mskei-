import csv
from model.match import Match

class MatchData:
    def __init__(self):
        self.file_name = 'files/match.csv'

    def create_match(self, match):
        with open(self.file_name, 'a', newline='', encoding = 'utf-8') as csvfiles:
            fieldnames = ['home team', 'away team', 'home player', 'away player', 'results', 'date of match', 'new date of match']
            writer = csv.DictWriter(csvfiles, fieldnames=fieldnames)

            writer.writerow({'home team': match.home_team, 'away team': match.away_team, 'home player': match.home_player, 'away player': match.away_player, 'results': match.ResultsOfMatch, 'date of match': match.DateOfMatch, 'new date of match': match.PostponeMatch })

    #veit ekki hvað á að gera í neðra
