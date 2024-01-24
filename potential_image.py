# state file generated using paraview version 5.11.1
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1451, 784]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [321.75, 39.5, 749.4775946140289]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [354.50975385138713, -1198.916935149685, 3667.1061333854955]
renderView1.CameraFocalPoint = [321.75, 39.50000000000001, 749.4775946140289]
renderView1.CameraViewUp = [0.03791869373359104, 0.9200007750371352, 0.3900778724775461]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 820.3912981014454
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1451, 784)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Legacy VTK Reader'
data_1499vtk = LegacyVTKReader(registrationName='data_1499.vtk', FileNames=['/home/dhruv/Documents/2D Vortex Street/simplified_fields_vtk/data_1499.vtk'])

# create a new 'Legacy VTK Reader'
data_1000vtk = LegacyVTKReader(registrationName='data_1000.vtk', FileNames=['/home/dhruv/Documents/2D Vortex Street/simplified_fields_vtk/data_1000.vtk'])

# create a new 'Legacy VTK Reader'
final_checkvtk = LegacyVTKReader(registrationName='final_check.vtk', FileNames=['/home/dhruv/Documents/2D Vortex Street/final_check.vtk'])

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=final_checkvtk)
tube1.Scalars = ['POINTS', '']
tube1.Vectors = ['POINTS', '1']
tube1.Radius = 3.0

# create a new 'Legacy VTK Reader'
data_500vtk = LegacyVTKReader(registrationName='data_500.vtk', FileNames=['/home/dhruv/Documents/2D Vortex Street/simplified_fields_vtk/data_500.vtk'])

# create a new 'Transform'
transform1 = Transform(registrationName='Transform1', Input=data_500vtk)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Translate = [0.0, 0.0, 500.0]

# create a new 'Legacy VTK Reader'
data_0vtk = LegacyVTKReader(registrationName='data_0.vtk', FileNames=['/home/dhruv/Documents/2D Vortex Street/simplified_fields_vtk/data_0.vtk'])

# create a new 'Transform'
transform3 = Transform(registrationName='Transform3', Input=data_1499vtk)
transform3.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform3.Transform.Translate = [0.0, 0.0, 1499.0]

# create a new 'Transform'
transform2 = Transform(registrationName='Transform2', Input=data_1000vtk)
transform2.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform2.Transform.Translate = [0.0, 0.0, 1000.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tube1
tube1Display = Show(tube1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.SelectTCoordArray = 'None'
tube1Display.SelectNormalArray = 'TubeNormals'
tube1Display.SelectTangentArray = 'None'
tube1Display.OSPRayScaleArray = 'TubeNormals'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'None'
tube1Display.ScaleFactor = 152.42679357528687
tube1Display.SelectScaleArray = 'None'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'None'
tube1Display.GaussianRadius = 7.621339678764343
tube1Display.SetScaleArray = ['POINTS', 'TubeNormals']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'TubeNormals']
tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.PolarAxes = 'PolarAxesRepresentation'
tube1Display.SelectInputVectors = ['POINTS', 'TubeNormals']
tube1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# show data from data_0vtk
data_0vtkDisplay = Show(data_0vtk, renderView1, 'UniformGridRepresentation')

# get 2D transfer function for 'Result'
resultTF2D = GetTransferFunction2D('Result')

# get color transfer function/color map for 'Result'
resultLUT = GetColorTransferFunction('Result')
resultLUT.TransferFunction2D = resultTF2D
resultLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.917915, 0.865003, 0.865003, 0.865003, 1.83583, 0.705882, 0.0156863, 0.14902]
resultLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Result'
resultPWF = GetOpacityTransferFunction('Result')
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.83583, 1.0, 0.5, 0.0]
resultPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
data_0vtkDisplay.Representation = 'Slice'
data_0vtkDisplay.ColorArrayName = ['POINTS', 'Result']
data_0vtkDisplay.LookupTable = resultLUT
data_0vtkDisplay.SelectTCoordArray = 'None'
data_0vtkDisplay.SelectNormalArray = 'None'
data_0vtkDisplay.SelectTangentArray = 'None'
data_0vtkDisplay.OSPRayScaleArray = 'Result'
data_0vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
data_0vtkDisplay.SelectOrientationVectors = 'None'
data_0vtkDisplay.ScaleFactor = 63.900000000000006
data_0vtkDisplay.SelectScaleArray = 'Result'
data_0vtkDisplay.GlyphType = 'Arrow'
data_0vtkDisplay.GlyphTableIndexArray = 'Result'
data_0vtkDisplay.GaussianRadius = 3.1950000000000003
data_0vtkDisplay.SetScaleArray = ['POINTS', 'Result']
data_0vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
data_0vtkDisplay.OpacityArray = ['POINTS', 'Result']
data_0vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
data_0vtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
data_0vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
data_0vtkDisplay.ScalarOpacityUnitDistance = 17.421495333956425
data_0vtkDisplay.ScalarOpacityFunction = resultPWF
data_0vtkDisplay.OpacityArrayName = ['POINTS', 'Result']
data_0vtkDisplay.ColorArray2Name = ['POINTS', 'Result']
data_0vtkDisplay.IsosurfaceValues = [0.917915]
data_0vtkDisplay.SliceFunction = 'Plane'
data_0vtkDisplay.SelectInputVectors = [None, '']
data_0vtkDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
data_0vtkDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.83583, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
data_0vtkDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.83583, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
data_0vtkDisplay.SliceFunction.Origin = [319.5, 39.5, 0.0]

