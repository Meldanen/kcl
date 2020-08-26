# Running the robot model

### 1. Setup
The model path specified in <workspace>/launch/display.launch is hardcoded as I run into some issues using relative paths on windows.

### 2. In a new terminal (in the appropriate directory)

```
roslaunch basic_robot display.launch
```
### 3. In a new terminal (in the appropriate directory)

```
rosrun basic_robot src/BasicRobotModelClient
```
