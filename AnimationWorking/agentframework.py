import random

class Agent():

    '''definine __init__ function to create agents'''
    def __init__(self, environment, agents, heatmap):
        self.environment = environment
        self.agents = agents
        self.heatmap = heatmap
        self.house = 0
        self.isHome = False
        self._x = 150
        self._y = 150
        
        
    def move(self):
        if not self.isHome:
            rand = random.randint(1, 4)
            if rand == 1:
                newy = min( (self._y + 1), 299)
                if self.movecheck(newy, self._x):  
                    self._y = newy
                    self.heatmap[self._y][self._x] += 1
            elif rand == 2:
                newy = max( (self._y - 1), 0)
                if self.movecheck(newy, self._x):  
                   self._y = newy
                   self.heatmap[self._y][self._x] += 1
            elif rand == 3:
                newx = min( (self._x + 1), 299)
                if self.movecheck(self._y, newx):
                    self._x = newx
                    self.heatmap[self._y][self._x] += 1
            else:
                newx = max( (self._x - 1), 0)
                if self.movecheck(self._y, newx):
                    self._x = newx
                    self.heatmap[self._y][self._x] += 1
            return False
        else:
            return True
                    
            
    def movecheck(self, newx, newy):
        if self.environment[newx][newy] == self.house:
            self.isHome = True
            return True
        elif self.environment[newx][newy] == 0 or self.environment[newx][newy] == 1:
            return True
        else:
            return False
        
            
        
        
