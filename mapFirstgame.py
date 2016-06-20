class gamemap(object):
    def __init__(self):
        self.scenes = ["first", "second", "third"]
        self.currScene = self.scenes[0]
    def currentScene(self):
        return self.currScene

        
