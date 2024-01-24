import pandas
import numpy as np
import parameters
#grad_3D = np.zeros((600,600,119))

for t in range(parameters.timesteps):

    print(t)
    csvFile = pandas.read_csv('critical_points/' + str(t) + '.csv',usecols=['Points_0','Points_1'])
    cp = np.array(csvFile) 

    input_file = 'gradients/grad_' + str(t) + '.raw'
    npimg = np.fromfile(input_file, dtype='<f8')
    imageSize = (parameters.breadth, parameters.length)
    npimg = npimg.reshape(imageSize)
    for i in cp:
        npimg[i[1]][i[0]] = 0

    npimg.astype('double').tofile('gradients/grad_' + str(t) + '.raw')# Make this .vti/.vtk later for convenence


print("Final Gradient Fields Obtained")

