import numpy as np
import vtk
import parameters
import os

dir = 'gradients'
if not os.path.exists(dir):
    os.mkdir(dir)

for t in range(parameters.timesteps):
    print(t)
    file = 'simplified_fields_vtk/data_' + str(t) + '.vtk'
    #mesh = meshio.read(file)
    reader = vtk.vtkStructuredPointsReader()
    reader.SetFileName(file)
    reader.ReadAllScalarsOn()
    reader.Update()

    points = reader.GetOutput()
    #u = VN.vtk_to_numpy(points.GetCellData().GetArray('velocity'))
    data = points.GetPointData().GetArray('Result')
    data = np.array(data)
    data = np.reshape(data,(parameters.breadth,parameters.length))
    #print(data[0][25])
    #data.astype('double').tofile('grad.raw')# Make this .vti/.vtk later for convenence

    #Now to compute the gradient magnitude field
    grad = np.zeros((parameters.breadth,parameters.length,2))
    for i in range(parameters.breadth):
        for j in range(parameters.length):
            if i == parameters.breadth - 1 and j!=0 and j!=parameters.length - 1:
                grad[i][j][0] = data[i][j] - data[i-1][j]
                grad[i][j][1] = 0.5*(data[i][j+1] - data[i][j-1])

            elif i == 0 and j!=0 and j!=parameters.length - 1:
                grad[i][j][0] = -data[i][j] + data[i+1][j]
                grad[i][j][1] = 0.5*(data[i][j+1] - data[i][j-1])

            elif j == parameters.length - 1 and i!=0 and i!=parameters.breadth - 1:
                grad[i][j][1] = -data[i][j] + data[i][j-1]
                grad[i][j][0] = 0.5*(data[i+1][j] - data[i-1][j])
            
            elif j == 0 and i!=0 and i!=parameters.breadth - 1:
                grad[i][j][1] = -data[i][j] + data[i][j+1]
                grad[i][j][0] = 0.5*(data[i+1][j] - data[i-1][j])
                
            elif i == parameters.breadth - 1 and j==parameters.length - 1:
                grad[i][j][0] = data[i][j] - data[i-1][j]
                grad[i][j][1] = data[i][j] - data[i][j-1]
            
            elif i == parameters.breadth - 1 and j==0:
                grad[i][j][0] = data[i][j] - data[i-1][j]
                grad[i][j][1] = data[i][j+1] - data[i][j]
            
            elif i == 0 and j==parameters.length - 1:
                grad[i][j][0] = data[i+1][j] - data[i][j]
                grad[i][j][1] = data[i][j] - data[i][j-1]
            
            elif i == 0 and j == 0:
                grad[i][j][0] = data[i+1][j] - data[i][j]
                grad[i][j][1] = data[i][j+1] - data[i][j]

            else:
                grad[i][j][0] = 0.5*(data[i+1][j] - data[i-1][j])
                grad[i][j][1] = 0.5*(data[i][j+1] - data[i][j-1])
            
    #data.astype('double').tofile('dummy.raw')
    grad_mag = np.zeros((parameters.breadth,parameters.length))
    for i in range(parameters.breadth):
        for j in range(parameters.length):
            if grad[i][j][0]!=0:
                grad_mag[i][j] = ((grad[i][j][0])**(2) + (grad[i][j][1])**(2))**(0.5) 

    #grad_mag.astype('double').tofile('gradient_raw/grad_' + str(t) + '.raw')# Make this .vti/.vtk later for convenence
    grad_mag.astype('double').tofile('gradients/grad_' + str(t) + '.raw')# Make this .vti/.vtk later for convenence

print("Initial Gradient Fields Computed")
