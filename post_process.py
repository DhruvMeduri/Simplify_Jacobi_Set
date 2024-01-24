import pandas as pd
import numpy as np

dataframe = pd.read_csv("graph_max_con.csv")
dataframe = pd.DataFrame(dataframe)
#temp = dataframe[dataframe['RegionId'] == 31]
#temp=temp.query('Points_2 == Points_2.max()')
#print(temp)
start = []
end = []
temp_start = []
temp_end = []
for i in range(int(dataframe.max()['RegionId'])+1):
    temp = dataframe[dataframe['RegionId'] == i]
    temp=temp.query('Points_2 == Points_2.max()')
    temp = np.array(temp)[0]
    end.append(temp)

    temp = dataframe[dataframe['RegionId'] == i]
    temp=temp.query('Points_2 == Points_2.min()')
    temp = np.array(temp)[0]
    start.append(temp)
#print('START: ',start)
#print('END: ',end)
temp_start = start
temp_end = end
print(start[1])
#For debug
#The parameters

alpha = 100
t = 20

#For computing the start to end connnections
start_end = []
starts_removed = []

for i in range(len(temp_start)):
    flag = 0
    add = 0
    min = 100000
    for j in  range(len(temp_end)):
        if temp_start[i][3] - temp_end[j][3] <= t and temp_start[i][3] - temp_end[j][3] > 0 and (temp_start[i][1] - temp_end[j][1])**2 + (temp_start[i][2] - temp_end[j][2])**2 < alpha and temp_end[j][5] != temp_start[i][5]:
            if temp_start[i][3] - temp_end[j][3] < min:
                add = j
                min = temp_start[i][3] - temp_end[j][3]
                flag = 1
    
    if flag == 1:
    
        start_end.append([temp_start[i][5],temp_end[add][5]])
        starts_removed.append(int(temp_start[i][5]))
        temp = []
        for k in range(len(temp_end)):
            if k !=add :
                temp.append(temp_end[k])
        temp_end = temp



print(start_end)

temp= []
for i in temp_start:
    if int(i[5]) not in starts_removed:
        temp.append(i)

temp_start = temp

#For computing end_start connections
end_start = []
#print(end)
#print(start)
for i in range(len(temp_end)):
    flag = 0
    add = 0
    min = 10000000
    for j in  range(len(temp_start)):
        if temp_end[i][3] - temp_start[j][3] <= t and temp_end[i][3] - temp_start[j][3] >= 0 and (temp_end[i][1] - temp_start[j][1])**2 + (temp_end[i][2] - temp_start[j][2])**2 < alpha and temp_end[i][5] != temp_start[j][5] and temp_end[i][3] < end[int(temp_start[j][5])][3]:
            if temp_end[i][3] - temp_start[j][3] < min:
                add = j
                min = temp_end[i][3] - temp_start[j][3]
                flag = 1
                
            
    if flag == 1:
        print([temp_end[i][5],temp_start[add][5]])
        print([temp_end[i][3],temp_end[add][3]])
        print(add)
        end_start.append([temp_end[i][5],temp_start[add][5]])
        temp= []
        for k in range(len(temp_start)):
            if k !=add :
                temp.append(temp_start[k])
        temp_start = temp
        


print("IMPORTANT: ",end_start)

points = []
lines = []
count = 0
for i in range(int(dataframe.max()['RegionId'])+1):
    temp = dataframe[dataframe['RegionId'] == i]
    cut_start = temp['Points_2'].min()
    temp = temp.sort_values(by=['Points_2'])
    # Main change
    for con in end_start:
        if i == int(con[1]):
            cut_end = dataframe[dataframe['RegionId'] == con[0]]
            cut_end = cut_end['Points_2'].max()
            temp = temp.iloc[int(cut_end - cut_start + 1):]
    temp = np.array(temp)
    for j in temp:
        points.append([j[1],j[2],j[3]])
    for k in range(len(temp)-1):
        lines.append([count+k,count+k+1])
    count = count + len(temp)
#print(cut_start)
#print(cut_end)

for i in start_end:
    temp1 = dataframe[dataframe['RegionId'] == i[0]]
    temp1=temp1.query('Points_2 == Points_2.min()')
    temp1 = np.array(temp1)[0]

    temp2 = dataframe[dataframe['RegionId'] == i[1]]
    temp2=temp2.query('Points_2 == Points_2.max()')
    temp2 = np.array(temp2)[0]

    temp_line  = []

    for j in range(len(points)):
        if points[j][0] == temp1[1] and points[j][1] == temp1[2] and points[j][2] == temp1[3]:
            temp_line.append(j)
        
        if points[j][0] == temp2[1] and points[j][1] == temp2[2] and points[j][2] == temp2[3]:
            temp_line.append(j)

    lines.append(temp_line)

for i in end_start:
    temp1 = dataframe[dataframe['RegionId'] == i[0]]
    cut_end = temp1['Points_2'].max()
    temp1=temp1.query('Points_2 == Points_2.max()')
    temp1 = np.array(temp1)[0]

    temp2 = dataframe[dataframe['RegionId'] == i[1]]
    #temp2=temp2.query('Points_2 == Points_2.min()')
    cut_start = temp2['Points_2'].min()
    temp2 = temp2.sort_values(by=['Points_2'])
    temp2 = temp2.iloc[cut_end - cut_start + 1:]
    temp2=temp2.query('Points_2 == Points_2.min()')   
    #temp2 = temp2[cut_end - cut_start + 1]
    temp2 = np.array(temp2)[0]
    print(temp2)
    temp_line  = []
    for j in range(len(points)):
        if points[j][0] == temp1[1] and points[j][1] == temp1[2] and points[j][2] == temp1[3]:
            temp_line.append(j)
        
        if points[j][0] == temp2[1] and points[j][1] == temp2[2] and points[j][2] == temp2[3]:
            temp_line.append(j)
    print(len(temp_line))

    lines.append(temp_line)



file1 = open("final.vtk","w")
file1.write("# vtk DataFile Version 2.0\nvtk output\nASCII\nDATASET POLYDATA\n")
file1.write("POINTS " + str(len(points)) + " float" + "\n")
for i in points:
    file1.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")

file1.write("LINES " + str(len(lines)) + " " + str(3*len(lines)) + "\n")
for i in lines:
    file1.write("2 " + str(i[0]) + " " + str(i[1]) + "\n")

#Debug

