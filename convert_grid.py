import pandas as pd
import numpy as np
import parameters
import os

dir = 'simplified_fields_vtk'
if not os.path.exists(dir):
    os.mkdir(dir)

for t in range(parameters.timesteps):
    print(t)
    filename = './fields_csv/' +str(t) + '.csv'
    d = pd.read_csv(filename, usecols=['Result'])
    dataframe = pd.DataFrame(d)
    values = np.array(dataframe)
    file1 = open('./simplified_fields_vtk/data_' + str(t) + '.vtk',"w")
    file1.write('# vtk DataFile Version 5.1\nvtk output\nASCII\nDATASET STRUCTURED_POINTS\nDIMENSIONS ' + str(parameters.length) + ' ' + str(parameters.breadth) +  ' 1' + '\nSPACING 1 1 1\nORIGIN 0 0 0\nPOINT_DATA ' + str(parameters.length*parameters.breadth) + '\nSCALARS Result double\nLOOKUP_TABLE default\n')
    for i in values:
        file1.write(str(i[0]) + "\n")

print("Grid Conversion Done")