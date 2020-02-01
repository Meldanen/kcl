import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import PointUtils
import PathPlanner
import time


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

        entriesAndTargets = {}
        combinedEntriesAndTargets = {}

        startTime = time.time()
        PointUtils.getFilteredTargets(targets, hippocampus)
        endTime = time.time()
        print('Filtered targets time: ', endTime - startTime, 'seconds')

        entriesAndTargets = PointUtils().getEntriesAndTargetsInDict(entries,
                                                                    PointUtils().convertMarkupNodeToPoints(targets))

        startTime = time.time()
        PathPlanner.getEntryTargetDictionaryAvoidingArea(entriesAndTargets, ventricles)
        endTime = time.time()
        print('Avoid area - Ventricles: ', endTime - startTime, 'seconds')

        startTime = time.time()
        PathPlanner.getEntryTargetDictionaryAvoidingArea(entriesAndTargets, bloodVessels)
        endTime = time.time()
        print('Avoid area - Blood Vessels: ', endTime - startTime, 'seconds')

        startTime = time.time()
        PathPlanner.getEntryTargetDictionaryWithSpecifiedAngle(entriesAndTargets, cortex, angle)
        endTime = time.time()
        print('Use only specified angle: ', endTime - startTime, 'seconds')

        startTime = time.time()
        filteredTargets = PointUtils.getFilteredTargets(targets, hippocampus)
        combinedEntriesAndTargets = PointUtils.getEntriesAndTargetsInDict(entries, filteredTargets)
        combinedEntriesAndTargets = PathPlanner.applySpecifiedConstraints(combinedEntriesAndTargets, ventricles,
                                                                            bloodVessels, cortex,
                                                                            angle)
        endTime = time.time()
        print('All together: ', endTime - startTime, 'seconds')

        # good to have some way of seeing our results
        allPaths = PointUtils.printEntryAndTargetsInDict(combinedEntriesAndTargets)
        pathNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode', 'GoodPaths')
        pathNode.SetAndObserveMesh(allPaths)
        # you can add something here to output the good entry target pairs
        logging.info('Processing completed')
        return True


class Assignment1Test(ScriptedLoadableModuleTest):

    def setUp(self):
        slicer.mrmlScene.Clear(0)

    def runTest(self):
        self.setUp()
        self.testLoadAllData("C:\Users\dorit\BrainParcellation")
        self.testGetFilteredHippocampusTargets()
        self.testAllTogether()
        self.testAvoidVentriclesValidPath()
        self.testAvoidVentriclesInvalidPath()
        self.testAvoidBloodVesselsValidPath()
        self.testAvoidBloodVesselsInvalidPath()
        self.testAngleValidPath()
        self.testAngleInvalidPath()
        self.delayDisplay('Finished testing')
        self.setUp()  # to reclear data

    def testLoadAllData(self, directory):
        self.delayDisplay("Starting load data test")
        self.testLoadLabel(directory + '/r_hippo.nii')
        self.testLoadLabel(directory + '/ventricles.nii')
        self.testLoadLabel(directory + '/vessels.nii')
        self.testLoadLabel(directory + '/cortex.nii')
        self.testLoadFiducial(directory + '/targets.fcsv')
        self.testLoadFiducial(directory + '/entries.fcsv')
        self.delayDisplay('testLoadAllData passed!')

    def testLoadFiducial(self, path):
        self.assertTrue(slicer.util.loadMarkupsFiducialList(path))

    def testLoadLabel(self, path):
        self.assertTrue(slicer.util.loadLabelVolume(path))

    # This is just to make sure all constraints run together. It doesn't actually validate the results
    def testAllTogether(self):
        hippocampus = slicer.util.getNode("r_hippo")
        ventricles = slicer.util.getNode("ventricles")
        bloodVessels = slicer.util.getNode("vessels")
        cortex = slicer.util.getNode("cortex")
        entries = slicer.util.getNode("entries")
        targets = slicer.util.getNode("targets")
        angle = 55
        filteredTargets = PointUtils.getFilteredTargets(targets, hippocampus)
        entryTargetDictionary = PointUtils.getEntriesAndTargetsInDict(entries, filteredTargets)
        PathPlanner.applySpecifiedConstraints(entryTargetDictionary, ventricles, bloodVessels, cortex, angle)
        self.delayDisplay('testAllTogether passed!')

    def testGetFilteredHippocampusTargets(self):
        hippocampus = slicer.util.getNode("r_hippo")
        targets = slicer.util.getNode("targets")
        filteredTargets = PointUtils.getFilteredTargets(targets, hippocampus)
        self.assertTrue(targets.GetNumberOfMarkups() > len(filteredTargets))
        self.delayDisplay('testGetFilteredHippocampusTargets passed!')

    def testAvoidVentriclesValidPath(self):
        ventricles = slicer.util.getNode("ventricles")
        entriesAndTargets = {(212.09, 147.385, 76.878): [[162.0, 133.0, 90.0]]}
        result = PathPlanner.getEntryTargetDictionaryAvoidingArea(entriesAndTargets, ventricles)
        self.assertTrue(len(result) > 0)
        self.delayDisplay('testAvoidVentriclesValidPath passed!')

    def testAvoidVentriclesInvalidPath(self):
        ventricles = slicer.util.getNode("ventricles")
        entriesAndTargets = {(212.09, 147.385, 76.878): [[158.0, 128.0, 82.0]]}
        result = PathPlanner.getEntryTargetDictionaryAvoidingArea(entriesAndTargets, ventricles)
        self.assertTrue(len(result) == 0)
        self.delayDisplay('testAvoidVentriclesInvalidPath passed!')

    def testAvoidBloodVesselsValidPath(self):
        vessels = slicer.util.getNode("vessels")
        entriesAndTargets = {(212.09, 147.385, 76.878): [[162.0, 133.0, 90.0]]}
        result = PathPlanner.getEntryTargetDictionaryAvoidingArea(entriesAndTargets, vessels)
        self.assertTrue(len(result) > 0)
        self.delayDisplay('testAvoidBloodVesselsValidPath passed!')

    def testAvoidBloodVesselsInvalidPath(self):
        vessels = slicer.util.getNode("vessels")
        entriesAndTargets = {(212.09, 147.385, 76.878): [[158.0, 133.0, 82.0]]}
        result = PathPlanner.getEntryTargetDictionaryAvoidingArea(entriesAndTargets, vessels)
        self.assertTrue(len(result) == 0)
        self.delayDisplay('testAvoidBloodVesselsInvalidPath passed!')

    def testAngleValidPath(self):
        cortex = slicer.util.getNode("cortex")
        entriesAndTargets = {(212.09, 147.385, 76.878): [[162.0, 133.0, 90.0]]}
        result = PathPlanner.getEntryTargetDictionaryWithSpecifiedAngle(entriesAndTargets, cortex, 55)
        self.assertTrue(len(result) > 0)
        self.delayDisplay('testAngleValidPath passed!')

    def testAngleInvalidPath(self):
        cortex = slicer.util.getNode("cortex")
        entriesAndTargets = {(208.654, 134.777, 61.762): [[162.0, 128.0, 106.0]]}
        result = PathPlanner.getEntryTargetDictionaryWithSpecifiedAngle(entriesAndTargets, cortex, 55)
        self.assertTrue(len(result) == 0)
        self.delayDisplay('testAngleInvalidPath passed!')
