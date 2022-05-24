import random

class Agent():

    ''''''
    def __init__(self, environment, agents, heatmap):
        self.environment = environment
        self.agents = agents
        self.heatmap = heatmap
        self.house = 0
        self.isHome = False
        self.housepos_x = 0
        self.housepos_y = 0
        self._x = 150
        self._y = 150
        
        
    def move(self):
        if not self.isHome:
            rand = random.randint(1, 6)
            if rand == 1:
                self.makemove('down')
            elif rand == 2:
                self.makemove('up')
            elif rand == 3:
                self.makemove('left')
            elif rand == 4:
                self.makemove('right')
            else:
                horizonaldistance = self._x - self.housepos_x
                verticaldistance = self._y - self.housepos_y
                if (abs(horizonaldistance)>abs(verticaldistance)):
                    if (self.housepos_x > self._x):
                        self.makemove('right')
                    else:
                        self.makemove('left')

                else:
                    if (self.housepos_y > self._y):
                        self.makemove('down')
                    else:
                        self.makemove('up')
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

    def sethouse(self, housenum):
        self.house = housenum
        for i in range(len(self.environment)):
            for j in range(len(self.environment)):
                if self.environment[i][j] == self.house:
                    self.housepos_x = j
                    self.housepos_y = i
                    return

    def makemove(self, direction):
        if direction == 'left':
            newx = max( (self._x - 1), 0)
            if self.movecheck(self._y, newx):
                self._x = newx
                self.heatmap[self._y][self._x] += 1
        elif direction == 'right':
            newx = min( (self._x + 1), 299)
            if self.movecheck(self._y, newx):
                self._x = newx
                self.heatmap[self._y][self._x] += 1
        elif direction == 'up':
            newy = max( (self._y - 1), 0)
            if self.movecheck(newy, self._x):  
                self._y = newy
                self.heatmap[self._y][self._x] += 1
        elif direction == 'down':
            newy = min( (self._y + 1), 299)
            if self.movecheck(newy, self._x):  
                self._y = newy
                self.heatmap[self._y][self._x] += 1

            
