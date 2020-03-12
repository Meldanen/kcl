#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import math
import tf
from math import pi
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import Transform
from std_msgs.msg import String
from ros_igtl_bridge.msg import igtlpoint
from ros_igtl_bridge.msg import igtlstring
from ros_igtl_bridge.msg import igtltransform

class importer():
    def cb_transform(self,data):
        pass

    def cb_point(self,data):

        if data.name == 'Target':
            rospy.loginfo(rospy.get_caller_id() + " Target = (%f, %f, %f).", data.pointdata.x, data.pointdata.y, data.pointdata.z)
        self.go_to_pose_goal(data.pointdata.x,data.pointdata.y,data.pointdata.z)

    def cb_string(self,data):
        pass

    def go_to_pose_goal(self,x,y,z):
        move_group = self.move_group


        pose_goal = geometry_msgs.msg.Pose()
        #pose_goal.orientation.w = 1.0
        pose_goal.position.x = x/1000.0
        pose_goal.position.y = y/1000.0
        pose_goal.position.z = z/1000.0
        print(pose_goal.position.x)
        move_group.set_pose_target(pose_goal)

        ## Now, we call the planner to compute the plan and execute it.
        plan = move_group.go(wait=True)
        # Calling `stop()` ensures that there is no residual movement
        move_group.stop()
        # It is always good to clear your targets after planning with poses.
        # Note: there is no equivalent function for clear_joint_value_targets()
        move_group.clear_pose_targets()

        current_pose = move_group.get_current_pose().pose
        return self.all_close(pose_goal, current_pose, 0.01)

    def all_close(self,goal, actual, tolerance):

      all_equal = True
      if type(goal) is list:
        for index in range(len(goal)):
          if abs(actual[index] - goal[index]) > tolerance:
            return False

      elif type(goal) is geometry_msgs.msg.PoseStamped:
        return all_close(goal.pose, actual.pose, tolerance)

      elif type(goal) is geometry_msgs.msg.Pose:
        return self.all_close(pose_to_list(goal), pose_to_list(actual), tolerance)

      return True

    def igtl_importer(self):

        global pub_igtl_transform_out

        pub_igtl_transform_out = rospy.Publisher('IGTL_TRANSFORM_OUT', igtltransform, queue_size=10)

        # In ROS, nodes are uniquely named. If two nodes with the same
        # node are launched, the previous one is kicked off. The
        # anonymous=True flag means that rospy will choose a unique
        # name for our 'listener' node so that multiple listeners can
        # run simultaneously.
        rospy.init_node('igtl_importer', anonymous=True)

        rospy.Subscriber("IGTL_TRANSFORM_IN", igtltransform, self.cb_transform)
        rospy.Subscriber("IGTL_POINT_IN", igtlpoint, self.cb_point)
        rospy.Subscriber("IGTL_STRING_IN", igtlstring, self.cb_string)
        ## BEGIN_SUB_TUTORIAL setup
        ##
        ## First initialize `moveit_commander`_ and a `rospy`_ node:
        moveit_commander.roscpp_initialize(sys.argv)
        #rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

        ## Instantiate a `RobotCommander`_ object. Provides information such as the robot's
        ## kinematic model and the robot's current joint states
        robot = moveit_commander.RobotCommander()

        ## Instantiate a `PlanningSceneInterface`_ object.  This provides a remote interface
        ## for getting, setting, and updating the robot's internal understanding of the
        ## surrounding world:
        scene = moveit_commander.PlanningSceneInterface()

        ## Instantiate a `MoveGroupCommander`_ object.  This object is an interface
        ## to a planning group (group of joints).  In this tutorial the group is the primary
        ## arm joints in the Panda robot, so we set the group's name to "panda_arm".
        ## If you are using a different robot, change this value to the name of your robot
        ## arm planning group.
        ## This interface can be used to plan and execute motions:
        group_name = "panda_arm"
        move_group = moveit_commander.MoveGroupCommander(group_name)

        ## Create a `DisplayTrajectory`_ ROS publisher which is used to display
        ## trajectories in Rviz:
        display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                       moveit_msgs.msg.DisplayTrajectory,
                                                       queue_size=20)

        # Misc variables
        #self.box_name = ''
        self.robot = robot
        self.scene = scene
        self.move_group = move_group
        self.display_trajectory_publisher = display_trajectory_publisher
        #self.planning_frame = planning_frame
        #self.eef_link = eef_link
        #self.group_names = group_names

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

if __name__ == '__main__':
    jsp = importer()
    jsp.igtl_importer()
