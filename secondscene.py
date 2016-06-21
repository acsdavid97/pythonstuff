class secondscene(object):
    def start(self):
        print "say a number bigger than 5"
        try:
            answer = int(raw_input("> "))
        except ValueError:
            print """we teleport you back to the first scene, since you do not know what a number is
                OR you deliberately want to sabotage my program, but I got exception handling HA
                """
            return "first"
        if answer > 5:
            print "good boy, you can go to the final scene"
            return "final"
        else:
            return "first"
