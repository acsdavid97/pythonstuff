class gamemap(object):
    def __init__(self):
        self.first=firstscene()
        self.currScene = "first"
    def nextScene(self):
        self.currScene=self.scenes[self.currScene]
    
        


        
