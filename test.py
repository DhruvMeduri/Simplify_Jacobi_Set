# state file generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
import parameters
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


# create a new 'TTK CinemaReader'
rotationcdb = TTKCinemaReader(registrationName='rotation.cdb', DatabasePath='./rotation.cdb')

# create a new 'TTK CinemaQuery'
ttkCinemaQuery1 = TTKCinemaQuery(registrationName='TTKCinemaQuery1', InputTable=rotationcdb)
ttkCinemaQuery1.SQLStatement = """SELECT * FROM InputTable0
ORDER BY Time
LIMIT """ + str(parameters.timesteps) + """ OFFSET 0"""

# create a new 'TTK ForEach'
ttkForEach1 = TTKForEach(registrationName='TTKForEach1', Input=ttkCinemaQuery1)

# create a new 'TTK CinemaProductReader'
ttkCinemaProductReader1 = TTKCinemaProductReader(registrationName='TTKCinemaProductReader1', Input=ttkForEach1)

# create a new 'Merge Blocks'
mergeBlocks1 = MergeBlocks(registrationName='MergeBlocks1', Input=ttkCinemaProductReader1)

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=mergeBlocks1)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Value = 0

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [31.5, 31.5, 50.0]
clip1.ClipType.Normal = [0.0, 0.0, 1.0]


# create a new 'Connectivity'
connectivity2 = Connectivity(registrationName='Connectivity2', Input=clip1)

# create a new 'TTK BlockAggregator'
ttkBlockAggregator1 = TTKBlockAggregator(registrationName='TTKBlockAggregator6', Input=connectivity2)
ttkBlockAggregator1.ForceReset = 1

# create a new 'TTK ArrayEditor'
ttkArrayEditor1 = TTKArrayEditor(registrationName='TTKArrayEditor1', Target=ttkBlockAggregator1,
    Source=ttkCinemaProductReader1)
ttkArrayEditor1.EditorMode = 'Add Arrays from Source'
ttkArrayEditor1.TargetAttributeType = 'Field Data'
ttkArrayEditor1.SourceFieldDataArrays = ['_ttk_IterationInfo']

# create a new 'TTK TrackingFromOverlap'
ttkTrackingFromOverlap1 = TTKTrackingFromOverlap(registrationName='TTKTrackingFromOverlap1', Input=ttkArrayEditor1)
ttkTrackingFromOverlap1.Labels = 'NONE'
ttkTrackingFromOverlap1.Labels = 'RegionId'
# create a new 'TTK EndFor'
ttkEndFor1 = TTKEndFor(registrationName='TTKEndFor1', Data=ttkTrackingFromOverlap1,
    For=ttkForEach1)

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=ttkEndFor1)
calculator1.ResultArrayName = 'Size'
calculator1.Function = 'Size/10000'
calculator1.ResultArrayType = 'Float'

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
calculator1Display = Show(calculator1, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('./tracking_graph_' + parameters.critical_type + '.csv', view=spreadSheetView1)

print("Tracking Graph Computed")


