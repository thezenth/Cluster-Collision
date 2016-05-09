import os
import numpy as np

def read_csv(file_name, n):
    data = np.zeros(5,n) #Make a multidimensional numpy array of zeros, with n number of arrays, and each array having 5 entries (id, mass, x, y, z)
    print (data)
    
    f = open(file_name, "r")
    for line in f:
        if not line.contains("id")
            id_idx = line.index(",")
            m_idx = line.index("kg,")
            x_idx = line.index("uh") #Manually insert some sort of custom indexer value for x, y, z positions?
            ident = line[:id_idx]
            mass = line[id_idx:m_idx]
            #etc
            data[line][0] = ident

