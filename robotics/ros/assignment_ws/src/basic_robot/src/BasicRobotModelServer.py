#!/usr/bin/env python3

import rospy
import numpy as np
from sensor_msgs.msg import JointState
from basic_robot.msg import instructionsMessage
from Message import Message
from Kinematics import Kinematics
from NodeTypeEnum import NodeTypeEnum
from MoveValidityEnum import MoveValidityEnum
from MovementModeEnum import Utils as MovementModeUtils

class RobotState:
    def __init__(self):
        self.initJointState()
        self.initPublishersAndSubscribers()
        self.message = Message()
        self.kinematics = Kinematics()

    def initJointState(self):
        self.jointState = JointState()
        self.jointState.name = ['joint1', 'joint2']
        self.jointState.position = [0.0, 0.0]

    def initPublishersAndSubscribers(self):
        rospy.Subscriber(NodeTypeEnum.TWO_WAY_COMMUNICATION_CHATTER.value, instructionsMessage, self.callback)
        self.publisher = rospy.Publisher(NodeTypeEnum.TWO_WAY_COMMUNICATION_CHATTER.value, instructionsMessage, queue_size=1)
        self.jointStatePublisher = rospy.Publisher(NodeTypeEnum.JOINT_STATES.value, JointState, queue_size=1)

    def setResponseMessage(self, data):
        jointStatePosition = self.getJointStatePosition(data)
        if jointStatePosition[2].isValid:
            joint1, joint2 = jointStatePosition[0], jointStatePosition[1]
            x, y, z = self.kinematics.getForwardKinematics(joint1, joint2)
            self.jointState.position = [joint1, joint2]
        else:
            x, y, z = 0.0, 0.0, 0.0
            joint1, joint2 = self.jointState.position[0], self.jointState.position[1]
        self.setMessage(data.mode, x, y, z, joint1, joint2, jointStatePosition)

    def start(self):
        while not rospy.is_shutdown():
            self.updateJoints()
            self.publishMessage(self.message)

    def publishMessage(self, message):
        self.publisher.publish(message.getRosMessage())

    def callback(self, data):
        if data.node == NodeTypeEnum.CLIENT.value:
            self.setResponseMessage(data)

    def updateJoints(self):
        self.jointState.header.stamp = rospy.Time.now()
        self.jointStatePublisher.publish(self.jointState)

    def getJointStatePosition(self, data):
        mode = MovementModeUtils.getEnumFromLabel(data.mode)
        if mode.isJointPosition:
            return data.joint1, data.joint2, MoveValidityEnum.VALID
        t1, t2 = self.kinematics.getInverseKinematics(data.x, data.y, data.z)
        if self.isValidPosition(t1, t2, data):
            return t1, t2, MoveValidityEnum.VALID
        return self.jointState.position[0], self.jointState.position[1], MoveValidityEnum.INVALID

    def isValidPosition(self, t1, t2, data):
        x, y, z = self.kinematics.getForwardKinematics(t1, t2)
        return np.isclose(x, data.x) and np.isclose(y, data.y) and np.isclose(z, data.z)

    def setMessage(self, mode, x, y, z, joint1, joint2, jointStatePosition):
        self.message.setMessage(mode=mode, x=x, y=y, z=z, joint1=joint1, joint2=joint2,
                                success=jointStatePosition[2].value,
                                position=jointStatePosition, node=NodeTypeEnum.SERVER.value)


if __name__ == '__main__':
    try:
        rospy.init_node(NodeTypeEnum.BASIC_ROBOT_MODEL_SERVER.value)
        robotState = RobotState()
        robotState.start()
    except rospy.ROSInterruptException:
        pass
