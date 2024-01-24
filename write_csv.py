import csv 
import parameters
# field names 
fields = ['Time', 'FILE'] 
    
# data rows of csv file 
rows = []

for i in range(parameters.timesteps):
#for i in range(40):
    str1 = str(i)
    str2 = 'final_sublevel_sets_'+parameters.critical_type+'/sublevel_' + str(i) + '.vtk'
    rows.append([str1,str2])
    
# name of csv file 
filename = "./rotation.cdb/data.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)

print("CSV Done")
