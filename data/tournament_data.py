import csv
from model.tournament import Tournament

class TournamentData:
    def __init__(self):
        self.file_name = 'files/tournament.csv'

    def create_tournament(self, tournament):
        with open(self.file_name, 'a', newline='', encoding = 'utf-8') as csvfile:
            fieldnames = ['team_id','team', 'organizer_name', 'phone_number', 'start_date', 'end_date', 'number_of_matches', 'tournament_name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'team_id': tournament.team_id, 'team': tournament.team, 'organizer_name': tournament.organizer_name, 'phone_number': tournament.phone_number, 'start_date': tournament.start_date, 'end_date': tournament.end_date, 'number_of_matches': tournament.number_of_matches, 'tournament_name': tournament.tournament_name})

    #def list_all_tournament(self):
        #return_list = []
        #with open(self.file_name, newline='', encoding = 'utf-8') as csvfile:
        #    reader = csv.DictReader(csvfile)
        #    for row in reader:
        #       return_list.append(Tournament(row['team_id'], row['team'], row['organizer_name'], row['phone_number'], row['start_date'], row['end_date'], row['number_of_matches'], row['tournament_name']))
        #return return_list

