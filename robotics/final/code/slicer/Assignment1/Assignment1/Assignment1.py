import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import PointUtils
import PathPlanner
import GeometryUtils
import time
import numpy as np


#
# Assignment1
#

class Assignment1(ScriptedLoadableModule):

    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = "Assignment 1"
        self.parent.categories = ["Examples"]
        self.parent.dependencies = []
        self.parent.contributors = ["Person McPerson"]
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
        # Input selectors go here
        #
        self.hippocampusSelector = slicer.qMRMLNodeComboBox()
        self.hippocampusSelector.nodeTypes = ["vtkMRMLLabelMapVolumeNode"]
        self.hippocampusSelector.selectNodeUponCreation = True
        self.hippocampusSelector.addEnabled = False
        self.hippocampusSelector.removeEnabled = False
        self.hippocampusSelector.noneEnabled = False
        self.hippocampusSelector.showHidden = False
        self.hippocampusSelector.showChildNodeTypes = False
        self.hippocampusSelector.setMRMLScene(slicer.mrmlScene)
        self.hippocampusSelector.setToolTip("The hippocampus volume")
        parametersFormLayout.addRow("Hippocampus Volume: ", self.hippocampusSelector)

        self.ventricleSelector = slicer.qMRMLNodeComboBox()
        self.ventricleSelector.nodeTypes = ["vtkMRMLLabelMapVolumeNode"]
        self.ventricleSelector.selectNodeUponCreation = True
        self.ventricleSelector.addEnabled = False
        self.ventricleSelector.removeEnabled = False
        self.ventricleSelector.noneEnabled = False
        self.ventricleSelector.showHidden = False
        self.ventricleSelector.showChildNodeTypes = False
        self.ventricleSelector.setMRMLScene(slicer.mrmlScene)
        self.ventricleSelector.setToolTip("The ventricle labels")
        parametersFormLayout.addRow("Ventricles Volume: ", self.ventricleSelector)

        self.bloodVesselSelector = slicer.qMRMLNodeComboBox()
        self.bloodVesselSelector.nodeTypes = ["vtkMRMLLabelMapVolumeNode"]
        self.bloodVesselSelector.selectNodeUponCreation = True
        self.bloodVesselSelector.addEnabled = False
        self.bloodVesselSelector.removeEnabled = False
        self.bloodVesselSelector.noneEnabled = False
        self.bloodVesselSelector.showHidden = False
        self.bloodVesselSelector.showChildNodeTypes = False
        self.bloodVesselSelector.setMRMLScene(slicer.mrmlScene)
        self.bloodVesselSelector.setToolTip("The blood vessel labels")
        parametersFormLayout.addRow("Blood Vessels Volume: ", self.bloodVesselSelector)

        self.cortexSelector = slicer.qMRMLNodeComboBox()
        self.cortexSelector.nodeTypes = ["vtkMRMLLabelMapVolumeNode"]
        self.cortexSelector.selectNodeUponCreation = True
        self.cortexSelector.addEnabled = False
        self.cortexSelector.removeEnabled = False
        self.cortexSelector.noneEnabled = False
        self.cortexSelector.showHidden = False
        self.cortexSelector.showChildNodeTypes = False
        self.cortexSelector.setMRMLScene(slicer.mrmlScene)
        self.cortexSelector.setToolTip("Cortex labels")
        parametersFormLayout.addRow("Cortex Volume: ", self.cortexSelector)

        self.entrySelector = slicer.qMRMLNodeComboBox()
        self.entrySelector.nodeTypes = ["vtkMRMLMarkupsFiducialNode"]
        self.entrySelector.selectNodeUponCreation = True
        self.entrySelector.addEnabled = False
        self.entrySelector.removeEnabled = False
        self.entrySelector.noneEnabled = False
        self.entrySelector.showHidden = False
        self.entrySelector.showChildNodeTypes = False
        self.entrySelector.setMRMLScene(slicer.mrmlScene)
        self.entrySelector.setToolTip("The entry point fiducials")
        parametersFormLayout.addRow("Entry Points: ", self.entrySelector)

        self.targetSelector = slicer.qMRMLNodeComboBox()
        self.targetSelector.nodeTypes = ["vtkMRMLMarkupsFiducialNode"]
        self.targetSelector.selectNodeUponCreation = True
        self.targetSelector.addEnabled = False
        self.targetSelector.removeEnabled = False
        self.targetSelector.noneEnabled = False
        self.targetSelector.showHidden = False
        self.targetSelector.showChildNodeTypes = False
        self.targetSelector.setMRMLScene(slicer.mrmlScene)
        self.targetSelector.setToolTip("The target point fiducials")
        parametersFormLayout.addRow("Target Points: ", self.targetSelector)

        self.angleSlider = ctk.ctkSliderWidget()
        self.angleSlider.singleStep = 1
        self.angleSlider.minimum = 0
        self.angleSlider.maximum = 90
        self.angleSlider.value = 55
        self.angleSlider.setToolTip("The angle value for entering the cortex")
        parametersFormLayout.addRow("Entry/Target angle", self.angleSlider)

        #
        # Apply Button
        #
        self.applyButton = qt.QPushButton("Apply")
        self.applyButton.toolTip = "Run the algorithm."
        self.applyButton.enabled = False
        parametersFormLayout.addRow(self.applyButton)

        # connections
        self.applyButton.connect('clicked(bool)', self.onApplyButton)
        self.entrySelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onSelect)
        self.targetSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onSelect)

        # Add vertical spacer
        self.layout.addStretch(1)

        # Refresh Apply button state
        self.onSelect()

    def cleanup(self):
        pass

    def onSelect(self):
        self.applyButton.enabled = self.hippocampusSelector.currentNode() and self.ventricleSelector.currentNode() and self.bloodVesselSelector.currentNode() and self.cortexSelector.currentNode() and self.entrySelector.currentNode() and self.targetSelector.currentNode()

    def onApplyButton(self):
        logic = Assignment1Logic()
        logic.run(self.hippocampusSelector.currentNode(),
                  self.ventricleSelector.currentNode(),
                  self.bloodVesselSelector.currentNode(),
                  self.cortexSelector.currentNode(),
                  self.entrySelector.currentNode(),
                  self.targetSelector.currentNode(),
                  self.angleSlider.value)


