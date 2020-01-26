import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import sympy
from sympy import Line3D, Point3D
import time


#
# Assignment1
#

class Assignment1(ScriptedLoadableModule):
    """Uses ScriptedLoadableModule base class, available at:
    https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = "Assignment1"  # TODO make this more human readable by adding spaces
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
# Assignment1Widget
#

class Assignment1Widget(ScriptedLoadableModuleWidget):
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
        logic = Assignment1Logic()
        logic.run(self.inputSelector.currentNode(), self.outputSelector.currentNode())


#
# Assignment1Logic
#

class Assignment1Logic(ScriptedLoadableModuleLogic):
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
        # bloodVessels = slicer.util.getNode('vesselsTest')
        [x, y, z] = ventricles.GetImageData().GetDimensions()
        # [x, y, z] = bloodVessels.GetImageData().GetDimensions()
        startTime = time.time()
        ventriclesCoordinates = self.getDangerAreaCoordinates(ventricles, x, y, z)
        # bloodVesselCoordinates = self.getDangerAreaCoordinates(bloodVessels, x, y, z)
        # print(len(ventriclesCoordinates))
        endTime = time.time()
        print('Time: ', endTime - startTime, 'seconds')
        ventricleIncisions = self.getIncisions(entryNode, targetsNode, ventriclesCoordinates)
        # bloodVesselIncisions = self.getIncisions(entryNode, targetsNode, bloodVesselCoordinates)
        # overlappingPoints = self.getOverlappingTargetPoints(targetsNode, hippo)
        logging.info('Processing completed')
        return True

    def getDangerAreaCoordinates(self, dangerArea, x, y, z):
        dangerAreaCoordinates = []
        for i in range(0, x):
            for j in range(0, y):
                for k in range(0, z):
                    imageVoxelID = dangerArea.GetImageData().FindPoint(i, j, k)
                    xIndex, yIndex, zIndex = self.convertToIntegerIndices(imageVoxelID, x, y, z)
                    if dangerArea.GetImageData().GetScalarComponentAsDouble(xIndex, yIndex, zIndex, 0) == 1.0:
                        dangerAreaCoordinates.append([xIndex * 4, yIndex * 4, zIndex * 4])
        return dangerAreaCoordinates

    @staticmethod
    def getCoordinates(points, pointIndex):
        world = [0, 0, 0, 0]
        points.GetNthFiducialWorldCoordinates(pointIndex, world)
        return world

    # Task 2 & 3
    def getIncisions(self, entryPoints, targetPoints, ventricles):
        print("entry: ", entryPoints.GetNumberOfMarkups())
        print("target: ", targetPoints.GetNumberOfMarkups())
        incisions = {}
        startTime = time.time()
        for i in range(0, 25):  # entryPoints.GetNumberOfMarkups()):
            entry = self.getCoordinates(entryPoints, i)
            for j in range(0, 25):  # targetPoints.GetNumberOfMarkups()):
                target = self.getCoordinates(targetPoints, j)
                if not self.passThroughVentricles(entry, target, ventricles):
                    key = tuple(entry)
                    if key in incisions:
                        incisions[key].append(target)
                    else:
                        incisions[key] = target
        endTime = time.time()
        print('Entry - Target: ', endTime - startTime, 'seconds')
        return incisions

    @staticmethod
    def passThroughVentricles(entry, target, ventricles):
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
            xDivision = xTarget - xEntry
            yDivision = yTarget - yEntry
            zDivision = zTarget - zEntry
            if xDivision != 0:
                tx = (x - xEntry) / xDivision

            if yDivision != 0:
                ty = (y - yEntry) / yDivision

            if zDivision != 0:
                tz = (z - zEntry) / zDivision

            if xDivision == 0:
                if (ty == tz):
                    if ty > 0 or ty < 1:
                        return True
                    else:
                        continue
                else:
                    continue

            if yDivision == 0:
                if (tx == tz):
                    if tx > 0 or tx < 1:
                        return True
                    else:
                        continue
                else:
                    continue

            if zDivision == 0:
                if (ty == tx):
                    if (ty > 0 or ty < 1):
                        return True
                    else:
                        continue
                else:
                    continue

            if tx == ty and ty == tz:
                if tx > 0 or ty < 1:
                    return True
        return False

    @staticmethod
    def isNotZero(value):
        return value != 0

    # ventriclesTest = slicer.util.getNode('ventriclesTest')
    # ventriclesTest.GetImageData().GetScalarComponentAsDouble(33,40,27,0)
    # for i, entry in enumerate(entryPoints):
    # get coordinates between the two points

    # Task 1
    def targetArea(self, targetPointName, areaName):
        # targetsNode = slicer.util.getNode('targets')
        # hippo = slicer.util.getNode('r_hippoTest_1')
        targetNodes = slicer.util.getNode(targetPointName)
        area = slicer.util.getNode(areaName)
        areaArray = slicer.util.arrayFromVolume(area)

        [xMax, yMax, zMax] = area.GetImageData().GetDimensions()

        goodTarget = []

        for x in range(0, targetNodes.GetNumberOfMarkups()):
            xIndex, yIndex, zIndex = self.getXYZIndices(area, targetNodes, x, xMax, yMax, zMax)
            imageVal = area.GetImageData().GetScalarComponentAsDouble(xIndex, yIndex, zIndex, 0)
            if imageVal != 0:
                goodTarget.append(x)
        print(goodTarget, "LENGTH OF ARRAY =", len(goodTarget))

    def getXYZIndices(self, area, targetNodes, x, xMax, yMax, zMax):
        coordinates = self.getCoordinates(targetNodes, x)
        subsampleFactor = 4
        imageVoxelID = area.GetImageData().FindPoint(coordinates[0] / subsampleFactor, coordinates[1] / subsampleFactor,
                                                     coordinates[2] / subsampleFactor)
        return self.convertToIntegerIndices(imageVoxelID, xMax, yMax, zMax)

    @staticmethod
    def convertToIntegerIndices(imageVoxelID, xMax, yMax, zMax):
        xIndex = int(imageVoxelID % xMax)
        yIndex = int((imageVoxelID / xMax) % yMax)
        zIndex = int((imageVoxelID / (xMax * yMax)) % zMax)
        return xIndex, yIndex, zIndex


class Assignment1Test(ScriptedLoadableModuleTest):

    def setUp(self):
        slicer.mrmlScene.Clear(0)

    def runTest(self):
        self.setUp()
        self.test_Assignment1()

    def test_Assignment1(self):
        self.assertTrue(True)
