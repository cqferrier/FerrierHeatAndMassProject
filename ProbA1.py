import numpy as np
from matplotlib import pyplot as plt

#Written by Christopher Ferrier for CHE 3102 Project A1 and A2
#Ver 1 started on 03/22/2021

#Problem Statement:
#Brick wall (alpha = 4.72E-7) with thickness 0.5m has T0 = 300K
#Determine time for center to reach 425 K if surfaces raised to and
#maintained at 425 and 600 K

#Defining constants
alpha = 4.72E-7
totallength = 0.5

#creating 101 nodes because node 0 is at edge of wall and node 100 is at other edge
nodes = 101
dx = totallength / (nodes-1)
dt = 0.5 * ((dx**2)/alpha)
tau = (alpha*dt)/(dx**2)

#defines an array with nodes 0 through 100,
ansarray = np.zeros((10000, nodes+1))
ansarray[0,1:nodes+1] = np.arange(nodes)
ansarray[1:2448,0] = np.arange(0, 64800, dt)
ansarray[1:2448,1] = 425
ansarray[1:2448,nodes] = 600
ansarray[1,2:nodes] = 300

#creating temperature distribution with a for loop
for j in range(2447):
	for i in range(nodes-2):
		ansarray[j+2,i+2] = (tau*(ansarray[j+1,i+3] + ansarray[j+1,i+1])) + ((1-(2*tau))*ansarray[j+1,i+2])

#Finding time at which node 50 reaches 425
for j in range(2447):
	if ansarray[j,51] >= 424.9:
		time = ansarray[j,0]
		exacttemp = ansarray[j,51]
		break

#Converting time to hrs and creating console message with exact answer
timehr = time/3600
msg = "It takes %f s or %f hr for the center of the wall to reach 425 K" % (time,timehr)
print(msg)

#Plotting the temperature over location
yrange = ansarray[1:2448,52]
xrange = ansarray[1:2448,0]/3600
plt.plot(xrange,yrange)
plt.title("Temperature of Midpoint vs Time")
plt.xlabel("Time (hr)")
plt.ylabel("Temperature (K)")
plt.hlines(exacttemp, 0, (64800/3600), colors = 'orange', linestyles = "dashed")
plt.text(2, 426, '425 K', color = 'orange')
plt.show()