# show data from transform1
transform1Display = Show(transform1, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
transform1Display.Representation = 'Surface'
transform1Display.ColorArrayName = ['POINTS', 'Result']
transform1Display.LookupTable = resultLUT
transform1Display.SelectTCoordArray = 'None'
transform1Display.SelectNormalArray = 'None'
transform1Display.SelectTangentArray = 'None'
transform1Display.OSPRayScaleArray = 'Result'
transform1Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform1Display.SelectOrientationVectors = 'None'
transform1Display.ScaleFactor = 63.900000000000006
transform1Display.SelectScaleArray = 'Result'
transform1Display.GlyphType = 'Arrow'
transform1Display.GlyphTableIndexArray = 'Result'
transform1Display.GaussianRadius = 3.1950000000000003
transform1Display.SetScaleArray = ['POINTS', 'Result']
transform1Display.ScaleTransferFunction = 'PiecewiseFunction'
transform1Display.OpacityArray = ['POINTS', 'Result']
transform1Display.OpacityTransferFunction = 'PiecewiseFunction'
transform1Display.DataAxesGrid = 'GridAxesRepresentation'
transform1Display.PolarAxes = 'PolarAxesRepresentation'
transform1Display.ScalarOpacityFunction = resultPWF
transform1Display.ScalarOpacityUnitDistance = 17.421495333956425
transform1Display.SelectInputVectors = [None, '']
transform1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.57006, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.57006, 1.0, 0.5, 0.0]

# show data from transform2
transform2Display = Show(transform2, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
transform2Display.Representation = 'Surface'
transform2Display.ColorArrayName = ['POINTS', 'Result']
transform2Display.LookupTable = resultLUT
transform2Display.SelectTCoordArray = 'None'
transform2Display.SelectNormalArray = 'None'
transform2Display.SelectTangentArray = 'None'
transform2Display.OSPRayScaleArray = 'Result'
transform2Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform2Display.SelectOrientationVectors = 'None'
transform2Display.ScaleFactor = 63.900000000000006
transform2Display.SelectScaleArray = 'Result'
transform2Display.GlyphType = 'Arrow'
transform2Display.GlyphTableIndexArray = 'Result'
transform2Display.GaussianRadius = 3.1950000000000003
transform2Display.SetScaleArray = ['POINTS', 'Result']
transform2Display.ScaleTransferFunction = 'PiecewiseFunction'
transform2Display.OpacityArray = ['POINTS', 'Result']
transform2Display.OpacityTransferFunction = 'PiecewiseFunction'
transform2Display.DataAxesGrid = 'GridAxesRepresentation'
transform2Display.PolarAxes = 'PolarAxesRepresentation'
transform2Display.ScalarOpacityFunction = resultPWF
transform2Display.ScalarOpacityUnitDistance = 17.421495333956425
transform2Display.SelectInputVectors = [None, '']
transform2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.55683, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.55683, 1.0, 0.5, 0.0]

# show data from transform3
transform3Display = Show(transform3, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
transform3Display.Representation = 'Surface'
transform3Display.ColorArrayName = ['POINTS', 'Result']
transform3Display.LookupTable = resultLUT
transform3Display.SelectTCoordArray = 'None'
transform3Display.SelectNormalArray = 'None'
transform3Display.SelectTangentArray = 'None'
transform3Display.OSPRayScaleArray = 'Result'
transform3Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform3Display.SelectOrientationVectors = 'None'
transform3Display.ScaleFactor = 63.900000000000006
transform3Display.SelectScaleArray = 'Result'
transform3Display.GlyphType = 'Arrow'
transform3Display.GlyphTableIndexArray = 'Result'
transform3Display.GaussianRadius = 3.1950000000000003
transform3Display.SetScaleArray = ['POINTS', 'Result']
transform3Display.ScaleTransferFunction = 'PiecewiseFunction'
transform3Display.OpacityArray = ['POINTS', 'Result']
transform3Display.OpacityTransferFunction = 'PiecewiseFunction'
transform3Display.DataAxesGrid = 'GridAxesRepresentation'
transform3Display.PolarAxes = 'PolarAxesRepresentation'
transform3Display.ScalarOpacityFunction = resultPWF
transform3Display.ScalarOpacityUnitDistance = 17.421495333956425
transform3Display.SelectInputVectors = [None, '']
transform3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.49761, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.49761, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for resultLUT in view renderView1
resultLUTColorBar = GetScalarBar(resultLUT, renderView1)
resultLUTColorBar.Title = 'Result'
resultLUTColorBar.ComponentTitle = ''

# set color bar visibility
resultLUTColorBar.Visibility = 1

# show color legend
data_0vtkDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
transform1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
transform2Display.SetScalarBarVisibility(renderView1, True)

# show color legend
transform3Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(data_1499vtk)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')