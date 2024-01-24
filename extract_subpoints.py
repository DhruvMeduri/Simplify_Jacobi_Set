# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
import parameters
import os
#### disable automatic camera reset on 'Show'

dir = 'sublevel_points'
if not os.path.exists(dir):
    os.mkdir(dir)

for t in range(parameters.timesteps):

    print(t)
    paraview.simple._DisableFirstRenderCameraReset()

    # create a new 'XML Image Data Reader'
    grad_0vti = XMLImageDataReader(registrationName='grad_' + str(t) + '.vti', FileName=['./gradient_vti/grad_' + str(t) + '.vti'])
    grad_0vti.PointArrayStatus = ['ImageFile']

    
    # create a query selection
    QuerySelect(QueryString='(ImageFile <= ' + str(parameters.delta) + ')', FieldType='POINT', InsideOut=0)


    # create a new 'Extract Selection'
    extractSelection1 = ExtractSelection(registrationName='ExtractSelection1', Input=grad_0vti)


    # Create a new 'SpreadSheet View'
    spreadSheetView1 = CreateView('SpreadSheetView')
    spreadSheetView1.ColumnToSort = ''
    spreadSheetView1.BlockSize = 1024

    # show data in view
    extractSelection1Display_1 = Show(extractSelection1, spreadSheetView1, 'SpreadSheetRepresentation')

    # export view
    ExportView('./sublevel_points/subpoints_' + str(t) + '.csv', view=spreadSheetView1)

print("Subpoints extracted")
