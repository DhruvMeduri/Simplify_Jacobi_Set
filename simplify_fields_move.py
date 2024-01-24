# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
import parameters
import os

dir = 'simplified_fields_move'
if not os.path.exists(dir):
    os.mkdir(dir)

for t in range(parameters.timesteps):

    # create a new 'Legacy VTK Reader'
    data_0vtk = LegacyVTKReader(registrationName='data_0.vtk', FileNames=['/home/legend/Documents/data/Bounisq/simplified_fields_vtk/data_' + str(t) + '.vtk'])

    # create a new 'Transform'
    transform1 = Transform(registrationName='Transform1', Input=data_0vtk)
    transform1.Transform = 'Transform'

    # Properties modified on transform1.Transform
    transform1.Transform.Translate = [0.0, 0.0, t]


    # save data
    SaveData('./simplified_fields_move/data_' + str(t) + '.vtk', proxy=transform1, PointDataArrays=['Result', 'Result_Order'],
        FileType='Ascii')

    print(t)
