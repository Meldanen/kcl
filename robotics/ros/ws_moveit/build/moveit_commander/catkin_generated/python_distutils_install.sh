#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/mikroszolos/kcl/robotics/ros/ws_moveit/src/moveit/moveit_commander"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/mikroszolos/kcl/robotics/ros/ws_moveit/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/mikroszolos/kcl/robotics/ros/ws_moveit/install/lib/python2.7/dist-packages:/home/mikroszolos/kcl/robotics/ros/ws_moveit/build/moveit_commander/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/mikroszolos/kcl/robotics/ros/ws_moveit/build/moveit_commander" \
    "/usr/bin/python2" \
    "/home/mikroszolos/kcl/robotics/ros/ws_moveit/src/moveit/moveit_commander/setup.py" \
    build --build-base "/home/mikroszolos/kcl/robotics/ros/ws_moveit/build/moveit_commander" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/mikroszolos/kcl/robotics/ros/ws_moveit/install" --install-scripts="/home/mikroszolos/kcl/robotics/ros/ws_moveit/install/bin"