#
# Assignment1Logic
#

class Assignment1Logic(ScriptedLoadableModuleLogic):

    def isValidInputOutputData(self, hippocampus, ventricles, bloodVessels, cortex, entries, targets, angle):
        """Validates if the output is not the same as input
        """
        if not hippocampus:
            logging.debug('No hippocampus data selected')
            return False
        if not ventricles:
            logging.debug('No ventricle data selected')
            return False
        if not bloodVessels:
            logging.debug('No blood vessel data selected')
            return False
        if not cortex:
            logging.debug('No cortex data selected')
            return False
        if not entries:
            logging.debug('No entry point data selected')
            return False
        if not targets:
            logging.debug('No target point data selected')
            return False
        if not angle:
            logging.debug('No valid angle selected')
            return False
        return True

    def run(self, hippocampus, ventricles, bloodVessels, cortex, entries, targets, angle):
        """
        Run the actual algorithm
        """
        if not self.isValidInputOutputData(hippocampus, ventricles, bloodVessels, cortex, entries, targets,
                                           angle):
            slicer.util.errorDisplay('Invalid input.')
            return False

        logging.info('Processing started')

        # uncomment to see one-by-one
        # startTime = time.time()
        # PointUtils.getFilteredTargets(targets, hippocampus)
        # endTime = time.time()
        # print('Filtered targets time: ', endTime - startTime, 'seconds')
        #
        # entriesAndTargets = PointUtils.getTrajectoryDictionary(entries,
        #                                                        PointUtils.convertMarkupNodeToPoints(targets))
        #
        # startTime = time.time()
        # PathPlanner.getTrajectoriesAvoidingArea(entriesAndTargets, ventricles)
        # endTime = time.time()
        # print('Avoid area - Ventricles: ', endTime - startTime, 'seconds')
        #
        # startTime = time.time()
        # PathPlanner.getTrajectoriesAvoidingArea(entriesAndTargets, bloodVessels)
        # endTime = time.time()
        # print('Avoid area - Blood Vessels: ', endTime - startTime, 'seconds')
        #
        # startTime = time.time()
        # PathPlanner.getTrajectoriesWithSpecifiedAngle(entriesAndTargets, cortex, angle)
        # endTime = time.time()
        # print('Use only specified angle: ', endTime - startTime, 'seconds')

        startTime = time.time()
        trajectoriesForAllHardConstraints = PathPlanner.applyAllHardConstraints(entries, targets, hippocampus,
                                                                                ventricles,
                                                                                bloodVessels, cortex,
                                                                                angle)
        # finalTrajectories = PathPlanner.getBestTrajectory(trajectoriesForAllConstraints, bloodVessels, 0.01)
        endTime = time.time()
        print('All together: ', endTime - startTime, 'seconds')

        # add to slicer scene to view
        self.registerToSlicer(trajectoriesForAllHardConstraints)
        logging.info('Processing completed')
        return True

    @staticmethod
    def registerToSlicer(trajectories):
        trajectories = PointUtils.convertEntryTargetDictionaryToVtkObject(trajectories)
        pathNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode', 'finalTrajectories')
        pathNode.SetAndObserveMesh(trajectories)


