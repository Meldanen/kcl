# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
<<<<<<< HEAD
if os.path.exists(os.path.join('C:/opt/ros/melodic/x64/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('C:/opt/ros/melodic/x64/share/catkin/cmake', '..', 'python'))
=======
if os.path.exists(os.path.join('/opt/ros/melodic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/melodic/share/catkin/cmake', '..', 'python'))
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
<<<<<<< HEAD
    for workspace in "C:/kcl/robotics/ros/catkin_ws/devel;C:/opt/ros/melodic/x64".split(';'):
        python_path = os.path.join(workspace, 'lib/site-packages')
=======
    for workspace in "/home/mikroszolos/catkin_ws/devel;/opt/ros/melodic".split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

<<<<<<< HEAD
code = generate_environment_script('C:/kcl/robotics/ros/catkin_ws/devel/env.bat')

output_filename = 'C:/kcl/robotics/ros/catkin_ws/build/catkin_generated/setup_cached.bat'
=======
code = generate_environment_script('/home/mikroszolos/catkin_ws/devel/env.sh')

output_filename = '/home/mikroszolos/catkin_ws/build/catkin_generated/setup_cached.sh'
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
with open(output_filename, 'w') as f:
    #print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
