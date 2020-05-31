# How to use:

## Initialise the connection between ROS and Slicer 4.8.1:
###Setting up the connection
###Slicer Part
1.	Launch Slicer 4.8.1
2.	Go to your favourite IGTLink extension (SlicerIGT in this case)
3.	Create a connection with Slicer as the server on port 18944
###ROS Part
1.	Start the VM (if using one. I run this on Ubuntu, so it was not required) with the ap-propriate configuration for two-way communication
2.	Launch the bridge file of the ros_igtl_bridge 
3.	Choose to run as client
4.	Set IP to the appropriate IP found by writing “ifconfig” in your terminal
5.	Set port to 18944

A connection should be now established.

###Sending data from Slicer to ROS
###Step 1:
1.	In Slicer 4.8.1
2.	Go to Markups
3.	Create a new MarkupFiducials called “Entry” and/or “Target”
4.	Place a point in the workspace (I did this the other way around. I manually moved the robot in RVIZ and those coordinates instead)
###Step 2:
1.	Launch a new terminal
2.	Go to your workspace and source it
3.	Enter “roslaunch ismr19_moveit demo.launch”
###Step 3:
4.	Launch a new terminal
5.	Go to your workspace and source it
6.	Enter “rosrun robot_control igtl_importer.py”
###Step 4:
1.	Launch a new terminal
2.	Go to your workspace and source it
3.	Enter “rosrun robot_control igtl_exporter.py”
###Step 5:
1.	Go back to slicer
2.	Go to IGT -> IGTLinkIF
3.	Scroll down to I/O Configuration
4.	Click on either “Entry” or “Target” (if you used the supplied scene) and click send
