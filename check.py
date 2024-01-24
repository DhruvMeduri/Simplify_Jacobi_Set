# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Image Data Reader'
magnitudevti = XMLImageDataReader(registrationName='magnitude.vti', FileName=['/home/dhruv/Documents/jacobi-sets-of-time-varying-fields/magnitude.vti'])
magnitudevti.PointArrayStatus = ['Result']

# Properties modified on magnitudevti
magnitudevti.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
magnitudevtiDisplay = Show(magnitudevti, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
magnitudevtiDisplay.Representation = 'Outline'
magnitudevtiDisplay.ColorArrayName = ['POINTS', '']
magnitudevtiDisplay.SelectTCoordArray = 'None'
magnitudevtiDisplay.SelectNormalArray = 'None'
magnitudevtiDisplay.SelectTangentArray = 'None'
magnitudevtiDisplay.OSPRayScaleArray = 'Result'
magnitudevtiDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
magnitudevtiDisplay.SelectOrientationVectors = 'None'
magnitudevtiDisplay.ScaleFactor = 1.5
magnitudevtiDisplay.SelectScaleArray = 'Result'
magnitudevtiDisplay.GlyphType = 'Arrow'
magnitudevtiDisplay.GlyphTableIndexArray = 'Result'
magnitudevtiDisplay.GaussianRadius = 0.075
magnitudevtiDisplay.SetScaleArray = ['POINTS', 'Result']
magnitudevtiDisplay.ScaleTransferFunction = 'PiecewiseFunction'
magnitudevtiDisplay.OpacityArray = ['POINTS', 'Result']
magnitudevtiDisplay.OpacityTransferFunction = 'PiecewiseFunction'
magnitudevtiDisplay.DataAxesGrid = 'GridAxesRepresentation'
magnitudevtiDisplay.PolarAxes = 'PolarAxesRepresentation'
magnitudevtiDisplay.ScalarOpacityUnitDistance = 0.04025247566406486
magnitudevtiDisplay.OpacityArrayName = ['POINTS', 'Result']
magnitudevtiDisplay.ColorArray2Name = ['POINTS', 'Result']
magnitudevtiDisplay.IsosurfaceValues = [0.917913474211245]
magnitudevtiDisplay.SliceFunction = 'Plane'
magnitudevtiDisplay.Slice = 750
magnitudevtiDisplay.SelectInputVectors = [None, '']
magnitudevtiDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
magnitudevtiDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.83582694842249, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
magnitudevtiDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.83582694842249, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
magnitudevtiDisplay.SliceFunction.Origin = [3.4999999998925, -4.0000225354219765e-12, 7.5]

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# change representation type
magnitudevtiDisplay.SetRepresentationType('Surface')

# set scalar coloring
ColorBy(magnitudevtiDisplay, ('POINTS', 'Result'))

# rescale color and/or opacity maps used to include current data range
magnitudevtiDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
magnitudevtiDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Result'
resultLUT = GetColorTransferFunction('Result')

# get opacity transfer function/opacity map for 'Result'
resultPWF = GetOpacityTransferFunction('Result')

# get 2D transfer function for 'Result'
resultTF2D = GetTransferFunction2D('Result')

# create a new 'Extract Subset'
extractSubset1 = ExtractSubset(registrationName='ExtractSubset1', Input=magnitudevti)
extractSubset1.VOI = [0, 639, 0, 79, 0, 1500]

# Properties modified on extractSubset1
extractSubset1.VOI = [0, 639, 0, 79, 0, 1]

# show data in view
extractSubset1Display = Show(extractSubset1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
extractSubset1Display.Representation = 'Outline'
extractSubset1Display.ColorArrayName = ['POINTS', 'Result']
extractSubset1Display.LookupTable = resultLUT
extractSubset1Display.SelectTCoordArray = 'None'
extractSubset1Display.SelectNormalArray = 'None'
extractSubset1Display.SelectTangentArray = 'None'
extractSubset1Display.OSPRayScaleArray = 'Result'
extractSubset1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSubset1Display.SelectOrientationVectors = 'None'
extractSubset1Display.ScaleFactor = 0.7999999999785001
extractSubset1Display.SelectScaleArray = 'Result'
extractSubset1Display.GlyphType = 'Arrow'
extractSubset1Display.GlyphTableIndexArray = 'Result'
extractSubset1Display.GaussianRadius = 0.039999999998925
extractSubset1Display.SetScaleArray = ['POINTS', 'Result']
extractSubset1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSubset1Display.OpacityArray = ['POINTS', 'Result']
extractSubset1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSubset1Display.DataAxesGrid = 'GridAxesRepresentation'
extractSubset1Display.PolarAxes = 'PolarAxesRepresentation'
extractSubset1Display.ScalarOpacityUnitDistance = 0.21814622195447353
extractSubset1Display.ScalarOpacityFunction = resultPWF
extractSubset1Display.TransferFunction2D = resultTF2D
extractSubset1Display.OpacityArrayName = ['POINTS', 'Result']
extractSubset1Display.ColorArray2Name = ['POINTS', 'Result']
extractSubset1Display.IsosurfaceValues = [0.917913474211245]
extractSubset1Display.SliceFunction = 'Plane'
extractSubset1Display.SelectInputVectors = [None, '']
extractSubset1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSubset1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.83582694842249, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSubset1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.83582694842249, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
extractSubset1Display.SliceFunction.Origin = [3.4999999998925, -4.0000225354219765e-12, 0.005]

# show color bar/color legend
extractSubset1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(magnitudevti, renderView1)

# change representation type
extractSubset1Display.SetRepresentationType('Surface')

# save data
SaveData('/home/dhruv/Documents/jacobi-sets-of-time-varying-fields/test.vtk', proxy=extractSubset1, PointDataArrays=['Result'],
    FileType='Ascii')

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1538, 784)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [3.5, 0.0, 7.910307310990646]
renderView1.CameraFocalPoint = [3.5, 0.0, 7.5]
renderView1.CameraParallelScale = 8.514693182963201

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).