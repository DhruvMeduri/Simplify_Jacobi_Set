import pandas as pd
import numpy as np
import parameters
import os

dir = 'sublevel_sets'
if not os.path.exists(dir):
    os.mkdir(dir)

def decode(str):
    x = int(str[1:1+int(str[0])])
    y = int(str[2+int(str[0]):2+int(str[0]) + int(str[1+int(str[0])])])
    z = int(str[3 + int(str[0]) + int(str[1+int(str[0])]):len(str)])

    return [x,y,z]

for t in range(parameters.timesteps):
#for t in range(40):
    filename = './sublevel_points/subpoints_' + str(t) + '.csv' # <=0.007
    #filename = 'check.csv'
    d = pd.read_csv(filename, usecols=['Points_0','Points_1'])
    dataframe = pd.DataFrame(d)
    point_set = np.array(dataframe)

    #point_set = [[2,3],[3,3]]
    centres = []
    for i in point_set:
        if i[0]-0.5 >= 0 and i[0]-0.5 <= parameters.length - 1 and i[1]-0.5 >= 0 and i[1]-0.5 <= parameters.breadth - 1:
            centres.append([i[0]-0.5,i[1]-0.5])
        if i[0]+0.5 >= 0 and i[0]+0.5 <= parameters.length - 1 and i[1]-0.5 >= 0 and i[1]-0.5 <= parameters.breadth - 1:
            centres.append([i[0]+0.5,i[1]-0.5])
        if i[0]-0.5 >= 0 and i[0]-0.5 <= parameters.length - 1 and i[1]+0.5 >= 0 and i[1]+0.5 <= parameters.breadth - 1:
            centres.append([i[0]-0.5,i[1]+0.5])
        if i[0]+0.5 >= 0 and i[0]+0.5 <= parameters.length - 1 and i[1]+0.5 >= 0 and i[1]+0.5 <= parameters.breadth - 1:
            centres.append([i[0]+0.5,i[1]+0.5])

    centres = np.array(centres)
    centres = np.unique(centres,axis = 0)
    #print(centres)
    points = {}
    connectivity = []
    count = 0

    for i in centres:

        temp1 = str(len(str(int(i[0]-0.5))))+str(int(i[0]-0.5))+str(len(str(int(i[1]-0.5))))+str(int(i[1]-0.5))+'10'
        #print(str(count) + ":", temp1)
        if temp1 not in points:
            points.setdefault(temp1,count)
            count = count + 1

        temp2 = str(len(str(int(i[0]+0.5))))+str(int(i[0]+0.5))+str(len(str(int(i[1]-0.5))))+str(int(i[1]-0.5))+'10'
        #print(str(count) + ":", temp2)
        if temp2 not in points:
            points.setdefault(temp2,count)
            count = count + 1

        temp3 = str(len(str(int(i[0]-0.5))))+str(int(i[0]-0.5))+str(len(str(int(i[1]+0.5))))+str(int(i[1]+0.5))+'10'
        #print(str(count) + ":", temp3)
        if temp3 not in points:
            points.setdefault(temp3,count)
            count = count + 1

        temp4 = str(len(str(int(i[0]+0.5))))+str(int(i[0]+0.5))+str(len(str(int(i[1]+0.5))))+str(int(i[1]+0.5))+'10'
        #print(str(count) + ":", temp4)
        if temp4 not in points:
            points.setdefault(temp4,count)
            count = count + 1

        connectivity.append([points[temp1],points[temp2],points[temp3],points[temp4]])

    #points = np.array(points)
    #print(points)

    file1 = open('sublevel_sets/sublevel_' + str(t) + '.vtk',"w")
    #file1 = open('check.vtk',"w")
    file1.write("# vtk DataFile Version 5.1\nvtk output\nASCII\nDATASET UNSTRUCTURED_GRID\n")
    file1.write("POINTS " + str(len(points)) + " float" + "\n")
    for i in points:
        temp = decode(i)
        file1.write(str(temp[0])+ " " + str(temp[1])+ " " + str(temp[2])+ "\n")

    file1.write("CELLS " + str(len(centres)+1) + " " + str(4*len(centres)) + "\n")
    file1.write("OFFSETS vtktypeint64" + "\n")
    for i in range(len(centres) + 1):
        file1.write(str(4*i) + "\n")

    file1.write("CONNECTIVITY vtktypeint64" + "\n")
    for i in connectivity:
        file1.write(str(i[0]) + " " + str(i[1]) + " " +str(i[2]) + " " +str(i[3]) + "\n")

    file1.write("CELL_TYPES " + str(len(centres)) + "\n")
    for i in range(len(centres)):
        file1.write("8" + "\n")

    print(t)

print("Temperory Sublevel Sets Done")








