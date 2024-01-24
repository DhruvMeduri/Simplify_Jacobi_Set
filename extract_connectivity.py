# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
import parameters
import os

dir = 'connectivity_sublevel_sets'
if not os.path.exists(dir):
    os.mkdir(dir)

for t in range(parameters.timesteps):
#for t in range(40):
        
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()
    print(t)
    # create a new 'Legacy VTK Reader'
    sublevel_0vtk = LegacyVTKReader(registrationName='sublevel_' +str(t)+'.vtk', FileNames=['./sublevel_sets/sublevel_' + str(t) + '.vtk'])

    
    # create a new 'Connectivity'
    connectivity1 = Connectivity(registrationName='Connectivity1', Input=sublevel_0vtk)

    
    # Create a new 'SpreadSheet View'
    spreadSheetView1 = CreateView('SpreadSheetView')
    spreadSheetView1.ColumnToSort = ''
    spreadSheetView1.BlockSize = 1024

    # show data in view
    connectivity1Display_1 = Show(connectivity1, spreadSheetView1, 'SpreadSheetRepresentation')


    # export view
    ExportView('./connectivity_sublevel_sets/con_' + str(t) + '.csv', view=spreadSheetView1)

print("Connectivity Computed")
