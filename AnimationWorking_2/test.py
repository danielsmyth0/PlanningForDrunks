from msilib.schema import Environment
import agentframework
import unittest
import csv
import os

'''
Planning for drunks - Unit testing
'''

class TestAgents(unittest.TestCase):

    '''
    __init__ function test
    '''
    def test_init(self):
        environment = []
        heatmap = []
        agents = []
        testagent = agentframework.Agent(environment, heatmap, agents)
        self.assertEqual(testagent.environment, environment)
        self.assertEqual(testagent.heatmap, heatmap)
        self.assertEqual(testagent.agents, agents)
        self.assertEqual(testagent.house, 0)
        self.assertEqual(testagent.isHome, False)
        self.assertEqual(testagent.housepos_x, 0)
        self.assertEqual(testagent.housepos_y, 0)
        self.assertEqual(testagent._x, 150)
        self.assertEqual(testagent._y, 150)


    '''
    movecheck function test
    '''
    def test_movecheck_agentathome(self):
        heatmap = []
        agents = []
        environment = self.importenvironment('agenthometrue.txt')
        testagent = agentframework.Agent(environment, agents, heatmap)
        testagent.house = 10
        self.assertTrue(testagent.movecheck(0,0))

    def test_movecheck_normalmove(self):
        heatmap = []
        agents = []
        environment = self.importenvironment('agenthometrue.txt')
        testagent = agentframework.Agent(environment, agents, heatmap)
        testagent.house = 10
        self.assertTrue(testagent.movecheck(5,5))

    def test_movecheck_else(self):
        heatmap = []
        agents = []
        environment = self.importenvironment('agenthometrue.txt')
        testagent = agentframework.Agent(environment, agents, heatmap)
        testagent.house = 10
        self.assertFalse(testagent.movecheck(9,9))


    '''
    sethouse function test
    '''
    def test_sethouse(self):
        heatmap = []
        agents = []
        environment = self.importenvironment('agenthometrue.txt')
        testagent = agentframework.Agent(environment, agents, heatmap)
        testagent.sethouse(10)
        self.assertEqual(testagent.house, 10)
        self.assertEqual(testagent.housepos_x, 0)
        self.assertEqual(testagent.housepos_y, 0)


    '''
    testing makemove function - valid move left
    '''    
    def test_makemove_left_validmove(self):
        agents = []
        heatmap = self.importenvironment('base.txt')
        environment = self.importenvironment('agenthometrue.txt')
        testagent = agentframework.Agent(environment, agents, heatmap)
        testagent.house = 10
        testagent._x = 3
        testagent._y = 3
        testagent.makemove('left')
        self.assertEqual(testagent._x, 2)
        self.assertEqual(testagent._y, 3)

    '''
    testing makemove function - invalid move left
    '''
    def test_makemove_left_invalidmove(self):
        agents = []
        heatmap = self.importenvironment('base.txt')
        environment = self.importenvironment('agenthometrue.txt')
        testagent = agentframework.Agent(environment, agents, heatmap)
        testagent.house = 10
        testagent._x = 2
        testagent._y = 1
        testagent.makemove('left')
        self.assertEqual(testagent._x, 2)
        self.assertEqual(testagent._y, 1)


    '''
    testing makemove function - valid move right
    '''
    def test_makemove_right_validmove(self):
        agents = []
        heatmap = self.importenvironment('base.txt')
        environment = self.importenvironment('agenthometrue.txt')
        testagent = agentframework.Agent(environment, agents, heatmap)
        testagent.house = 10
        testagent._x = 3
        testagent._y = 3
        testagent.makemove('right')
        self.assertEqual(testagent._x, 4)
        self.assertEqual(testagent._y, 3)

    '''
    testing makemove function - invalid move right
    '''
    def test_makemove_right_invalidmove(self):
        agents = []
        heatmap = self.importenvironment('base.txt')
        environment = self.importenvironment('agenthometrue.txt')
        testagent = agentframework.Agent(environment, agents, heatmap)
        testagent.house = 10
        testagent._x = 0
        testagent._y = 1
        testagent.makemove('right')
        self.assertEqual(testagent._x, 0)
        self.assertEqual(testagent._y, 1)

    
    '''
    testing makemove function - valid move up
    '''
    def test_makemove_up_validmove(self):
        agents = []
        heatmap = self.importenvironment('base.txt')
        environment = self.importenvironment('agenthometrue.txt')
        testagent = agentframework.Agent(environment, agents, heatmap)
        testagent.house = 10
        testagent._x = 3
        testagent._y = 3
        testagent.makemove('up')
        self.assertEqual(testagent._x, 3)
        self.assertEqual(testagent._y, 2)

    '''
    testing makemove function - invalid move up
    '''
    def test_makemove_up_invalidmove(self):
        agents = []
        heatmap = self.importenvironment('base.txt')
        environment = self.importenvironment('agenthometrue.txt')
        testagent = agentframework.Agent(environment, agents, heatmap)
        testagent.house = 10
        testagent._x = 1
        testagent._y = 2
        testagent.makemove('up')
        self.assertEqual(testagent._x, 1)
        self.assertEqual(testagent._y, 2)


    '''
    testing makemove function - valid move down
    '''
    def test_makemove_down_validmove(self):
        agents = []
        heatmap = self.importenvironment('base.txt')
        environment = self.importenvironment('agenthometrue.txt')
        testagent = agentframework.Agent(environment, agents, heatmap)
        testagent.house = 10
        testagent._x = 3
        testagent._y = 3
        testagent.makemove('down')
        self.assertEqual(testagent._x, 3)
        self.assertEqual(testagent._y, 4)

    '''
    testing makemove function - invalid move down
    '''
    def test_makemove_down_invalidmove(self):
        agents = []
        heatmap = self.importenvironment('base.txt')
        environment = self.importenvironment('agenthometrue.txt')
        testagent = agentframework.Agent(environment, agents, heatmap)
        testagent.house = 10
        testagent._x = 1
        testagent._y = 0
        testagent.makemove('down')
        self.assertEqual(testagent._x, 1)
        self.assertEqual(testagent._y, 0)
        


    '''
    Importing test environment
    '''
    def importenvironment(self, filename):
        testenvironments = []
        testenvironments_filepath = os.path.join('.', 'testenvironments')
        file = os.path.join(testenvironments_filepath, filename)
        with open (file, newline='') as q0:
            dataset = csv.reader(q0, quoting=csv.QUOTE_NONNUMERIC)
            for row in dataset:
                rowlist = []
                for value in row:
                    rowlist.append(float(value))
                testenvironments.append(rowlist)
        return testenvironments

if __name__ == '__main__':
    unittest.main()
