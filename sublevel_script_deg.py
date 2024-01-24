import pandas as pd
import numpy as np
import parameters
import os

dir = 'rotation.cdb'
if not os.path.exists(dir):
    os.mkdir(dir)

dir = 'final_sublevel_sets_move_' + parameters.critical_type
if not os.path.exists(dir):
    os.mkdir(dir)

dir = './rotation.cdb/final_sublevel_sets_' + parameters.critical_type
if not os.path.exists(dir):
    os.mkdir(dir)

def decode(str):
    x = int(str[1:1+int(str[0])])
    y = int(str[2+int(str[0]):2+int(str[0]) + int(str[1+int(str[0])])])
    z = int(str[3 + int(str[0]) + int(str[1+int(str[0])]):len(str)])

    return [x,y,z]


for t in range(parameters.timesteps):

#for t in range(40):


    connectivity = './connectivity_sublevel_sets/con_' + str(t) + '.csv'
    d1 = pd.read_csv(connectivity, usecols=['Points_0','Points_1','RegionId'])
    m = max(d1['RegionId'])+1
    d1 = np.array(d1)
    deg1 = np.zeros(m)
    deg2 = np.zeros(m)
    critical = './critical_points/' + str(t) + '.csv'
    d2 = pd.read_csv(critical, usecols=['Points_0','Points_1','CriticalType'])
    d2 = np.array(d2)
    rem_regions = []

    if parameters.critical_type == 'MAX':

        for i in d2:
        
            for j in d1:

                if i[1] == j[0] and i[2] == j[1]:

                    if i[0] == 3: # for max only add 3,for min only add 0 for saddle only add 1 or 2  
                        deg1[j[2]] = 1

                    if i[0] == 0 or i[0] == 3:
                        deg2[j[2]] = deg2[j[2]] + 1
                    
                    if i[0] == 1 or i[0] == 2:
                        deg2[j[2]] = deg2[j[2]] - 1


        for i in range(len(deg2)):
            if deg2[i] == 0 or deg1[i] != 1: # for max, min, saddle only add this "or deg1[i] != 1"  
                rem_regions.append(i) 
            

    if parameters.critical_type == 'MIN':
        
        for i in d2:
        
            for j in d1:

                if i[1] == j[0] and i[2] == j[1]:

                    if i[0] == 0: # for max only add 3,for min only add 0 for saddle only add 1 or 2  
                        deg1[j[2]] = 1

                    if i[0] == 0 or i[0] == 3:
                        deg2[j[2]] = deg2[j[2]] + 1
                    
                    if i[0] == 1 or i[0] == 2:
                        deg2[j[2]] = deg2[j[2]] - 1

        for i in range(len(deg2)):
            if deg2[i] == 0 or deg1[i] != 1: # for max, min, saddle only add this "or deg1[i] != 1"  
                rem_regions.append(i) 
            

    if parameters.critical_type == 'ALL':
        
        for i in d2:
        
            for j in d1:

                if i[1] == j[0] and i[2] == j[1]:

                    if i[0] == 0 or i[0] == 3:
                        deg2[j[2]] = deg2[j[2]] + 1
                    
                    if i[0] == 1 or i[0] == 2:
                        deg2[j[2]] = deg2[j[2]] - 1

        for i in range(len(deg2)):
            if deg2[i] == 0: # for max, min, saddle only add this "or deg1[i] != 1"  
                rem_regions.append(i) 
            

    d1 = pd.read_csv(connectivity, usecols=['Points_0','Points_1','RegionId'])
    d1 = d1.loc[d1['RegionId'].isin(rem_regions)]
    d1 = d1[['Points_0','Points_1']]
    #print(d1)


    filename = './sublevel_points/subpoints_' + str(t) + '.csv' # <=0.01
    #filename = 'check.csv'
    d = pd.read_csv(filename, usecols=['Points_0','Points_1'])
    d = pd.concat([d, d1, d1]).drop_duplicates(keep=False) 
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

    file1 = open('./rotation.cdb/final_sublevel_sets_' + parameters.critical_type + '/sublevel_' + str(t) + '.vtk',"w")
    file2 = open('final_sublevel_sets_move_' + parameters.critical_type + '/sublevel_' + str(t) + '.vtk',"w")
    #file1 = open('check.vtk',"w")
    file1.write("# vtk DataFile Version 5.1\nvtk output\nASCII\nDATASET UNSTRUCTURED_GRID\n")
    file1.write("POINTS " + str(len(points)) + " float" + "\n")
    file2.write("# vtk DataFile Version 5.1\nvtk output\nASCII\nDATASET UNSTRUCTURED_GRID\n")
    file2.write("POINTS " + str(len(points)) + " float" + "\n")
    for i in points:
        temp = decode(i)
        file1.write(str(temp[0])+ " " + str(temp[1])+ " " + str(0)+ "\n")
        file2.write(str(temp[0])+ " " + str(temp[1])+ " " + str(t)+ "\n")

    file1.write("CELLS " + str(len(centres)+1) + " " + str(4*len(centres)) + "\n")
    file1.write("OFFSETS vtktypeint64" + "\n")
    file2.write("CELLS " + str(len(centres)+1) + " " + str(4*len(centres)) + "\n")
    file2.write("OFFSETS vtktypeint64" + "\n")
    for i in range(len(centres) + 1):
        file1.write(str(4*i) + "\n")
        file2.write(str(4*i) + "\n")

    file1.write("CONNECTIVITY vtktypeint64" + "\n")
    file2.write("CONNECTIVITY vtktypeint64" + "\n")
    for i in connectivity:
        file1.write(str(i[0]) + " " + str(i[1]) + " " +str(i[2]) + " " +str(i[3]) + "\n")
        file2.write(str(i[0]) + " " + str(i[1]) + " " +str(i[2]) + " " +str(i[3]) + "\n")

    file1.write("CELL_TYPES " + str(len(centres)) + "\n")
    file2.write("CELL_TYPES " + str(len(centres)) + "\n")
    for i in range(len(centres)):
        file1.write("8" + "\n")
        file2.write("8" + "\n")

    print(t)

print("Final Sublevel Sets Done")
