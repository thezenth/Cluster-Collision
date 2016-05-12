import os
import numpy as np

# -- MATPLOTLIB -- #
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#class star:
#    def __init__(self, identifier, mss, xpos, ypos, zpos):
#        self.ID = identifier
#        self.mass = mss
#        
#        #Position
#        self.x = xpos
#        self.y = ypos
#        self.z = zpos

def read_csv(file_name, n):
    #ALWAYS MAKE SURE THE NUMPY.ZEROS HAS TWO SETS OF BRACKETS
    data = np.zeros((n, 5)) #Make an empty list for the stars
    print (data)
    
    f = open(file_name, "r")
    i = 0
    for line in f:
        if "id" not in line:
            id_idx = line.index(",")
            m_idx = line.index("M,")
            x_idx = line.index("X,") #Manually insert some sort of custom indexer value for x, y, z positions?
            y_idx = line.index("Y,")
            z_idx = line.index("Z")
            ident = line[:id_idx]
            mass = line[id_idx+1:m_idx]
            x = line[m_idx+2:x_idx]
            y = line[x_idx+2:y_idx]
            z = line[y_idx+2:z_idx]

            #new_star = star(ident, mass, x, y, z)
            #data.append(new_star)


            data[i][0] = float(ident) #Put data into the array
            data[i][1] = float(mass) #Line - 1 because the loop skips the first line
            data[i][2] = float(x)
            data[i][3] = float(y)
            data[i][4] = float(z)
            i+=1


    return data

path1 = "time_0.0.txt"

#def to_plot(plot_data):
#    fig = plt.figure()
#    ax = fig.add_subplot(111, projection='3d')
#    ax.scatter(
#        
#    )

print (read_csv(path1, 125))
