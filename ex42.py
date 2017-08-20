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

        while True:
            print "\n--------"
            room = getattr(self, next)
            next = room()


    def death(self):
        print self.quips[randint(0, len(self.quips)-1)]
        exit(1)

    def central_corridor(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
