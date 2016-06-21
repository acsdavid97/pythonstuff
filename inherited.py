print "import begins"

from inheritance import *

class subclassy(classy):
    def p(self):
        print self.value
testclass = subclassy(5)
testclass.p()
