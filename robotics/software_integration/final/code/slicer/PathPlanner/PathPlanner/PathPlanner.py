import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import PointUtils
import PathPlannerUtils
import GeometryUtils
import time
import numpy as np


#
# PathPlanner
#

class PathPlanner(ScriptedLoadableModule):

    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = "Path Planner"
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
# PathPlannerWidget
#

class PathPlannerWidget(ScriptedLoadableModuleWidget):
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
        # vtkMRMLLabelMapVolumeNode
        # vtkMRMLModelNode
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

        self.bloodVesselDilateSelector = slicer.qMRMLNodeComboBox()
        self.bloodVesselDilateSelector.nodeTypes = ["vtkMRMLLabelMapVolumeNode"]
        self.bloodVesselDilateSelector.selectNodeUponCreation = True
        self.bloodVesselDilateSelector.addEnabled = False
        self.bloodVesselDilateSelector.removeEnabled = False
        self.bloodVesselDilateSelector.noneEnabled = False
        self.bloodVesselDilateSelector.showHidden = False
        self.bloodVesselDilateSelector.showChildNodeTypes = False
        self.bloodVesselDilateSelector.setMRMLScene(slicer.mrmlScene)
        self.bloodVesselDilateSelector.setToolTip("The blood vessel dilate labels")
        parametersFormLayout.addRow("Blood Vessels Dilate Volume: ", self.bloodVesselDilateSelector)

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


        self.distanceThreshold = ctk.ctkSliderWidget()
        self.distanceThreshold.singleStep = 1
        self.distanceThreshold.minimum = 0
        self.distanceThreshold.maximum = 9999
        self.distanceThreshold.value = 9999
        self.distanceThreshold.setToolTip("Set maximum incision value")
        parametersFormLayout.addRow("Maximum trajectory length", self.distanceThreshold)

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
        self.applyButton.enabled = self.hippocampusSelector.currentNode() and self.bloodVesselDilateSelector.currentNode() and self.bloodVesselSelector.currentNode() and self.cortexSelector.currentNode() and self.entrySelector.currentNode() and self.targetSelector.currentNode()

    def onApplyButton(self):
        logic = PathPlannerLogic()
        logic.run(self.hippocampusSelector.currentNode(),
                  self.bloodVesselDilateSelector.currentNode(),
                  self.bloodVesselSelector.currentNode(),
                  self.cortexSelector.currentNode(),
                  self.entrySelector.currentNode(),
                  self.targetSelector.currentNode(),
                  self.angleSlider.value,
                  self.distanceThreshold.value)


#
# PathPlanner Logic
#

