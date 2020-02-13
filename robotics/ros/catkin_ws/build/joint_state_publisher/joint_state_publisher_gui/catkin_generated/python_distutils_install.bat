@echo off

if DEFINED DESTDIR (
  echo "Destdir.............%DESTDIR%"
  set DESTDIR_ARG="--root=%DESTDIR%"
)

cd "C:/kcl/robotics/ros/catkin_ws/src/joint_state_publisher/joint_state_publisher_gui"

mkdir "C:/kcl/robotics/ros/catkin_ws/install\lib/site-packages"

set "PYTHONPATH=C:/kcl/robotics/ros/catkin_ws/install\lib/site-packages;C:/kcl/robotics/ros/catkin_ws/build\lib/site-packages"
set "CATKIN_BINARY_DIR=C:/kcl/robotics/ros/catkin_ws/build"
"C:/opt/python27amd64/python.exe" ^
    "C:/kcl/robotics/ros/catkin_ws/src/joint_state_publisher/joint_state_publisher_gui\setup.py" ^
    build --build-base "C:/kcl/robotics/ros/catkin_ws/build/joint_state_publisher/joint_state_publisher_gui" ^
    install %DESTDIR_ARG%  ^
    --prefix="C:\kcl\robotics\ros\catkin_ws\install" ^
    --install-scripts="C:\kcl\robotics\ros\catkin_ws\install\bin"
