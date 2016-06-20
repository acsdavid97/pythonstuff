class car(object):

    def __init__(self):
        self.wheels = 4
    
    def honk(self):
        print "honk"
        
myCar = car()
myCar.honk()
print myCar.wheels ,"wheels"
