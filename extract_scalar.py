# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
import parameters
import os
#### disable automatic camera reset on 'Show'

dir = 'fields_csv'
if not os.path.exists(dir):
    os.mkdir(dir)

paraview.simple._DisableFirstRenderCameraReset()
for t in range(parameters.timesteps):
    print(t)
    # create a new 'XML Image Data Reader'
    magnitudevti = XMLImageDataReader(registrationName='magnitude.vti', FileName=['./magnitude.vti'])
    magnitudevti.PointArrayStatus = ['Result']

    # Properties modified on magnitudevti
    magnitudevti.TimeArray = 'None'

    
    # create a new 'Extract Subset'
    extractSubset1 = ExtractSubset(registrationName='ExtractSubset1', Input=magnitudevti)
    extractSubset1.VOI = [0, parameters.length - 1, 0, parameters.breadth - 1, 0, parameters.timesteps]

    # Properties modified on extractSubset1
    extractSubset1.VOI = [0, parameters.length - 1, 0, parameters.breadth - 1, t, t]

    
    # Create a new 'SpreadSheet View'
    spreadSheetView1 = CreateView('SpreadSheetView')
    spreadSheetView1.ColumnToSort = ''
    spreadSheetView1.BlockSize = 1024

    # show data in view
    extractSubset1Display_1 = Show(extractSubset1, spreadSheetView1, 'SpreadSheetRepresentation')


    # export view
    ExportView('./fields_csv/' + str(t) + '.csv', view=spreadSheetView1)

print("Extracting Fields Done")
