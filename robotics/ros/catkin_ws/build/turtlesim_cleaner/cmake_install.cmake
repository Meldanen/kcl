<<<<<<< HEAD
# Install script for directory: C:/kcl/robotics/ros/catkin_ws/src/turtlesim_cleaner

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/kcl/robotics/ros/catkin_ws/install")
=======
# Install script for directory: /home/mikroszolos/catkin_ws/src/turtlesim_cleaner

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/mikroszolos/catkin_ws/install")
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
<<<<<<< HEAD
    set(CMAKE_INSTALL_CONFIG_NAME "RelWithDebInfo")
=======
    set(CMAKE_INSTALL_CONFIG_NAME "")
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

<<<<<<< HEAD
=======
# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
<<<<<<< HEAD
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "C:/kcl/robotics/ros/catkin_ws/build/turtlesim_cleaner/catkin_generated/installspace/turtlesim_cleaner.pc")
=======
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/mikroszolos/catkin_ws/build/turtlesim_cleaner/catkin_generated/installspace/turtlesim_cleaner.pc")
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlesim_cleaner/cmake" TYPE FILE FILES
<<<<<<< HEAD
    "C:/kcl/robotics/ros/catkin_ws/build/turtlesim_cleaner/catkin_generated/installspace/turtlesim_cleanerConfig.cmake"
    "C:/kcl/robotics/ros/catkin_ws/build/turtlesim_cleaner/catkin_generated/installspace/turtlesim_cleanerConfig-version.cmake"
=======
    "/home/mikroszolos/catkin_ws/build/turtlesim_cleaner/catkin_generated/installspace/turtlesim_cleanerConfig.cmake"
    "/home/mikroszolos/catkin_ws/build/turtlesim_cleaner/catkin_generated/installspace/turtlesim_cleanerConfig-version.cmake"
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
<<<<<<< HEAD
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlesim_cleaner" TYPE FILE FILES "C:/kcl/robotics/ros/catkin_ws/src/turtlesim_cleaner/package.xml")
=======
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlesim_cleaner" TYPE FILE FILES "/home/mikroszolos/catkin_ws/src/turtlesim_cleaner/package.xml")
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
endif()