class PathPlannerLogic(ScriptedLoadableModuleLogic):

    def isValidInputOutputData(self, hippocampus, bloodVesselsDilate, bloodVessels, cortex, entries, targets, angle, distanceThreshold):
        """Validates if the output is not the same as input
        """
        if not hippocampus:
            logging.debug('No hippocampus data selected')
            return False
        if not bloodVesselsDilate:
            logging.debug('No blood vessels dilate data selected')
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
        if not distanceThreshold:
            logging.debug('No valid maximum trajectory distance selected')
            return False
        return True

    def run(self, hippocampus, bloodVesselsDilate, bloodVessels, cortex, entries, targets, angle, distanceThreshold):
        """
        Run the actual algorithm
        """
        if not self.isValidInputOutputData(hippocampus, bloodVesselsDilate, bloodVessels, cortex, entries, targets,
                                           angle, distanceThreshold):
            slicer.util.errorDisplay('Invalid input.')
            return False

        logging.info('Processing started')

        # uncomment to see one-by-one timings
        # self.timeEachComponent(entries, targets, hippocampus, bloodVesselsDilate, bloodVessels, cortex, angle, distanceThreshold)

        startTime = time.time()
        trajectoriesForAllHardConstraints = PathPlannerUtils.applyAllHardConstraints(entries, targets, hippocampus,
                                                                                     bloodVesselsDilate,
                                                                                     bloodVessels, cortex,
                                                                                     angle, distanceThreshold)
        bestAndWorstPair = PathPlannerUtils.getBestAndWorstTrajectory(trajectoriesForAllHardConstraints, bloodVessels,
                                                                       bloodVesselsDilate, 0.01)
        endTime = time.time()
        print('All together: ', endTime - startTime, 'seconds')

        # add to slicer scene to view
        self.registerToSlicer(bestAndWorstPair)
        logging.info('Processing completed')
        return True

    def registerToSlicer(self, bestAndWorstPair):
        maxTrajectory = bestAndWorstPair[0][1]
        self.registerEntryTargetPair(maxTrajectory)

        # minTrajectory = PointUtils.convertEntryTargetPairToVtkObject(finalTrajectories[1][1])

    def registerEntryTargetPair(self, entryTargetPair):
        self.createAndRegisterFiducial(entryTargetPair[0], 'Entry')
        self.createAndRegisterFiducial(entryTargetPair[1], 'Target')

    def createAndRegisterFiducial(self, coordinates, label):
        fudicualNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', label)
        fudicualNode.AddFiducialFromArray(coordinates)

    # Helps to see how much time each component takes on its own. Could have probably been an automated test instead
    def timeEachComponent(self, entries, targets, hippocampus, bloodVesselsDilate, bloodVessels, cortex,
                          angle, distanceThreshold):
        startTime = time.time()
        PointUtils.getFilteredTargets(targets, hippocampus)
        endTime = time.time()
        print('Filtered targets time: ', endTime - startTime, 'seconds')

        entriesAndTargets = PointUtils.getTrajectoryDictionary(entries,
                                                               PointUtils.convertMarkupNodeToPoints(targets))

        startTime = time.time()
        PathPlannerUtils.getTrajectoriesOfMaximumLength(entriesAndTargets, distanceThreshold)
        endTime = time.time()
        print('Maximum trajectory: ', endTime - startTime, 'seconds')

        startTime = time.time()
        PathPlannerUtils.getTrajectoriesAvoidingArea(entriesAndTargets, bloodVesselsDilate)
        endTime = time.time()
        print('Avoid area - Blood Vessels Dilate: ', endTime - startTime, 'seconds')

        startTime = time.time()
        PathPlannerUtils.getTrajectoriesAvoidingArea(entriesAndTargets, bloodVessels)
        endTime = time.time()
        print('Avoid area - Blood Vessels: ', endTime - startTime, 'seconds')

        startTime = time.time()
        PathPlannerUtils.getTrajectoriesWithSpecifiedAngle(entriesAndTargets, cortex, angle)
        endTime = time.time()
        print('Use only specified angle: ', endTime - startTime, 'seconds')
        endTime = time.time()
        print('All together: ', endTime - startTime, 'seconds')


