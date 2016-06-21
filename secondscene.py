class secondscene(gamemap):
    def start(self):
        print "say a number bigger than 5"
        answer = int(raw_input("> "))
        if answer > 5:
            print "good boy, you can go to scene 3"
            return "third"
        else:
            return "first"
