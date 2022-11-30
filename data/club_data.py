import csv
from model.club import Club
from model.player import Player

class ClubData:
    def __init__(self):
        self.file_name = 'files/clubs.csv'

    def create_club(self, club):
        with open(self.file_name, 'a', newline='', encoding = 'utf-8') as csvfile:
            fieldnames = ['name', 'id', 'address', 'phone', 'teams']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': club.name, 'id': club.id, 'address': club.address, 'phone': club.phone, 'team': club.team })

    def list_all_clubs(self):
        return_list = []
        with open(self.file_name, newline='', encoding = 'utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                return_list.append(Player(row['name'], row['id'], row['address'], row['phone'], row['team']))
        return return_list