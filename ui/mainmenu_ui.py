from ui.player_ui import Player_UI
from logic.logic_wrapper import LogicWrapper
from ui.team_ui import Team_UI

class MainMenu_UI:
    def __init__(self):
        self.logic_wrapper = LogicWrapper

    def main_menu(self):
        print('Main menu')
        print('1) Player menu')
        print('2) Team menu')
        print('3) Club menu')
        print('4) Match menu')
        print('5) Tournament menu')
        print('q) to quit')

    def input_prompt(self):
        while True:
            self.main_menu()
            command = input('Choose menu: ')
            command = command.lower()
            if command == 'q':
                print('Goodbye!')
                break
            elif command == '1':
                menu = Player_UI(self.logic_wrapper())
                back_method = menu.input_prompt()
                if back_method == "q":
                    return "q"
            elif command == '2':
                team_menu = Team_UI(self.logic_wrapper())
            elif command == '3':
                pass
            elif command == '4':
                pass
            elif command == '5':
                pass
