# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
import parameters
import os
#### disable automatic camera reset on 'Show'

dir = 'gradient_vti'
if not os.path.exists(dir):
    os.mkdir(dir)

for t in range(int(parameters.timesteps/2)):
    
    print(t)
    # create a new 'Image Reader'
    grad_0raw = ImageReader(registrationName='grad_' + str(t) + '.raw', FileNames=['./gradients/grad_' + str(t) + '.raw'])

    # Properties modified on grad_0raw
    grad_0raw.DataScalarType = 'double'
    grad_0raw.DataByteOrder = 'LittleEndian'
    grad_0raw.DataExtent = [0, parameters.length - 1, 0, parameters.breadth - 1, 0, 0]

    
    # save data
    SaveData('./gradient_vti/grad_' + str(t) + '.vti', proxy=grad_0raw, PointDataArrays=['ImageFile'])

print("VTI gradient fields")
    