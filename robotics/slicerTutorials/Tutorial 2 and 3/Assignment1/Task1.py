import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import sympy
from sympy import Line3D, Point3D
import time


#
# Task1
#

class Task1(ScriptedLoadableModule):
    """Uses ScriptedLoadableModule base class, available at:
    https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = "Task1"  # TODO make this more human readable by adding spaces
        self.parent.categories = ["Examples"]
        self.parent.dependencies = []
        self.parent.contributors = ["John Doe (AnyWare Corp.)"]  # replace with "Firstname Lastname (Organization)"
        self.parent.helpText = """
This is an example of scripted loadable module bundled in an extension.
It performs a simple thresholding on the input volume and optionally captures a screenshot.
"""
        self.parent.helpText += self.getDefaultModuleDocumentationLink()
        self.parent.acknowledgementText = """
This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc.
and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.
"""  # replace with organization, grant and thanks.


#
# Task1Widget
#

class Task1Widget(ScriptedLoadableModuleWidget):
    """Uses ScriptedLoadableModuleWidget base class, available at:
    https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def setup(self):
        ScriptedLoadableModuleWidget.setup(self)

        # Instantiate and connect widgets ...

        #
        # Parameters Area
        #
        parametersCollapsibleButton = ctk.ctkCollapsibleButton()
        parametersCollapsibleButton.text = "Parameters"
        self.layout.addWidget(parametersCollapsibleButton)

        # Layout within the dummy collapsible button
        parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)

        #
        # input volume selector
        #
        self.inputSelector = slicer.qMRMLNodeComboBox()
        self.inputSelector.nodeTypes = ["vtkMRMLScalarVolumeNode"]
        self.inputSelector.selectNodeUponCreation = True
        self.inputSelector.addEnabled = False
        self.inputSelector.removeEnabled = False
        self.inputSelector.noneEnabled = False
        self.inputSelector.showHidden = False
        self.inputSelector.showChildNodeTypes = False
        self.inputSelector.setMRMLScene(slicer.mrmlScene)
        self.inputSelector.setToolTip("Pick the input to the algorithm.")
        parametersFormLayout.addRow("Input Volume: ", self.inputSelector)

        #
        # output volume selector
        #
        self.outputSelector = slicer.qMRMLNodeComboBox()
        self.outputSelector.nodeTypes = ["vtkMRMLScalarVolumeNode"]
        self.outputSelector.selectNodeUponCreation = True
        self.outputSelector.addEnabled = True
        self.outputSelector.removeEnabled = True
        self.outputSelector.noneEnabled = True
        self.outputSelector.showHidden = False
        self.outputSelector.showChildNodeTypes = False
        self.outputSelector.setMRMLScene(slicer.mrmlScene)
        self.outputSelector.setToolTip("Pick the output to the algorithm.")
        parametersFormLayout.addRow("Output Volume: ", self.outputSelector)

        #
        # Apply Button
        #
        self.applyButton = qt.QPushButton("Apply")
        self.applyButton.toolTip = "Run the algorithm."
        self.applyButton.enabled = False
        parametersFormLayout.addRow(self.applyButton)

        # connections
        self.applyButton.connect('clicked(bool)', self.onApplyButton)
        self.inputSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onSelect)
        self.outputSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onSelect)

        # Add vertical spacer
        self.layout.addStretch(1)

        # Refresh Apply button state
        self.onSelect()

    def cleanup(self):
        pass

    def onSelect(self):
        self.applyButton.enabled = True
        # self.applyButton.enabled = self.inputSelector.currentNode() and self.outputSelector.currentNode()

    def onApplyButton(self):
        logic = Task1Logic()
        logic.run(self.inputSelector.currentNode(), self.outputSelector.currentNode())


#
# Task1Logic
#

