# How to use:

## Initialise the connection between ROS and Slicer 4.8.1:
### Slicer Part
1.	Launch Slicer 4.8.1
2.	Go to your favourite IGTLink extension (SlicerIGT in this case)
3.	Create a connection with Slicer as the server on port 18944
### ROS Part
1.	Start the VM with the network adapter attached to NAT
2.	Launch the bridge file of the ros_igtl_bridge 
3.	Choose to run as client
4.	Set IP to 10.0.2.2
5.	Set port to 18944


## Then to plan and execute:
### Step 1:
1.	In Slicer 4.8.1
2.	Go to Markups
3.	Create a new MarkupFiducials called “Goal”
4.	Place a point in the workspace (I did this the other way around. I manually moved the robot in RVIZ and those coordinates instead)
Or simply use the provided scene “SlicerToRos” found in <directory>/Scenes
### Step 2:
1.	Launch a new terminal
2.	Go to your workspace and source it
3.	Enter “roslaunch panda_moveit_config demo.launch”
### Step 3:
4.	Launch a new terminal
5.	Go to your workspace and source it
6.	Enter “rosrun robot_control slicerToRos.py”
### Step 4:
1.	Go back to slicer
2.	Go to IGT -> IGTLinkIF
3.	Scroll down to I/O Configuration
4.	Click on either “Goal1” or “Goal2” (if you used the supplied scene)
5.	Click send (as seen here Figure 6: Slicer Scene)
If you now look at RVIZ, the robot should now be moving.
