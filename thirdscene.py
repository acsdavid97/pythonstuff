import mapFirstgame
import random import randint

class thirdscene(self):
    def start(self):
        print "you have to guess a natural number between 0 and 9"
        print "you have 3 chances, the random number won't change"
        rand = randint(1,9)
        for i in range (1, 3, 1)
            guess = int(raw_input("> "))
            if rand == guess:
                print "nice job!"
                return "final"
            else:
                print "try again"
        return "death"

