import random
import os
import csv
import matplotlib.pyplot as mpl
import matplotlib.animation 
import agentframework


'''Set up directories'''
main = os.getcwd()
print (main)
inputs = os.path.join('.', 'input')
print ("Input files are located " + inputs)
outputs = os.path.join('.', 'output')
print ("Output files are located " + outputs)


'''Set up variables'''
num_of_agents = 25
iteration_num = 0
environment = []
agents = []
heatmap = []
fig = mpl.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])




'''Set up environment'''
file = os.path.join(inputs, 'drunk.txt')
with open (file, newline='') as q0:
    dataset = csv.reader(q0, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset:
        rowlist = []
        for value in row:
            rowlist.append(float(value))
        environment.append(rowlist)

'''Set up heatmap'''
file = os.path.join(inputs, 'heatmapin.txt')
with open (file, newline='') as q0:
    dataset = csv.reader(q0, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset:
        rowlist = []
        for value in row:
            rowlist.append(float(value))
        heatmap.append(rowlist)
        
'''Make the Agents'''
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, heatmap))
    
'''Agent Actions Assign house''' 
for i in range(num_of_agents):
    while i < num_of_agents:
        agents[0].agents[i].house +=10
        i = i + 1

'''Agent Actions Move'''



def gen_function(b = [0]):
    a = 0
    global num_of_agents
    while  num_of_agents > 0:
        yield a			#: Returns control and waits next call.
        a = a + 1

def update(frame_number):
    global iteration_num
    global num_of_agents
    global agents
    fig.clear()
    iteration_num += 1
    newagents = []
    print("iteration number: ", iteration_num)
    random.shuffle(agents)
    for i in range(num_of_agents):
        if not agents[i].move():
            newagents.append(agents[i])
    agents = newagents
    num_of_agents = len(agents)

    mpl.xlim(0, 299)
    mpl.ylim(0, 299)
    mpl.imshow(environment)
    for i in range(num_of_agents):
        mpl.scatter(agents[i]._x,agents[i]._y, color = "grey")
    
animation = matplotlib.animation.FuncAnimation(fig, update, interval=0.01, repeat=False, frames=gen_function) 
matplotlib.pyplot.show()

'''Environment Data output'''
file = os.path.join(outputs, 'output_env.csv')
with open(file, 'w', newline='') as q1:
    writer = csv.writer(q1, delimiter=' ')
    for row in environment:
        writer.writerow(row)
print("Environment data is located in " + file)


'''Density Data output'''
file = os.path.join(outputs, 'output_heatmap.csv')
with open(file, 'w', newline='') as q1:
    writer = csv.writer(q1, delimiter=' ')
    for row in heatmap:
        writer.writerow(row)
print("Heatmap data is located in " + file)


