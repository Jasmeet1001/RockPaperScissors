from actions import Rps

class Player:
    def __init__(self, lives, name):
        self.lives = lives
        self.name = name

    def get_action(self):
        choices = ", ".join([f"{action.name}[{action.value}]" for action in Rps])
        usr_action = input(f'Enter choice ({choices}): ')
        player_action = Rps(int(usr_action))
        
        return player_action

    def get_lives(self):
        return self.lives

    def get_name(self):
        return self.name