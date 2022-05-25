import random

class Agent():

    
    def __init__(self, environment, agents, heatmap):
        '''
        Initialises an agent


        
        :param: environment: List containing lists of numbers
            This is a 2D dataset containing the town layout including the pub and house locations.

        :param: heatmap: List containing lists of numbers
            This is a 2D dataset containing data for the density of drunks passing through each point on the map.

        :param: agents: List of agents
            This is the list of drunks, this list size may be adjusted however for the purpose of this exercise the 'num_of_agents = 25'.

        
        :return None.:
        
        '''
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
        '''
        Utilises the makemove and random.randist functions to give...
            - a 2/6 chance for the agent to move towards the correct house 
            - a 4/6 chance to move in a random cardinal direction

            50% chance to move towards the correct house and 50% chance to move in another direction
        '''
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
        '''
        Checks if the movement location is viable
            - Movement is only allowed onto an agents own house tile or a tile with environment value 0, prevents movement through the pub/other houses


        
        :param: newy:
            This is the environment x coordinate that the agent will move to

        :param: newx: 
            This is the environment x coordinate that the agent will move to

        
        :return: True
            if the move is possible
        
        :return: False
            if the move is not possible
        '''
        if self.environment[newx][newy] == self.house:
            self.isHome = True
            return True
        elif self.environment[newx][newy] == 0:
            return True
        else:
            return False

    def sethouse(self, housenum):
        '''
        Framework for unique house assignment and stores house location
            - House assignment occurs in model.py using this function
        '''
        self.house = housenum
        for i in range(len(self.environment)):
            for j in range(len(self.environment)):
                if self.environment[i][j] == self.house:
                    self.housepos_x = j
                    self.housepos_y = i
                    return

    def makemove(self, direction):
        '''
        Sets up directional movement for use in the move function


        
        :param: direction:
            Compares variable to direction to enable progressing through correct if statement

        
        :return: None
        '''
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

            
