import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import sympy
from sympy import Line3D, Point3D
import time
import PointUtils


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

    def hasImageData(self, volumeNode):
        if not volumeNode:
            logging.debug('hasImageData failed: no volume node')
            return False
        if volumeNode.GetImageData() is None:
            logging.debug('hasImageData failed: no image data in volume node')
            return False
        return True

    def isValidInputOutputData(self, inputVolumeNode, outputVolumeNode):
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
        points = PointUtils.getPoints(inputVolume, targetsNode, entryNode)
        # ventriclesCoordinates = self.getDangerAreaCoordinates(ventricles, x, y, z)
        # # bloodVesselCoordinates = self.getDangerAreaCoordinates(bloodVessels, x, y, z)
        # # print(len(ventriclesCoordinates))
        # endTime = time.time()
        # print('Time: ', endTime - startTime, 'seconds')
        # ventricleIncisions = self.getIncisions(entryNode, targetsNode, ventriclesCoordinates)
        # # bloodVesselIncisions = self.getIncisions(entryNode, targetsNode, bloodVesselCoordinates)
        # # overlappingPoints = self.getOverlappingTargetPoints(targetsNode, hippo)
        # logging.info('Processing completed')
        # print(ventricleIncisions)
        return True

class Assignment1Test(ScriptedLoadableModuleTest):

    def setUp(self):
        slicer.mrmlScene.Clear(0)

    def runTest(self):
        self.setUp()
        self.test_Assignment1()

    def test_Assignment1(self):
        self.assertTrue(True)
