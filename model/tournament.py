from model.team import Team
class Tournament():
    def __init__(self, team="", organizer_name="", phone_number=0, start_date="", end_date="", number_of_matches=0, tournament_name=""):
        
        self.team = Team(self.team).id
        self.organizer_name = organizer_name
        self.phone_number = phone_number
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_matches = number_of_matches
        self.tournament_name = tournament_name

    def __str__(self):
        return f"{self.team}, {self.organizer_name}, {self.phone_number}, {self.start_date}, {self.end_date}, {self.number_of_matches}, {self.tournament_name}"