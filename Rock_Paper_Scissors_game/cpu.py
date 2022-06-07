from random import randint
from actions import Rps

class Cpu:
    def __init__(self, lives, name):
        self.lives = lives
        self.name = name

    def get_action(self):
        cpu_action = Rps(randint(0, len(Rps) - 1))
        return cpu_action
    
    def get_lives(self):
        return self.lives
    
    def get_name(self):
        return self.name