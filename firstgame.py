from sys import exit


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
        
class firstscene(object):

    def start(self):
        print "this is the start of scene#1"
        print "no matter what you say, you are going to scene 2"
        answer = raw_input(">")
        return "second"

class secondscene(object):
    def start(self):
        print "say a number bigger than 5"
        try:
            answer = int(raw_input("> "))
        except ValueError:
            print "we teleport you back to the first scene"
            return "first"
        if answer > 5:
            print "good boy, you can go to the final scene"
            return "final"
        else:
            return "first"
class finalscene(object):
    def start(self):
        print "final scene"
        print """if you arrived here it means that the raptile god has been in
        a good mood :)) now go get that Holy Grail
        """
        quit()
       
myMap = gamemap()
myEngine = engine(myMap)
myEngine.startingScene()
