# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
import parameters
import os
#### disable automatic camera reset on 'Show'

dir = 'critical_points'
if not os.path.exists(dir):
    os.mkdir(dir)

for t in range(parameters.timesteps):

    print(t)

    # create a new 'Legacy VTK Reader'
    data_0vtk = LegacyVTKReader(registrationName='data_' + str(t) + '.vtk', FileNames=['./simplified_fields_vtk/data_' + str(t) + '.vtk'])

    
    # create a new 'TTK ScalarFieldCriticalPoints'
    tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(registrationName='TTKScalarFieldCriticalPoints1', Input=data_0vtk)
    tTKScalarFieldCriticalPoints1.ScalarField = ['POINTS', 'Result']
    tTKScalarFieldCriticalPoints1.InputOffsetField = ['POINTS', 'Result']

    
    # Create a new 'SpreadSheet View'
    spreadSheetView1 = CreateView('SpreadSheetView')
    spreadSheetView1.ColumnToSort = ''
    spreadSheetView1.BlockSize = 1024

    # show data in view
    tTKScalarFieldCriticalPoints1Display_1 = Show(tTKScalarFieldCriticalPoints1, spreadSheetView1, 'SpreadSheetRepresentation')

    # export view
    ExportView('./critical_points/' + str(t) + '.csv', view=spreadSheetView1)


print("Critical Points Have Been Obtained")