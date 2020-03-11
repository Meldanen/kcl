@echo off

if DEFINED DESTDIR (
  echo "Destdir.............%DESTDIR%"
  set DESTDIR_ARG="--root=%DESTDIR%"
)

cd "C:/kcl/robotics/ros/catkin_ws/src/universal_robot/ur_driver"

mkdir "C:/kcl/robotics/ros/catkin_ws/install\lib/site-packages"

set "PYTHONPATH=C:/kcl/robotics/ros/catkin_ws/install\lib/site-packages;C:/kcl/robotics/ros/catkin_ws/build\lib/site-packages"
set "CATKIN_BINARY_DIR=C:/kcl/robotics/ros/catkin_ws/build"
"C:/opt/python27amd64/python.exe" ^
    "C:/kcl/robotics/ros/catkin_ws/src/universal_robot/ur_driver\setup.py" ^
    build --build-base "C:/kcl/robotics/ros/catkin_ws/build/universal_robot/ur_driver" ^
    install %DESTDIR_ARG%  ^
    --prefix="C:\kcl\robotics\ros\catkin_ws\install" ^
    --install-scripts="C:\kcl\robotics\ros\catkin_ws\install\bin"
