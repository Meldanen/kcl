#!/usr/bin/env python
import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from moveit_commander.conversions import pose_to_list
from ros_igtl_bridge.msg import igtlpoint
from ros_igtl_bridge.msg import igtltransform


class SlicerToRos():

    def cbPoint(self, data):
        rospy.loginfo(rospy.get_caller_id() + " Goal = (%f, %f, %f).", data.pointdata.x, data.pointdata.y,
                      data.pointdata.z)
        self.moveToGoal(data.pointdata.x, data.pointdata.y, data.pointdata.z)

    def moveToGoal(self, x, y, z):
        moveGroup = self.moveGroup

        # Set pose
        poseG = geometry_msgs.msg.Pose()
        poseG.position.x = x / 1000.0
        poseG.position.y = y / 1000.0
        poseG.position.z = z / 1000.0
        moveGroup.set_pose_target(poseG)

        # Execute plan
        plan = moveGroup.go(wait=True)

        # call stop() and clear for stability
        moveGroup.stop()
        moveGroup.clear_pose_targets()

        currentPose = moveGroup.get_current_pose().pose
        return self.allClose(poseG, currentPose, 0.01)

    def allClose(self, goal, actual, tolerance):
        if type(goal) is list:
            for index in range(len(goal)):
                if abs(actual[index] - goal[index]) > tolerance:
                    return False

        elif type(goal) is geometry_msgs.msg.PoseStamped:
            return self.allClose(goal.pose, actual.pose, tolerance)

        elif type(goal) is geometry_msgs.msg.Pose:
            return self.allClose(pose_to_list(goal), pose_to_list(actual), tolerance)

        return True

    def importer(self):

        global pubIgtlTransformOut

        pubIgtlTransformOut = rospy.Publisher('IGTL_TRANSFORM_OUT', igtltransform, queue_size=10)
        rospy.init_node('igtl_importer', anonymous=True)
        rospy.Subscriber("IGTL_POINT_IN", igtlpoint, self.cbPoint)

        ## First initialize and instantiate moveit_commander
        moveit_commander.roscpp_initialize(sys.argv)
        robot = moveit_commander.RobotCommander()

        ## Instantiate a PlanningSceneInterface_object to help us navigate the robot
        scene = moveit_commander.PlanningSceneInterface()

        ## Instantiate a MoveGroupCommander_ object. This helps us plan and execute movements
        groupName = "panda_arm"
        moveGroup = moveit_commander.MoveGroupCommander(groupName)

        ## To display the trajectory of the robot in rviz
        trajectoryPublisher = rospy.Publisher('/move_group/display_planned_path',
                                              moveit_msgs.msg.DisplayTrajectory,
                                              queue_size=20)

        self.robot = robot
        self.scene = scene
        self.moveGroup = moveGroup
        self.trajectoryPublisher = trajectoryPublisher

        rospy.spin()


if __name__ == '__main__':
    jsp = SlicerToRos()
    jsp.importer()
