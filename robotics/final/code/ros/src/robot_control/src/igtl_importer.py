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

        if data.name == 'Entry':
            rospy.loginfo(rospy.get_caller_id() + " Entry = (%f, %f, %f).", data.pointdata.x, data.pointdata.y, data.pointdata.z)
            self.go_to_pose_goal(data.pointdata.x,data.pointdata.y,data.pointdata.z)
        elif data.name == 'Target':
            rospy.loginfo(rospy.get_caller_id() + " Target = (%f, %f, %f).", data.pointdata.x, data.pointdata.y, data.pointdata.z)
            self.plan_cartesian_path(data.pointdata.x,data.pointdata.y,data.pointdata.z)
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

    def plan_cartesian_path(self,x,y,z, scale=10):
        # Copy class variables to local variables to make the web tutorials more clear.
        # In practice, you should use the class variables directly unless you have a good
        # reason not to.
        move_group = self.move_group

        ## BEGIN_SUB_TUTORIAL plan_cartesian_path
        ##
        ## Cartesian Paths
        ## ^^^^^^^^^^^^^^^
        ## You can plan a Cartesian path directly by specifying a list of waypoints
        ## for the end-effector to go through. If executing  interactively in a
        ## Python shell, set scale = 1.0.
        ##
        waypoints = []
	wpose = move_group.get_current_pose().pose
	xTarget = wpose.position.x
	yTarget = wpose.position.y
	zTarget = wpose.position.z
	xEntry = x/1000.0
	yEntry = y/1000.0
	zEntry = z/1000.0
	for step in range(scale):
		xEnd = xEntry + (step/scale)*(xTarget-xEntry)
		yEnd = yEntry + (step/scale)*(yTarget-yEntry)
		zEnd = zEntry + (step/scale)*(zTarget-zEntry)
        	wpose.position.x = xEnd
        	wpose.position.y = yEnd
		wpose.position.z = zEnd
		rospy.loginfo(wpose)
        	waypoints.append(copy.deepcopy(wpose))


        # We want the Cartsesian path to be interpolated at a resolution of 1 cm
        # which is why we will specify 0.01 as the eef_step in Cartesian
        # translation.  We will disable the jump threshold by setting it to 0.0,
        # ignoring the check for infeasible jumps in joint space, which is sufficient
        # for this tutorial.
        (plan, fraction) = move_group.compute_cartesian_path(
                                           waypoints,   # waypoints to follow
                                           0.01,        # eef_step
                                           0.0)         # jump_threshold

        # Note: We are just planning, not asking move_group to actually move the robot yet:
        self.display_trajectory(plan)
        self.execute_plan(plan)
        return plan, fraction

        ## END_SUB_TUTORIAL


    def display_trajectory(self, plan):
        # Copy class variables to local variables to make the web tutorials more clear.
        # In practice, you should use the class variables directly unless you have a good
        # reason not to.
        robot = self.robot
        display_trajectory_publisher = self.display_trajectory_publisher

        ## BEGIN_SUB_TUTORIAL display_trajectory
        ##
        ## Displaying a Trajectory
        ## ^^^^^^^^^^^^^^^^^^^^^^^
        ## You can ask RViz to visualize a plan (aka trajectory) for you. But the
        ## group.plan() method does this automatically so this is not that useful
        ## here (it just displays the same trajectory again):
        ##
        ## A `DisplayTrajectory`_ msg has two primary fields, trajectory_start and trajectory.
        ## We populate the trajectory_start with our current robot state to copy over
        ## any AttachedCollisionObjects and add our plan to the trajectory.
        display_trajectory = moveit_msgs.msg.DisplayTrajectory()
        display_trajectory.trajectory_start = robot.get_current_state()
        display_trajectory.trajectory.append(plan)
        # Publish
        display_trajectory_publisher.publish(display_trajectory);

        ## END_SUB_TUTORIAL


    def execute_plan(self, plan):
        # Copy class variables to local variables to make the web tutorials more clear.
        # In practice, you should use the class variables directly unless you have a good
        # reason not to.
        move_group = self.move_group

        ## BEGIN_SUB_TUTORIAL execute_plan
        ##
        ## Executing a Plan
        ## ^^^^^^^^^^^^^^^^
        ## Use execute if you would like the robot to follow
        ## the plan that has already been computed:
        move_group.execute(plan, wait=True)

        ## **Note:** The robot's current joint state must be within some tolerance of the
        ## first waypoint in the `RobotTrajectory`_ or ``execute()`` will fail
        ## END_SUB_TUTORIAL


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