class Assignment1Test(ScriptedLoadableModuleTest):

    def setUp(self):
        slicer.mrmlScene.Clear(0)

    def runTest(self):
        self.setUp()
        self.testLoadAllData("C:\dev\kcl\\robotics\\final\models\slicer")
        self.testGetFilteredHippocampusTargets()
        # self.testAvoidVentriclesValidPath()
        # self.testAvoidVentriclesInvalidPath()
        self.testAvoidBloodVesselsValidPath()
        self.testAvoidBloodVesselsInvalidPath()
        self.testAngleValidPath()
        self.testAngleInvalidPath()
        self.testCountRejectedTrajectories(True)  # slow test
        self.testAllTogether()  # slow test
        self.delayDisplay('Finished testing')
        self.setUp()  # to reclear data

    def testLoadAllData(self, directory):
        self.delayDisplay("Starting load data test")
        self.testLoadLabel(directory + '/hippoSlicer.vtk')
        # self.testLoadLabel(directory + '/ventricles.nii')
        self.testLoadLabel(directory + '/VesselsSlicer.vtk')
        self.testLoadLabel(directory + '/CortexSlicer.vtk')
        self.testLoadFiducial(directory + '/targets.fcsv')
        self.testLoadFiducial(directory + '/entries.fcsv')
        self.delayDisplay('testLoadAllData passed!')

    def testLoadFiducial(self, path):
        self.assertTrue(slicer.util.loadMarkupsFiducialList(path))

    def testLoadLabel(self, path):
        self.assertTrue(slicer.util.loadModel(path))

    # Slow test
    # This is just to make sure all constraints run together. It doesn't actually validate the results
    def testAllTogether(self):
        hippocampus = self.getNode("hippoSlicer")
        ventricles = []#self.getNode("ventricles")
        bloodVessels = self.getNode("VesselsSlicer")
        cortex = self.getNode("CortexSlicer")
        entries = self.getNode("entries")
        targets = self.getNode("targets")
        angle = 55
        trajectoriesForAllHardConstraints = PathPlanner.applyAllHardConstraints(entries, targets, hippocampus,
                                                                                ventricles, bloodVessels, cortex, angle)
        # PathPlanner.getBestTrajectory(trajectoriesForAllHardConstraints, bloodVessels, 0.01)
        self.delayDisplay('testAllTogether passed!')

    def testGetFilteredHippocampusTargets(self):
        hippocampus = self.getNode("hippoSlicer")
        targets = self.getNode("targets")
        filteredTargets = PointUtils.getFilteredTargets(targets, hippocampus)
        self.assertTrue(targets.GetNumberOfMarkups() > len(filteredTargets))
        self.delayDisplay('testGetFilteredHippocampusTargets passed!')

    def testAvoidVentriclesValidPath(self):
        ventricles = self.getNode("ventricles")
        entriesAndTargets = {(212.09, 147.385, 76.878): [[162.0, 133.0, 90.0]]}
        result = PathPlanner.getTrajectoriesAvoidingArea(entriesAndTargets, ventricles)
        self.assertTrue(len(result) > 0)
        self.delayDisplay('testAvoidVentriclesValidPath passed!')

    def testAvoidVentriclesInvalidPath(self):
        ventricles = self.getNode("ventricles")
        entriesAndTargets = {(212.09, 147.385, 76.878): [[158.0, 128.0, 82.0]]}
        result = PathPlanner.getTrajectoriesAvoidingArea(entriesAndTargets, ventricles)
        self.assertTrue(len(result) == 0)
        self.delayDisplay('testAvoidVentriclesInvalidPath passed!')

    def testAvoidBloodVesselsValidPath(self):
        vessels = self.getNode("vessels")
        entriesAndTargets = {(212.09, 147.385, 76.878): [[162.0, 133.0, 90.0]]}
        result = PathPlanner.getTrajectoriesAvoidingArea(entriesAndTargets, vessels)
        self.assertTrue(len(result) > 0)
        self.delayDisplay('testAvoidBloodVesselsValidPath passed!')

    def testAvoidBloodVesselsInvalidPath(self):
        vessels = self.getNode("vessels")
        entriesAndTargets = {(212.09, 147.385, 76.878): [[158.0, 133.0, 82.0]]}
        result = PathPlanner.getTrajectoriesAvoidingArea(entriesAndTargets, vessels)
        self.assertTrue(len(result) == 0)
        self.delayDisplay('testAvoidBloodVesselsInvalidPath passed!')

    def testAngleValidPath(self):
        cortex = self.getNode("cortex")
        entriesAndTargets = {(212.09, 147.385, 76.878): [[162.0, 133.0, 90.0]]}
        result = PathPlanner.getTrajectoriesWithSpecifiedAngle(entriesAndTargets, cortex, 55)
        self.assertTrue(len(result) > 0)
        self.delayDisplay('testAngleValidPath passed!')

    def testAngleInvalidPath(self):
        cortex = self.getNode("cortex")
        entriesAndTargets = {(208.654, 134.777, 61.762): [[162.0, 128.0, 106.0]]}
        result = PathPlanner.getTrajectoriesWithSpecifiedAngle(entriesAndTargets, cortex, 55)
        self.assertTrue(len(result) == 0)
        self.delayDisplay('testAngleInvalidPath passed!')

    # Slow test
    def testCountRejectedTrajectories(self, printOutput):
        hippocampus = self.getNode("r_hippo")
        ventricles = self.getNode("ventricles")
        bloodVessels = self.getNode("vessels")
        cortex = self.getNode("cortex")
        entries = self.getNode("entries")
        targets = self.getNode("targets")
        angle = 55
        total = entries.GetNumberOfMarkups() * targets.GetNumberOfMarkups()
        if printOutput:
            print("Total: ", total)
        self.testCountRejectedTrajectoriesForHippocampus(entries, targets, hippocampus, total, printOutput)
        self.testCountRejectedByHardConstraints(entries, targets, hippocampus, ventricles, bloodVessels, cortex,
                                                angle, total, printOutput)
        self.delayDisplay('testCountRejectedTrajectories passed!')

    def testCountRejectedTrajectoriesForHippocampus(self, entries, targets, hippocampus, total, printOutput):
        startTime = time.time()
        filteredTargets = PointUtils.getFilteredTargets(targets, hippocampus)
        endTime = time.time()
        totalTrajectoriesOnHippocampus = entries.GetNumberOfMarkups() * len(filteredTargets)
        if printOutput:
            print('Filtering hippocampus total time: ', endTime - startTime, 'seconds')
            print("Total accepted filtering hippocampus: ", totalTrajectoriesOnHippocampus)
            print("Total rejected filtering hippocampus: ", total - totalTrajectoriesOnHippocampus)
        self.assertTrue(total - totalTrajectoriesOnHippocampus == 78336)
        self.delayDisplay('testCountRejectedTrajectoriesForHippocampus passed!')

    def testCountRejectedByHardConstraints(self, entries, targets, hippocampus, ventricles, bloodVessels, cortex,
                                           angle, total, printOutput):
        entriesAndTargets = PointUtils.convertEntryAndTargetPointsToDictionary(entries,
                                                                               PointUtils.convertMarkupNodeToPoints(
                                                                                   targets))
        self.testCountRejectedTrajectoriesForVentricles(entriesAndTargets, ventricles, total, printOutput)
        self.testCountRejectedTrajectoriesForBloodVessels(entriesAndTargets, bloodVessels, total, printOutput)
        self.testCountRejectedTrajectoriesForAngle(entriesAndTargets, cortex, angle, total, printOutput)
        self.testCountRejectedTrajectoriesCombiningAllHard(entries, targets, hippocampus, ventricles, bloodVessels,
                                                           cortex,
                                                           angle, total, printOutput)

    def testCountRejectedTrajectoriesForVentricles(self, entriesAndTargets, ventricles, total, printOutput):
        startTime = time.time()
        filteredForVentricles = PathPlanner.getTrajectoriesAvoidingArea(entriesAndTargets, ventricles)
        endTime = time.time()
        totalTrajectoriesFilteringVentricles = 0
        for _, targetValues in filteredForVentricles.items():
            totalTrajectoriesFilteringVentricles += len(targetValues)
        if printOutput:
            print('Filtering for ventricles total time: ', endTime - startTime, 'seconds')
            print("Total accepted filtering ventricles: ", totalTrajectoriesFilteringVentricles)
            print("Total rejected filtering ventricles: ", total - totalTrajectoriesFilteringVentricles)
        self.assertTrue(total - totalTrajectoriesFilteringVentricles == 10205)
        self.delayDisplay('testCountRejectedTrajectoriesForVentricles passed!')

    def testCountRejectedTrajectoriesForBloodVessels(self, entriesAndTargets, bloodVessels, total, printOutput):
        startTime = time.time()
        filteredForBloodVessels = PathPlanner.getTrajectoriesAvoidingArea(entriesAndTargets, bloodVessels)
        endTime = time.time()
        totalTrajectoriesFilteringBloodVessels = 0
        for _, targetValues in filteredForBloodVessels.items():
            totalTrajectoriesFilteringBloodVessels += len(targetValues)
        if printOutput:
            print('Filtering for blood vessels total time: ', endTime - startTime, 'seconds')
            print("Total accepted filtering blood vessels: ", totalTrajectoriesFilteringBloodVessels)
            print("Total rejected filtering blood vessels: ", total - totalTrajectoriesFilteringBloodVessels)
        self.assertTrue(total - totalTrajectoriesFilteringBloodVessels == 47855)
        self.delayDisplay('testCountRejectedTrajectoriesForBloodVessels passed!')

    def testCountRejectedTrajectoriesForAngle(self, entriesAndTargets, cortex, angle, total, printOutput):
        startTime = time.time()
        filteredForAngles = PathPlanner.getTrajectoriesWithSpecifiedAngle(entriesAndTargets, cortex, angle)
        endTime = time.time()
        totalTrajectoriesFilteringAngles = 0
        for _, targetValues in filteredForAngles.items():
            totalTrajectoriesFilteringAngles += len(targetValues)
        if printOutput:
            print('Filtering for angles total time: ', endTime - startTime, 'seconds')
            print("Total accepted filtering angles: ", totalTrajectoriesFilteringAngles)
            print("Total rejected filtering angles: ", total - totalTrajectoriesFilteringAngles)
        self.assertTrue(total - totalTrajectoriesFilteringAngles == 17426)
        self.delayDisplay('testCountRejectedTrajectoriesForAngle passed!')

    def testCountRejectedTrajectoriesCombiningAllHard(self, entries, targets, hippocampus, ventricles, bloodVessels,
                                                      cortex,
                                                      angle, total, printOutput):
        startTime = time.time()
        totalTrajectoriesForAllConstraints = PathPlanner.applyAllHardConstraints(entries, targets, hippocampus,
                                                                                 ventricles,
                                                                                 bloodVessels, cortex, angle)
        endTime = time.time()
        totalTrajectoriesFilteringAllConstraints = 0
        for _, targets in totalTrajectoriesForAllConstraints.items():
            totalTrajectoriesFilteringAllConstraints += len(targets)
        if printOutput:
            print('Filtering for all hard constraints total time: ', endTime - startTime, 'seconds')
            print("Total accepted filtering all hard constraints: ", totalTrajectoriesFilteringAllConstraints)
            print("Total rejected filtering all hard constraints: ", total - totalTrajectoriesFilteringAllConstraints)
        self.assertTrue(total - totalTrajectoriesFilteringAllConstraints == 88603)
        self.delayDisplay('testCountRejectedTrajectoriesCombiningAll passed!')

    @staticmethod
    def getNode(fileName):
        return slicer.util.getNode(fileName)
