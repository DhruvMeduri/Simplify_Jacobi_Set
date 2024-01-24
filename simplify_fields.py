# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
import parameters
import os

#### disable automatic camera reset on 'Show'

for t in range(parameters.timesteps):

    print(t)

    # create a new 'Legacy VTK Reader'
    data_0vtk = LegacyVTKReader(registrationName='data_' + str(t) + '.vtk', FileNames=['./simplified_fields_vtk/data_' + str(t) + '.vtk'])
 
    # create a new 'TTK TopologicalSimplificationByPersistence'
    TTKopologicalSimplificationByPersistence1 = TTKTopologicalSimplificationByPersistence(registrationName='TTKTopologicalSimplificationByPersistence1', Input=data_0vtk)
    TTKopologicalSimplificationByPersistence1.InputArray = ['POINTS', 'Result']

    # Properties modified on tTKTopologicalSimplificationByPersistence1
    TTKopologicalSimplificationByPersistence1.PersistenceThreshold = parameters.persistence

    
    # save data
    SaveData('./simplified_fields_vtk/data_' + str(t) + '.vtk', proxy=TTKopologicalSimplificationByPersistence1, PointDataArrays=['Result', 'Result_Order'],
        FileType='Ascii')
    
    #print(t)

print("Fields Have Been Simplified")

    