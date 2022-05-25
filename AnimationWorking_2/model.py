import random
import os
import csv
import matplotlib.pyplot as mpl
import matplotlib.animation 
import agentframework
import matplotlib
#matplotlib.use('TkAgg')
#import tkinter








'''Set up directories'''
main = os.getcwd()
print (main)
inputs = os.path.join('.', 'input')
print ("Input files are located " + inputs)
outputs = os.path.join('.', 'output')
print ("Output files are located " + outputs)


'''Set up parameters'''
num_of_agents = 25
iteration_num = 0
environment = []
agents = []
heatmap = []
fig = mpl.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])



'''Set up environment: contains data relating to the spatial environment upon which the agents act'''
file = os.path.join(inputs, 'drunk.txt')
with open (file, newline='') as q0:
    dataset = csv.reader(q0, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset:
        rowlist = []
        for value in row:
            rowlist.append(float(value))
        environment.append(rowlist)


'''Set up heatmap: contains data upon which the agents will change based upon the density of agents'''
file = os.path.join(inputs, 'heatmapin.txt')
with open (file, newline='') as q0:
    dataset = csv.reader(q0, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset:
        rowlist = []
        for value in row:
            rowlist.append(float(value))
        heatmap.append(rowlist)


'''Make the agents'''
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, heatmap))
    
'''Assign agent houses''' 
for i in range(num_of_agents):
    agents[i].sethouse((i+1)*10)


'''Define generator function for animation'''
def gen_function(b = [0]):
    a = 0
    global num_of_agents
    while  num_of_agents > 0:
        yield a			
        a = a + 1

'''Define update function for animation'''
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

    '''Plot environment + agents'''
    mpl.xlim(0, 299)
    mpl.ylim(0, 299)
    '''change 'environment' to 'heatmap' to display density map'''
    mpl.imshow(environment)
    for i in range(num_of_agents):
        mpl.scatter(agents[i]._x,agents[i]._y, color = "grey")

'''Define function to execute model - GUI. This works however breaks the heatmap export and therefore is commented out'''
#def run():
#    animation = matplotlib.animation.FuncAnimation(fig, update, interval=0.01, repeat=False, frames=gen_function) 
#    canvas.draw()
animation = matplotlib.animation.FuncAnimation(fig, update, interval=0.01, repeat=False, frames=gen_function) 
matplotlib.pyplot.show()

'''Environment Data output'''
file = os.path.join(outputs, 'output_env.csv')
with open(file, 'w', newline='') as q1:
    writer = csv.writer(q1, delimiter=',')
    for row in environment:
        writer.writerow(row)
print("Environment data is located in " + file)


'''Density Data output'''
file = os.path.join(outputs, 'output_heatmap.csv')
with open(file, 'w', newline='') as q1:
    writer = csv.writer(q1, delimiter=',')
    for row in heatmap:
        writer.writerow(row)
print("Heatmap data is located in " + file)


#'''Set up GUI'''
#root = tkinter.Tk()
#root.wm_title("Planning for drunks")
#canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
#canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
#menu_bar = tkinter.Menu(root)
#root.config(menu=menu_bar)
#model_menu = tkinter.Menu(menu_bar)
#menu_bar.add_cascade(label="Execute Model", command = run)
#tkinter.mainloop()
