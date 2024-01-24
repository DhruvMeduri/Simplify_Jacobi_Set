import pandas as pd
import numpy as np
#import vtk
import parameters

filename = "./tracking_graph_"+parameters.critical_type+".csv"
d = pd.read_csv(filename, usecols=['BranchId','LevelIndex','Points_0','Points_1','RegionId','SequenceIndex'])
level = 0

dataframe = pd.DataFrame(d)
dataframe = dataframe[dataframe['LevelIndex'] == level]
dataframe.reset_index(drop=True, inplace=True)
#complete_data = np.array(d)

#level_data = []
#for i in range(len(complete_data)):
#    if complete_data[i][1] == level:
#        level_data.append(complete_data[i])
level_data = np.array(dataframe)

file1 = open("graph_" + parameters.critical_type + ".vtk","w")
file1.write("# vtk DataFile Version 2.0\nvtk output\nASCII\nDATASET POLYDATA\n")
file1.write("POINTS " + str(len(level_data)) + " float" + "\n")
for i in range(len(level_data)):
    file1.write(str(level_data[i][2]) + " " + str(level_data[i][3]) + " " + str(level_data[i][5]) + "\n")

file1.write("LINES " + "\n")
dataframe = pd.DataFrame(d)
max_branch = int(dataframe.max()[0])
count = 0
for branch in range(max_branch+1):
    dataframe = pd.DataFrame(d)
    dataframe = dataframe[dataframe['LevelIndex'] == level]
    dataframe.reset_index(drop=True, inplace=True)
    dataframe = dataframe[dataframe['BranchId'] == branch]
    dataframe = dataframe.sort_values(by = 'SequenceIndex')
    #print(dataframe)
    path = np.array(dataframe.index)
    #print(path)
    if len(path) >= 0:
        for i in range(len(path)-1):
            file1.write("2 " + str(path[i]) + " " + str(path[i+1]) + "\n")
            count = count + 1

print("Add this to the 'Lines' row in the obtained VTK File: ",count)

print("Simplified Jacobi Set Obtained")

