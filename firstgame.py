from sys import exit
import mapFirstgame

class engine(object):
    def startingScene(self):
        print "this is the starting scene"
        print "are you sure you want to continue?"
        answer = raw_input("> ")
        if answer == "yes":
            self.play()
        else:
            self.exit()
    def play(self):
        print "playing"
    def exit(self):
        print "exiting"
        exit(0)

  

myEngine = engine()
myEngine.startingScene()
myMap = mapFirstgame.gamemap()
print myMap.currentScene()
