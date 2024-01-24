import pandas as pd
import numpy as np
import parameters
dataframe = pd.read_csv("final_con.csv")
dataframe = pd.DataFrame(dataframe)

points = []
lines = []
count = 0
for i in range(int(dataframe.max()['RegionId'])+1):
    temp = dataframe[dataframe['RegionId'] == i]
    temp = temp.sort_values(by=['Points_2'])

    temp = np.array(temp)
    if len(temp)>parameters.length_threshold:
    
        for j in temp:
            points.append([j[1],j[2],j[3]])
        for k in range(len(temp)-1):
            lines.append([count+k,count+k+1])
        count = count + len(temp)


file1 = open("final_check.vtk","w")
file1.write("# vtk DataFile Version 2.0\nvtk output\nASCII\nDATASET POLYDATA\n")
file1.write("POINTS " + str(len(points)) + " float" + "\n")
for i in points:
    file1.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")

file1.write("LINES " + str(len(lines)) + " " + str(3*len(lines)) + "\n")
for i in lines:
    file1.write("2 " + str(i[0]) + " " + str(i[1]) + "\n")