class PathPlannerTest(ScriptedLoadableModuleTest):

    def __init__(self):
        self.DIRECTORY = "C:\dev\kcl\\robotics\\final\models and scenes\\tests"
        self.TARGETS_NODE_LABEL = "targets"
        self.ENTRIES_NODE_LABEL = "entries"
        self.CORTEX_NODE_LABEL = "cortexLabelMap"
        self.VESSEL_NODE_LABEL = "vesselLabelMap"
        self.HIPPOCAMPUS_NODE_LABEL = "hippoLabelMap"
        self.VESSEL_DILATE_NODE_LABEL = "vesselDilateLabelMap"

    def setUp(self):
        slicer.mrmlScene.Clear(0)

    def runTest(self):
        self.setUp()
        self.testLoadAllData(self.DIRECTORY)
        self.testGetFilteredHippocampusValidTargets()
        self.testGetFilteredHippocampusInvalidTargets()
        self.testFilterTrajectoriesBelowDistanceThreshold()
        self.testFilterTrajectoriesAboveDistanceThreshold()
        self.testAvoidBloodVesselsDilateValidPath()
        self.testAvoidBloodVesselsDilateInvalidPath()
        self.testAvoidBloodVesselsValidPath()
        self.testAvoidBloodVesselsInvalidPath()
        self.testAngleValidPath()
        self.testAngleInvalidPath()
        # self.testUnnecessaryTests()
        self.delayDisplay('Finished testing')
        self.setUp()  # to reclear data

    def testLoadAllData(self, directory):
        self.delayDisplay("Starting load data test")
        self.testLoadLabel(directory + '/hippoLabelMap.nii.gz')
        self.testLoadLabel(directory + '/vesselLabelMap.nii.gz')
        self.testLoadLabel(directory + '/vesselDilateLabelMap.nii.gz')
        self.testLoadLabel(directory + '/cortexLabelMap.nii.gz')
        self.testLoadFiducial(directory + '/targets.fcsv')
        self.testLoadFiducial(directory + '/entries.fcsv')
        self.delayDisplay('testLoadAllData passed!')

    def testLoadFiducial(self, path):
        self.assertTrue(slicer.util.loadMarkupsFiducialList(path))

    def testLoadLabel(self, path):
        self.assertTrue(slicer.util.loadLabelVolume(path))

    # They don't really test anything. Mostly used for sanity checking
    # Values rejected for count rejected tests might need some adjustments
    def testUnnecessaryTests(self):
        self.testCountRejectedTrajectories(True)  # slow test
        self.testAllTogether()  # slow test

    # Slow test
    # This is just to make sure all constraints run together. It doesn't actually validate the results
    def testAllTogether(self):
        hippocampus = self.getNode(self.HIPPOCAMPUS_NODE_LABEL)
        bloodVesselsDilate = self.getNode(self.VESSEL_DILATE_NODE_LABEL)
        bloodVessels = self.getNode(self.VESSEL_NODE_LABEL)
        cortex = self.getNode(self.CORTEX_NODE_LABEL)
        entries = self.getNode(self.ENTRIES_NODE_LABEL)
        targets = self.getNode(self.TARGETS_NODE_LABEL)
        angle = 55
        trajectoriesForAllHardConstraints = PathPlannerUtils.applyAllHardConstraints(entries, targets, hippocampus,
                                                                                     bloodVesselsDilate,
                                                                                     bloodVessels, cortex,
                                                                                     angle)
        finalTrajectories = PathPlannerUtils.getBestAndWorstTrajectory(trajectoriesForAllHardConstraints, bloodVessels,
                                                                       bloodVesselsDilate, 0.01)
        logic = PathPlannerLogic()
        logic.registerToSlicer(finalTrajectories)
        self.delayDisplay('testAllTogether passed!')

    def testGetFilteredHippocampusValidTargets(self):
        hippocampus = self.getNode(self.HIPPOCAMPUS_NODE_LABEL)
        targets = self.getNode(self.TARGETS_NODE_LABEL)
        filteredTargets = PointUtils.getFilteredTargets(targets, hippocampus)
        self.assertTrue(targets.GetNumberOfMarkups() > len(filteredTargets))
        self.delayDisplay('testGetFilteredHippocampusValidTargets passed!')

    def testGetFilteredHippocampusInvalidTargets(self):
        hippocampus = self.getNode(self.HIPPOCAMPUS_NODE_LABEL)
        coordinates = [0, 1, 2]
        targets = slicer.vtkMRMLMarkupsFiducialNode()
        targets.AddFiducialFromArray(coordinates)
        filteredTargets = PointUtils.getFilteredTargets(targets, hippocampus)
        self.assertTrue(len(filteredTargets) == 0)
        self.delayDisplay('testGetFilteredHippocampusInvalidTargets passed!')

    def testFilterTrajectoriesBelowDistanceThreshold(self):
        entriesAndTargets = {(196.989, 131.913, 32.491): [[150.0, 128.0, 114.0]]}
        threshold = 9999
        result = PathPlannerUtils.getTrajectoriesOfMaximumLength(entriesAndTargets, threshold)
        self.assertTrue(len(result) > 0)
        self.delayDisplay('testFilterTrajectoriesBelowDistanceThreshold passed!')

    def testFilterTrajectoriesAboveDistanceThreshold(self):
        entriesAndTargets = {(196.989, 131.913, 32.491): [[150.0, 128.0, 114.0]]}
        threshold = 0
        result = PathPlannerUtils.getTrajectoriesOfMaximumLength(entriesAndTargets, threshold)
        self.assertTrue(len(result) == 0)
        self.delayDisplay('testFilterTrajectoriesAboveDistanceThreshold passed!')

    def testAvoidBloodVesselsDilateValidPath(self):
        bloodVesselsDilate = self.getNode(self.VESSEL_DILATE_NODE_LABEL)
        entriesAndTargets = {(196.989, 131.913, 32.491): [[150.0, 128.0, 114.0]]}
        result = PathPlannerUtils.getTrajectoriesAvoidingArea(entriesAndTargets, bloodVesselsDilate)
        self.assertTrue(len(result) > 0)
        self.delayDisplay('testAvoidBloodVesselsDilateValidPath passed!')

    def testAvoidBloodVesselsDilateInvalidPath(self):
        bloodVesselsDilate = self.getNode(self.VESSEL_DILATE_NODE_LABEL)
        entriesAndTargets = {(205.327, 107.823, 58.771): [[158.0, 133.0, 82.0]]}
        result = PathPlannerUtils.getTrajectoriesAvoidingArea(entriesAndTargets, bloodVesselsDilate)
        self.assertTrue(len(result) == 0)
        self.delayDisplay('testAvoidBloodVesselsDilateInvalidPath passed!')

    def testAvoidBloodVesselsValidPath(self):
        bloodVessels = self.getNode(self.VESSEL_NODE_LABEL)
        entriesAndTargets = {(196.989, 131.913, 32.491): [[150.0, 128.0, 114.0]]}
        result = PathPlannerUtils.getTrajectoriesAvoidingArea(entriesAndTargets, bloodVessels)
        self.assertTrue(len(result) > 0)
        self.delayDisplay('testAvoidBloodVesselsValidPath passed!')

    def testAvoidBloodVesselsInvalidPath(self):
        bloodVessels = self.getNode(self.VESSEL_NODE_LABEL)
        entriesAndTargets = {(212.09, 147.385, 76.878): [[158.0, 133.0, 82.0]]}
        result = PathPlannerUtils.getTrajectoriesAvoidingArea(entriesAndTargets, bloodVessels)
        self.assertTrue(len(result) == 0)
        self.delayDisplay('testAvoidBloodVesselsInvalidPath passed!')

    def testAngleValidPath(self):
        cortex = self.getNode(self.CORTEX_NODE_LABEL)
        entriesAndTargets = {(196.989, 131.913, 32.491): [[150.0, 128.0, 114.0]]}
        result = PathPlannerUtils.getTrajectoriesWithSpecifiedAngle(entriesAndTargets, cortex, 55)
        self.assertTrue(len(result) > 0)
        self.delayDisplay('testAngleValidPath passed!')

    def testAngleInvalidPath(self):
        cortex = self.getNode(self.CORTEX_NODE_LABEL)
        entriesAndTargets = {(208.654, 134.777, 61.762): [[162.0, 128.0, 106.0]]}
        result = PathPlannerUtils.getTrajectoriesWithSpecifiedAngle(entriesAndTargets, cortex, 55)
        self.assertTrue(len(result) == 0)
        self.delayDisplay('testAngleInvalidPath passed!')

    # Slow test
    # In theory this "test" is wrong as it uses real data files but I've used it for sanity checks and to optimise
    # the order in which each constraint should run
    def testCountRejectedTrajectories(self, printOutput):
        hippocampus = self.getNode(self.HIPPOCAMPUS_NODE_LABEL)
        bloodVesselsDilate = self.getNode(self.VESSEL_DILATE_NODE_LABEL)
        bloodVessels = self.getNode(self.VESSEL_NODE_LABEL)
        cortex = self.getNode(self.CORTEX_NODE_LABEL)
        entries = self.getNode(self.ENTRIES_NODE_LABEL)
        targets = self.getNode(self.TARGETS_NODE_LABEL)
        angle = 55
        distanceThreshold = 60
        total = entries.GetNumberOfMarkups() * targets.GetNumberOfMarkups()
        if printOutput:
            print("Total: ", total)
        self.testCountRejectedTrajectoriesForHippocampus(entries, targets, hippocampus, total, printOutput)
        self.testCountRejectedByHardConstraints(entries, targets, hippocampus, bloodVesselsDilate, bloodVessels, cortex,
                                                angle, distanceThreshold, total, printOutput)
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
        self.assertTrue(total - totalTrajectoriesOnHippocampus == 83520)
        self.delayDisplay('testCountRejectedTrajectoriesForHippocampus passed!')

    def testCountRejectedByHardConstraints(self, entries, targets, hippocampus, bloodVesselsDilate, bloodVessels,
                                           cortex,
                                           angle, distanceThreshold, total, printOutput):
        entriesAndTargets = PointUtils.convertEntryAndTargetPointsToDictionary(entries,
                                                                               PointUtils.convertMarkupNodeToPoints(
                                                                                   targets))
        self.testCountRejectedTrajectoriesForDistanceThreshold(entriesAndTargets, distanceThreshold, total,
                                                                printOutput)
        self.testCountRejectedTrajectoriesForBloodVesselsDilate(entriesAndTargets, bloodVesselsDilate, total,
                                                                printOutput)
        self.testCountRejectedTrajectoriesForBloodVessels(entriesAndTargets, bloodVessels, total, printOutput)
        self.testCountRejectedTrajectoriesForAngle(entriesAndTargets, cortex, angle, total, printOutput)
        self.testCountRejectedTrajectoriesCombiningAllHard(entries, targets, hippocampus, bloodVesselsDilate,
                                                           bloodVessels,
                                                           cortex,
                                                           angle, total, printOutput)

    def testCountRejectedTrajectoriesForDistanceThreshold(self, entriesAndTargets, distanceThreshold, total, printOutput):
        startTime = time.time()
        filteredForDistance = PathPlannerUtils.getTrajectoriesOfMaximumLength(entriesAndTargets, distanceThreshold)
        endTime = time.time()
        totalTrajectoriesFilteredForDistance = 0
        for _, targetValues in filteredForDistance.items():
            totalTrajectoriesFilteredForDistance += len(targetValues)
        if printOutput:
            print('Filtering for distance total time: ', endTime - startTime, 'seconds')
            print("Total accepted filtering distance: ", totalTrajectoriesFilteredForDistance)
            print("Total rejected filtering distance: ", total - totalTrajectoriesFilteredForDistance)
        self.assertTrue(total - totalTrajectoriesFilteredForDistance == 65395)
        self.delayDisplay('testCountRejectedTrajectoriesForDistanceThreshold passed!')

    def testCountRejectedTrajectoriesForBloodVesselsDilate(self, entriesAndTargets, bloodVesselsDilate, total,
                                                           printOutput):
        startTime = time.time()
        filteredForBloodVessels = PathPlannerUtils.getTrajectoriesAvoidingArea(entriesAndTargets, bloodVesselsDilate)
        endTime = time.time()
        totalTrajectoriesFilteringBloodVesselsDilate = 0
        for _, targetValues in filteredForBloodVessels.items():
            totalTrajectoriesFilteringBloodVesselsDilate += len(targetValues)
        if printOutput:
            print('Filtering for blood vessels dilate total time: ', endTime - startTime, 'seconds')
            print("Total accepted filtering blood vessels dilate: ", totalTrajectoriesFilteringBloodVesselsDilate)
            print("Total rejected filtering blood vessels dilate: ",
                  total - totalTrajectoriesFilteringBloodVesselsDilate)
        self.assertTrue(total - totalTrajectoriesFilteringBloodVesselsDilate == 9033)
        self.delayDisplay('testCountRejectedTrajectoriesForBloodVesselsDilate passed!')

    def testCountRejectedTrajectoriesForBloodVessels(self, entriesAndTargets, bloodVessels, total, printOutput):
        startTime = time.time()
        filteredForBloodVessels = PathPlannerUtils.getTrajectoriesAvoidingArea(entriesAndTargets, bloodVessels)
        endTime = time.time()
        totalTrajectoriesFilteringBloodVessels = 0
        for _, targetValues in filteredForBloodVessels.items():
            totalTrajectoriesFilteringBloodVessels += len(targetValues)
        if printOutput:
            print('Filtering for blood vessels total time: ', endTime - startTime, 'seconds')
            print("Total accepted filtering blood vessels: ", totalTrajectoriesFilteringBloodVessels)
            print("Total rejected filtering blood vessels: ", total - totalTrajectoriesFilteringBloodVessels)
        self.assertTrue(total - totalTrajectoriesFilteringBloodVessels == 68206)
        self.delayDisplay('testCountRejectedTrajectoriesForBloodVessels passed!')

    def testCountRejectedTrajectoriesForAngle(self, entriesAndTargets, cortex, angle, total, printOutput):
        startTime = time.time()
        filteredForAngles = PathPlannerUtils.getTrajectoriesWithSpecifiedAngle(entriesAndTargets, cortex, angle)
        endTime = time.time()
        totalTrajectoriesFilteringAngles = 0
        for _, targetValues in filteredForAngles.items():
            totalTrajectoriesFilteringAngles += len(targetValues)
        if printOutput:
            print('Filtering for angles total time: ', endTime - startTime, 'seconds')
            print("Total accepted filtering angles: ", totalTrajectoriesFilteringAngles)
            print("Total rejected filtering angles: ", total - totalTrajectoriesFilteringAngles)
        self.assertTrue(total - totalTrajectoriesFilteringAngles == 19405)
        self.delayDisplay('testCountRejectedTrajectoriesForAngle passed!')

    def testCountRejectedTrajectoriesCombiningAllHard(self, entries, targets, hippocampus, bloodVesselsDilate,
                                                      bloodVessels,
                                                      cortex,
                                                      angle, total, printOutput):
        startTime = time.time()
        totalTrajectoriesForAllConstraints = PathPlannerUtils.applyAllHardConstraints(entries, targets, hippocampus,
                                                                                      bloodVesselsDilate,
                                                                                      bloodVessels, cortex, angle)
        endTime = time.time()
        totalTrajectoriesFilteringAllConstraints = 0
        for _, targets in totalTrajectoriesForAllConstraints.items():
            totalTrajectoriesFilteringAllConstraints += len(targets)
        if printOutput:
            print('Filtering for all hard constraints total time: ', endTime - startTime, 'seconds')
            print("Total accepted filtering all hard constraints: ", totalTrajectoriesFilteringAllConstraints)
            print("Total rejected filtering all hard constraints: ", total - totalTrajectoriesFilteringAllConstraints)
        self.assertTrue(total - totalTrajectoriesFilteringAllConstraints == 92884)
        self.delayDisplay('testCountRejectedTrajectoriesCombiningAll passed!')

    @staticmethod
    def getNode(fileName):
        return slicer.util.getNode(fileName)
