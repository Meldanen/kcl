#!/usr/bin/env python3

import rospy
from basic_robot.msg import instructionsMessage
from Message import Message
from NodeTypeEnum import NodeTypeEnum
from MovementModeEnum import Utils as MovementModeUtils


class RobotModelClient:

    def __init__(self):
        rospy.init_node(NodeTypeEnum.BASIC_ROBOT_MODEL_CLIENT.value, anonymous=True)
        self.publisher = rospy.Publisher(NodeTypeEnum.TWO_WAY_COMMUNICATION_CHATTER.value, instructionsMessage,
                                         queue_size=1)
        self.message = Message()

    def start(self):
        while not rospy.is_shutdown():
            self.message.clearMessage()
            mode = self.getInput(
                "Type 1 to set joint angles directly or type 2 to set the end effector's position: ")
            modeEnum = MovementModeUtils.getEnumFromId(mode)
            self.message.setMode(modeEnum.getLabel)
            if self.message.isUsingJointPosition():
                joint1 = self.getInput("First joint (in radians): ")
                joint2 = self.getInput("Second joint (in radians): ")
                self.message.setJoint1(joint1)
                self.message.setJoint2(joint2)
                print("Valid input. Waiting for server reply...")
            elif self.message.isUsingEndEffectorPosition():
                x = self.getInput("x (valid values between -1 and 1): ")
                y = self.getInput("y (valid values between -1 and 1): ")
                z = self.getInput("z (valid values between -0.4 and 1.6): ")
                self.message.setX(x)
                self.message.setY(y)
                self.message.setZ(z)
                print("Valid input. Waiting for server reply...")
            else:
                print("Invalid input. Please type either 1 (to set joint angles) or 2 (set end the end effector)")
            rospy.loginfo(self.message.getRosMessage())
            self.publisher.publish(self.message.getRosMessage())
            response = rospy.wait_for_message(NodeTypeEnum.TWO_WAY_COMMUNICATION_CHATTER.value, instructionsMessage)
            rospy.loginfo(response)
            print("\n \n")

    @staticmethod
    def callback(data):
        rospy.loginfo(data)

    @staticmethod
    def getInput(message):
        while True:
            value = input(message)
            try:
                answer = int(value)
                break
            except ValueError:
                try:
                    answer = float(value)
                    break
                except ValueError:
                    print("Input must be numeric.")
        return answer


if __name__ == '__main__':
    try:
        robotModelClient = RobotModelClient()
        robotModelClient.start()
    except rospy.ROSInterruptException:
        pass