class Task1Logic(ScriptedLoadableModuleLogic):
    """This class should implement all the actual
    computation done by your module.  The interface
    should be such that other python code can import
    this class and make use of the functionality without
    requiring an instance of the Widget.
    Uses ScriptedLoadableModuleLogic base class, available at:
    https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def hasImageData(self, volumeNode):
        """This is an example logic method that
        returns true if the passed in volume
        node has valid image data
        """
        if not volumeNode:
            logging.debug('hasImageData failed: no volume node')
            return False
        if volumeNode.GetImageData() is None:
            logging.debug('hasImageData failed: no image data in volume node')
            return False
        return True

    def isValidInputOutputData(self, inputVolumeNode, outputVolumeNode):
        """Validates if the output is not the same as input
        """
        if not inputVolumeNode:
            logging.debug('isValidInputOutputData failed: no input volume node defined')
            return False
        if not outputVolumeNode:
            logging.debug('isValidInputOutputData failed: no output volume node defined')
            return False
        if inputVolumeNode.GetID() == outputVolumeNode.GetID():
            logging.debug(
                'isValidInputOutputData failed: input and output volume is the same. Create a new volume for output to avoid this error.')
            return False
        return True

    def run(self, inputVolume, outputVolume):
        """
        Run the actual algorithm
        """
        # if not self.isValidInputOutputData(inputVolume, outputVolume):
        #     slicer.util.errorDisplay('Input volume is the same as output volume. Choose a different output volume.')
        #     return False

        logging.info('Processing started')

        targetsNode = slicer.util.getNode('targets')
        entryNode = slicer.util.getNode('entries')
        ventricles = slicer.util.getNode('ventriclesTest')
        [x, y, z] = ventricles.GetImageData().GetDimensions()
        ventriclesCoordinates = []
        startTime = time.time()
        for i in range(0, x):
            for j in range(0, y):
                for k in range(0, z):
                    imageVoxelID = ventricles.GetImageData().FindPoint(i, j, k)
                    xIndex = int(imageVoxelID % x)
                    yIndex = int((imageVoxelID / x) % y)
                    zIndex = int((imageVoxelID / (x * y)) % z)
                    if ventricles.GetImageData().GetScalarComponentAsDouble(xIndex, yIndex, zIndex, 0) == 1.0:
                        ventriclesCoordinates.append([xIndex * 4, yIndex * 4, zIndex * 4])
        # print(len(ventriclesCoordinates))
        endTime = time.time()
        print('Time: ', endTime - startTime, 'seconds')
        self.getIncisions(entryNode, targetsNode, ventriclesCoordinates)
        # overlappingPoints = self.getOverlappingTargetPoints(targetsNode, hippo)
        logging.info('Processing completed')
        return True

    def getCoordinates(self, points, pointIndex):
        world = [0, 0, 0, 0]
        points.GetNthFiducialWorldCoordinates(pointIndex, world)
        return world

    def getIncisions(self, entryPoints, targetPoints, ventricles):
        # directionVectors = targetPoints - entryPoints
        # pointsBetweenThePoints = entryPoints + step * directionVector
        print("entry: ", entryPoints.GetNumberOfMarkups())
        print("target: ", targetPoints.GetNumberOfMarkups())
        incisions = {}
        startTime = time.time()
        for i in range(0, 25):  # entryPoints.GetNumberOfMarkups()):
            entry = self.getCoordinates(entryPoints, i)
            for j in range(0, 25):  # targetPoints.GetNumberOfMarkups()):

                target = self.getCoordinates(targetPoints, j)
                # self.pass
                if not self.passThroughVentricles(entry, target, ventricles):
                    kappa = 1
                    key = tuple(entry)
                    if key in incisions:
                        incisions[key].append(target)
                    else:
                        incisions[key] = target
                    # print(entry,target)
                else:
                    kappa = 2
                #     print(entry, target)
                # x = entryX + step * (targetX - entryX)
                # y = entryY + step * (targetY - entryY)
                # z = entryZ + step * (targetZ - entryZ)
                # lines.append([x,y,z])
        endTime = time.time()
        print('Entry - Target: ', endTime - startTime, 'seconds')

    def passThroughVentricles(self, entry, target, ventricles):
        xEntry, yEntry, zEntry = entry[0], entry[1], entry[2]
        xTarget, yTarget, zTarget = target[0], target[1], target[2]
        size = 10  # en(ventricles)
        # line = Line3D(Point3D(xEntry, yEntry, zEntry), Point3D(xTarget, yTarget, zTarget))
        for i in range(0, size):
            [x, y, z] = ventricles[i]
            # EvaluatePosition(): VTKLine
            # if line.contains(Point3D(x, y, z)):
            #     return True
            # asd = line.contains(Point3D(0, 0, 0))
            if (xTarget - xEntry) != 0:
                tx = (x - xEntry) / (xTarget - xEntry)
                xIsNonZero = True
            else:
                xIsNonZero = False

            if (yTarget - yEntry) != 0:
                ty = (y - yEntry) / (yTarget - yEntry)
                yIsNonZero = True
            else:
                yIsNonZero = False

            if (zTarget - zEntry) != 0:
                tz = (z - zEntry) / (zTarget - zEntry)
                zIsNonZero = True
            else:
                zIsNonZero = False

            if not xIsNonZero:
                if (ty == tz):
                    if (ty > 0 or ty < 1):
                        return True
                    else:
                        continue
                else:
                    continue

            if not yIsNonZero:
                if (tx == tz):
                    if (tx > 0 or tx < 1):
                        return True
                    else:
                        continue
                else:
                    continue

            if not zIsNonZero:
                if (ty == tx):
                    if (ty > 0 or ty < 1):
                        return True
                    else:
                        continue
                else:
                    continue

            if (tx == ty and ty == tz):
                if (tx > 0 or ty < 1):
                    return True
        return False

    # ventriclesTest = slicer.util.getNode('ventriclesTest')
    # ventriclesTest.GetImageData().GetScalarComponentAsDouble(33,40,27,0)
    # for i, entry in enumerate(entryPoints):
    # get coordinates between the two points

    def getOverlappingTargetPoints(self, targetPoints, targetArea):
        [xmax, ymax, zmax] = targetArea.GetImageData().GetDimensions()

        goodTarget = []

        for x in range(0, targetPoints.GetNumberOfMarkups()):
            xIndex, yIndex, zIndex = self.getCoordinates(targetPoints, x)

            imageVal = targetArea.GetImageData().GetScalarComponentAsDouble(xIndex, yIndex, zIndex, 0)

            if imageVal != 0:
                goodTarget.append(x)

        print(goodTarget, 'LENGTH OF ARRAY =', len(goodTarget))
        return goodTarget

    def getXYZIndices(self, points, pointIndex):
        world = [0, 0, 0, 0]
        points.GetNthFiducialWorldCoordinates(pointIndex, world)
        subsampleFactor = 4
        # imageVoxelID = hippo.GetImageData().FindPoint(world[0]/subsampleFactor,world[1]/subsampleFactor,world[2]/subsampleFactor)
        # xIndex = int(imageVoxelID%xmax)
        # yIndex = int((imageVoxelID/xmax)%ymax)
        # zIndex = int((imageVoxelID/(xmax*ymax))%zmax)
        # return xIndex, yIndex, zIndex


class Task1Test(ScriptedLoadableModuleTest):
    """
    This is the test case for your scripted module.
    Uses ScriptedLoadableModuleTest base class, available at:
    https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def setUp(self):
        """ Do whatever is needed to reset the state - typically a scene clear will be enough.
        """
        slicer.mrmlScene.Clear(0)

    def runTest(self):
        """Run as few or as many tests as needed here.
        """
        self.setUp()
        self.test_Task11()

    def test_Task11(self):
        """ Ideally you should have several levels of tests.  At the lowest level
        tests should exercise the functionality of the logic with different inputs
        (both valid and invalid).  At higher levels your tests should emulate the
        way the user would interact with your code and confirm that it still works
        the way you intended.
        One of the most important features of the tests is that it should alert other
        developers when their changes will have an impact on the behavior of your
        module.  For example, if a developer removes a feature that you depend on,
        your test should break so they know that the feature is needed.
        """

        self.delayDisplay("Starting the test")
        #
        # first, get some data
        #
        import SampleData
        SampleData.downloadFromURL(
            nodeNames='FA',
            fileNames='FA.nrrd',
            uris='http://slicer.kitware.com/midas3/download?items=5767')
        self.delayDisplay('Finished with download and loading')

        volumeNode = slicer.util.getNode(pattern="FA")
        logic = Task1Logic()
        self.assertIsNotNone(logic.hasImageData(volumeNode))
        self.delayDisplay('Test passed!')
