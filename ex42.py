from sys import exit
from random import randint

class Game(object):

    def __init__(self, start):
        self.quips = [
            "You died.  You kinda suck at this.",
             "Your mom would be proud. If she were smarter.",
             "Such a luser.",
             "I have a small puppy that's better at this."
        ]
        self.start = start
        
