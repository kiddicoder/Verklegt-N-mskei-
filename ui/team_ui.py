from logic.team_logic import TeamLogic
from model.team import Team
from ui.input_validators import *

class Team_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def output_team_menu(self):
        print('Team Menu')
        print('1) Create Team')
        print('2) List all teams')
        print('b) go back')

    
    def team_imput_prompt(self):
        while True:
            self.output_team_menu()
            the_question = input("Enter your command: ")
            the_question = the_question.lower()
            if the_question == "b":
                print("Going back!")
                return "b"
            elif the_question == "1":
                the_team = Team()
                while True:
                    the_team.name = input("Enter your team name: ")
                    try:
                        name_validator(the_team.name())
                        break
                    except NameLengthException:
                        print("Team name is too long")
                    except:
                        print("An error was found")
                
                self.logic_wrapper.create_team(the_team)
            elif the_question == "2":
                pass
