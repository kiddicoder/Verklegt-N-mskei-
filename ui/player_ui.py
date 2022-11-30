from logic.player_logic import PlayerLogic
from model.player import Player
from ui.input_validators import *

class Player_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def output_menu(self):
        print('Player menu')
        print('1) Create player')
        print('2) List all players')
        print('b) to go back')
        print('q) to quit')

    def input_prompt(self):
        while True:
            self.output_menu()
            command = input('Enter your command: ')
            command = command.lower()
            if command == 'b':
                print('going back')
                return 'b'
            elif command == 'q':
                print('goodbye!')
                return 'q'
            elif command == '1':
                p = Player()
                while True:
                    p.name = input('Enter the name of the player: ')
                    try:
                        name_validator(p.name)
                        break
                    except NameLengthException:
                        print('Name is too long')
                    except:
                        print('Some error')
                while True:
                    p.player_id = input('Enter the player id: ')
                    try:
                        id_validator(p.player_id)
                        break
                    except NameLengthException:
                        print("Please enter a 10 digit ID number")
                    except NotANumber:
                        print("Please enter numbers only")
                    except:
                        print('Some error')
                while True:
                    p.address = input('Enter the address of the player: ')
                    try:
                        address_validator(p.address)
                        break
                    except NameLengthException:
                        print("Address name is too long")
                    except:
                        print("Some error")
                while True:
                    p.email = input('Enter the email of the player: ')
                    try:
                        email_validator(p.email)
                        break
                    except NameLengthException:
                        print('Email is to long')
                    except:
                        print('Some error')
                while True:
                    p.gsm = input('Enter the mobile phone number of the player: ')
                    try:
                        phone_validator(p.gsm)
                        break
                    except NameLengthException:
                        print("Please enter a 7 digit phone number")
                    except NotANumber:
                        print("Please enter numbers only")
                    except:
                        print("Some error")
                while True:
                    p.phone = input('Enter the phone number of the player: ')
                    try:
                        phone_validator(p.phone)
                        break
                    except NameLengthException:
                        print("Please enter a 7 digit phone number")
                    except NotANumber:
                        print("Please enter numbers only")
                    except:
                        print("Some error")
                while True:
                    p.role = input('Enter the role of the player: ')
                    try: 
                        role_validator(p.role)
                        break
                    except SyntaxError:
                        print('please enter either "captain" or "player"')
                    except:
                        print('Some error')
                self.logic_wrapper.create_player(p)   
                #while True:      
                    #p.team = input('Enter the name of the players team: ')
                    #try:
            elif command == '2':
                result = self.logic_wrapper.list_all_players()
                for elem in result:
                
                    print(f'name: {elem.name}, id: {elem.player_id}, address: {elem.address}, email: {elem.email}, mobile phone: {elem.gsm}, phone: {elem.phone}, role: {elem.role}, team: {elem.team}')
            else: 
                print('invalid input, try again')
