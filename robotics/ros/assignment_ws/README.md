# Running the robot model

### 1. Setup
The model path specified in <workspace>/launch/display.launch is hardcoded as I run into some issues using relative paths on windows. Using relative paths is okay if you are on Linux.

### 2. In a new terminal (in the appropriate directory)

```
roslaunch basic_robot display.launch
```
### 3. In a new terminal (in the appropriate directory)

```
rosrun basic_robot src/BasicRobotModelClient
```
