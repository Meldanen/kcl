#!/usr/bin/env python3

from basic_robot.msg import instructionsMessage
from NodeTypeEnum import NodeTypeEnum
from MoveValidityEnum import MoveValidityEnum
from MovementModeEnum import MovementModeEnum
from MovementModeEnum import Utils as MovementModeEnumUtils

class Message:

    def __init__(self):
        self.message = instructionsMessage()
        self.clearMessage()

    def clearMessage(self):
        self.setMode(MovementModeEnum.NONE.getLabel)
        self.setX(0)
        self.setY(0)
        self.setZ(0)
        self.setJoint1(0)
        self.setJoint2(0)
        self.setSuccess(MoveValidityEnum.NOT_AVAILABLE.value)
        self.setPosition(("N/A", "N/A"))
        self.setNode(NodeTypeEnum.CLIENT.value)

    def setMessage(self, mode, x, y, z, joint1, joint2, success, position, node):
        self.setMode(mode)
        self.setX(x)
        self.setY(y)
        self.setZ(z)
        self.setJoint1(joint1)
        self.setJoint2(joint2)
        self.setSuccess(success)
        self.setPosition(position)
        self.setNode(node)

    def setNode(self, node):
        if node:
            self.message.node = node

    def setPosition(self, position):
        if position:
            self.message.position = "First Joint position: " + str(position[0]) + ", Second Joint position: " + str(
                position[1])

    def setSuccess(self, success):
        if success:
            self.message.success = success

    def setJoint2(self, joint2):
        if joint2:
            self.message.joint2 = joint2

    def setJoint1(self, joint1):
        if joint1:
            self.message.joint1 = joint1

    def setZ(self, z):
        if z:
            self.message.z = z

    def setY(self, y):
        if y:
            self.message.y = y

    def setX(self, x):
        if x:
            self.message.x = x

    def setMode(self, mode):
        if mode:
            self.message.mode = mode

    def getRosMessage(self):
        return self.message

    def getNode(self):
        return self.message.node

    def getFinalPosition(self):
        return self.message.position

    def getMoveSuccessful(self):
        return self.message.success

    def getJoint2(self):
        return self.message.joint2

    def getJoint1(self):
        return self.message.joint1

    def getZ(self):
        return self.message.z

    def getY(self):
        return self.message.y

    def getX(self):
        return self.message.x

    def getMode(self):
        return self.message.mode

    def isUsingJointPosition(self):
        return MovementModeEnumUtils.getEnumFromLabel(self.getMode()).isJointPosition

    def isUsingEndEffectorPosition(self):
        return MovementModeEnumUtils.getEnumFromLabel(self.getMode()).isEndEffectorPosition
