import os
import numpy as np

def read_csv(file_name, n):
    data = np.zeros(5,n) #Make a multidimensional numpy array of zeros, with n number of arrays, and each array having 5 entries (id, mass, x, y, z)
    print (data)
    
    f = open(file_name, "r")
    for line in f:
        if not line.contains("id")
            id_idx = line.index(",")
            m_idx = line.index("M,")
            x_idx = line.index("X,") #Manually insert some sort of custom indexer value for x, y, z positions?
            y_idx = line.index("Y,")
            z_idx = line.index("Z")
            ident = line[:id_idx]
            mass = line[id_idx:m_idx]
            x = line[m_idx:x_idx]
            y = line[x_idx:y_idx]
            z = line[y_idx:z_idx]
            data[line-1][0] = ident #Put data into the array
            data[line-1][1] = mass #Line - 1 because the loop skips the first line
            data[line-1][2] = x
            data[line-1][3] = y
            data[line-1][4] = z
    return data
    

