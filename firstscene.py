import mapFirstgame

class firstscene(gamemap):
    def start(self):
        print "this is the start of scene#1"
        print "no matter what you say, you are going to scene 2"
        answer = raw_input(">")
        return "second"

