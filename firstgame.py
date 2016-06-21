from sys import exit
from firstscene import firstscene
from secondscene import secondscene
from finalscene import finalscene


class gamemap(object):

    def __init__(self):
        self.currScene = "first"
        self.scenes = {
            "first": firstscene(),
            "second": secondscene(),
            "final": finalscene()
            }
        
    def nextScene(self):
        print "current scene is: %r" % self.currScene
        self.currScene=self.scenes[self.currScene].start()

class engine(object):
    def __init__(self,gamemap):
        self.gamemap=gamemap
        
    def startingScene(self):
        print "this is the starting scene"
        print "are you sure you want to continue?"
        answer = raw_input("> ")
        if answer == "yes":
            self.play()
        else:
            self.exit()
            
    def play(self):
        while(self.gamemap.currScene!="final"):
            self.gamemap.nextScene()
        finalscene().start()
    def exit(self):
        print "exiting"
        exit(0)

       
myMap = gamemap()
myEngine = engine(myMap)
myEngine.startingScene()
