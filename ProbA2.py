import numpy as np
from matplotlib import pyplot as plt

#Written by Christopher Ferrier for CHE 3102 Problem A2 Spring 2021

#Problem 3-57 from 5th Edition Cengal
#(Thermal Contact Resistance)
#Inconel plate of 12mm coated with a 300 um layer of TBC
#k = 10500 W/m2K at interface
#k_inc = 25 W/mK
#k_tbc = 1.5 W/mK
#plate surrounded by combustion gas at 1773.15C
#h = 750 W/m2K
#Ts = 1473.15 K

#Declaring constants
h_int = 10500
h_surr = 750
k_inc = 25
k_tbc = 1.5
t_s = 1473.15
t_surr = 1773.15
l_plate = 12E-3
l_tbc = 300E-6
q_conv = h_surr*(t_surr-t_s)


#Defining Functions
def total_resistance(platedepth):
    x = (platedepth/k_inc) + (1/h_int) + (l_tbc/k_tbc)
    return x

def platetemp(resistance):
    x = t_s - (q_conv*resistance)
    return x

#Finding temperature at midpoint
midpoint_temp = platetemp(total_resistance(l_plate/2))
print("The temperature at the midpoint of the plate is " + str(midpoint_temp) + " K")

#Plotting temperature over full thickness of plane
#Depth 0 is temp at interface
#Last depth is temp on other side
depths = np.arange(0,12E-3+0.5E-4,0.5E-4)
temps = platetemp(total_resistance(depths))

#Plotting temps of plate from interface to other side of plate
plt.plot(depths,temps)
plt.title('Temperature vs Plate Depth')
plt.xlabel("Plate Depth (m)")
plt.ylabel('Temperature (K)')
plt.show()



