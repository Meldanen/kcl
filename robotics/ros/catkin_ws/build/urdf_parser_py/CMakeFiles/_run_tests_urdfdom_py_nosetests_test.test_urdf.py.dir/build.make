# CMAKE generated file: DO NOT EDIT!
# Generated by "NMake Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

!IF "$(OS)" == "Windows_NT"
NULL=
!ELSE
NULL=nul
!ENDIF
SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = C:\opt\python27amd64\Lib\site-packages\cmake\data\bin\cmake.exe

# The command to remove a file.
RM = C:\opt\python27amd64\Lib\site-packages\cmake\data\bin\cmake.exe -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\kcl\robotics\ros\catkin_ws\src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\kcl\robotics\ros\catkin_ws\build

# Utility rule file for _run_tests_urdfdom_py_nosetests_test.test_urdf.py.

# Include the progress variables for this target.
include urdf_parser_py\CMakeFiles\_run_tests_urdfdom_py_nosetests_test.test_urdf.py.dir\progress.make

urdf_parser_py\CMakeFiles\_run_tests_urdfdom_py_nosetests_test.test_urdf.py:
	cd C:\kcl\robotics\ros\catkin_ws\build\urdf_parser_py
	call ..\catkin_generated\env_cached.bat C:/opt/python27amd64/python.exe C:/opt/ros/melodic/x64/share/catkin/cmake/test/run_tests.py C:/kcl/robotics/ros/catkin_ws/build/test_results/urdfdom_py/nosetests-test.test_urdf.py.xml "\"C:/opt/python27amd64/Lib/site-packages/cmake/data/bin/cmake.exe\" -E make_directory C:/kcl/robotics/ros/catkin_ws/build/test_results/urdfdom_py" "C:/opt/python27amd64/Scripts/nosetests-2.7.exe -P --process-timeout=60 C:/kcl/robotics/ros/catkin_ws/src/urdf_parser_py/test/test_urdf.py --with-xunit --xunit-file=C:/kcl/robotics/ros/catkin_ws/build/test_results/urdfdom_py/nosetests-test.test_urdf.py.xml"
	cd C:\kcl\robotics\ros\catkin_ws\build

_run_tests_urdfdom_py_nosetests_test.test_urdf.py: urdf_parser_py\CMakeFiles\_run_tests_urdfdom_py_nosetests_test.test_urdf.py
_run_tests_urdfdom_py_nosetests_test.test_urdf.py: urdf_parser_py\CMakeFiles\_run_tests_urdfdom_py_nosetests_test.test_urdf.py.dir\build.make

.PHONY : _run_tests_urdfdom_py_nosetests_test.test_urdf.py

# Rule to build all files generated by this target.
urdf_parser_py\CMakeFiles\_run_tests_urdfdom_py_nosetests_test.test_urdf.py.dir\build: _run_tests_urdfdom_py_nosetests_test.test_urdf.py

.PHONY : urdf_parser_py\CMakeFiles\_run_tests_urdfdom_py_nosetests_test.test_urdf.py.dir\build

urdf_parser_py\CMakeFiles\_run_tests_urdfdom_py_nosetests_test.test_urdf.py.dir\clean:
	cd C:\kcl\robotics\ros\catkin_ws\build\urdf_parser_py
	$(CMAKE_COMMAND) -P CMakeFiles\_run_tests_urdfdom_py_nosetests_test.test_urdf.py.dir\cmake_clean.cmake
	cd C:\kcl\robotics\ros\catkin_ws\build
.PHONY : urdf_parser_py\CMakeFiles\_run_tests_urdfdom_py_nosetests_test.test_urdf.py.dir\clean

urdf_parser_py\CMakeFiles\_run_tests_urdfdom_py_nosetests_test.test_urdf.py.dir\depend:
	$(CMAKE_COMMAND) -E cmake_depends "NMake Makefiles" C:\kcl\robotics\ros\catkin_ws\src C:\kcl\robotics\ros\catkin_ws\src\urdf_parser_py C:\kcl\robotics\ros\catkin_ws\build C:\kcl\robotics\ros\catkin_ws\build\urdf_parser_py C:\kcl\robotics\ros\catkin_ws\build\urdf_parser_py\CMakeFiles\_run_tests_urdfdom_py_nosetests_test.test_urdf.py.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : urdf_parser_py\CMakeFiles\_run_tests_urdfdom_py_nosetests_test.test_urdf.py.dir\depend

