import sys
import os

neigh = { 0: 0, 1: 0, 2: 2, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0 }

class cell(object):
    def __init__(self, x, y):
        self.alive = 0
        self.pos = (x, y)
    
    def livesOrDies(self, neighbours):
        if(neigh[neighbours] != 2):
            self.alive = neigh[neighbours]
        else:
            self.alive = self.alive

class grid(object):
# The grid of cells 

    def __init__(self, n, m):
        self.dim = (0, 0)
        if n > 0 and m > 0:
            self.n = n
            self.m = m 
            # Creating a matrix of cell objects
            self.cellGrid = [ [cell(j, i) for i in range(0, m, 1)] for j in range(0, n ,1) ]
            self.cellGridAux = [ [cell(j, i) for i in range(0, m, 1)] for j in range(0, n ,1) ]
        else:
            quit()
            
    def liveNeigh(self, i, j):
        s = self.cellGrid[i - 1][j - 1].alive + self.cellGrid[i - 1][j].alive + self.cellGrid[i - 1][j + 1].alive + self.cellGrid[i][j - 1].alive + self.cellGrid[i][j + 1].alive + self.cellGrid[i + 1][j - 1].alive + self.cellGrid[i + 1][j].alive + self.cellGrid[i + 1][j + 1].alive
        return s
        
    def nextState(self):
        self.cellGridAux = self.cellGrid
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                self.cellGridAux[i][j].livesOrDies(self.liveNeigh(i,j))
        self.cellGrid = self.cellGridAux
        
    def printGrid(self):
        for i in range(0, self.n, 1):
            for j in range(0, self.m, 1):
                if self.cellGrid[i][j].alive == 1:
                    sys.stdout.write("*")
                else:
                    sys.stdout.write(".")
                sys.stdout.flush()
            print
            
    def readGrid(self,FILE):
        text = open(FILE)
        i = 0
        for line in text:
            for j in range(len(line)-1):
                if line[j] == '*':
                    self.cellGrid[i][j].alive = 1
                else:
                    self.cellGrid[i][j].alive = 0
            i += 1
            
myGrid = grid(4, 8)

myGrid.readGrid("gameinput.txt")
myGrid.printGrid()
print 
myGrid.nextState()
myGrid.printGrid()
        
                    
        
