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

# Utility rule file for r2d2_geneus.

# Include the progress variables for this target.
include r2d2\CMakeFiles\r2d2_geneus.dir\progress.make

r2d2_geneus: r2d2\CMakeFiles\r2d2_geneus.dir\build.make

.PHONY : r2d2_geneus

# Rule to build all files generated by this target.
r2d2\CMakeFiles\r2d2_geneus.dir\build: r2d2_geneus

.PHONY : r2d2\CMakeFiles\r2d2_geneus.dir\build

r2d2\CMakeFiles\r2d2_geneus.dir\clean:
	cd C:\kcl\robotics\ros\catkin_ws\build\r2d2
	$(CMAKE_COMMAND) -P CMakeFiles\r2d2_geneus.dir\cmake_clean.cmake
	cd C:\kcl\robotics\ros\catkin_ws\build
.PHONY : r2d2\CMakeFiles\r2d2_geneus.dir\clean

r2d2\CMakeFiles\r2d2_geneus.dir\depend:
	$(CMAKE_COMMAND) -E cmake_depends "NMake Makefiles" C:\kcl\robotics\ros\catkin_ws\src C:\kcl\robotics\ros\catkin_ws\src\r2d2 C:\kcl\robotics\ros\catkin_ws\build C:\kcl\robotics\ros\catkin_ws\build\r2d2 C:\kcl\robotics\ros\catkin_ws\build\r2d2\CMakeFiles\r2d2_geneus.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : r2d2\CMakeFiles\r2d2_geneus.dir\depend
