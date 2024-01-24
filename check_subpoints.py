# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11
import parameters
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'

for t in range(1480,1500):

    #paraview.simple._DisableFirstRenderCameraReset()

    # create a new 'XML Image Data Reader'
    grad_0vti = XMLImageDataReader(registrationName='grad_0.vti', FileName=['/home/dhruv/Documents/jacobi-sets-of-time-varying-fields/gradient_vti/grad_' + str(t) + '.vti'])
    grad_0vti.PointArrayStatus = ['ImageFile']


    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')



    # create a query selection
    QuerySelect(QueryString='(ImageFile <= ' + str(parameters.delta) + ')', FieldType='POINT', InsideOut=0)

    # create a new 'Extract Selection'
    extractSelection1 = ExtractSelection(registrationName='ExtractSelection1', Input=grad_0vti)

    

    # update the view to ensure updated data information
    #renderView1.Update()


    # set active view
    #SetActiveView(None)

    # Create a new 'SpreadSheet View'
    spreadSheetView1 = CreateView('SpreadSheetView')
    spreadSheetView1.ColumnToSort = ''
    spreadSheetView1.BlockSize = 1024

    # show data in view
    extractSelection1Display_1 = Show(extractSelection1, spreadSheetView1, 'SpreadSheetRepresentation')


    # export view
    ExportView('/home/dhruv/Documents/jacobi-sets-of-time-varying-fields/sublevel_points/subpoints_' + str(t) + '.csv', view=spreadSheetView1)
    print(t)

    