# Install script for directory: C:/kcl/robotics/ros/catkin_ws/src/joint_state_publisher/joint_state_publisher_gui

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/kcl/robotics/ros/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "RelWithDebInfo")
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

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "C:/kcl/robotics/ros/catkin_ws/build/joint_state_publisher/joint_state_publisher_gui/catkin_generated/installspace/joint_state_publisher_gui.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/joint_state_publisher_gui/cmake" TYPE FILE FILES
    "C:/kcl/robotics/ros/catkin_ws/build/joint_state_publisher/joint_state_publisher_gui/catkin_generated/installspace/joint_state_publisher_guiConfig.cmake"
    "C:/kcl/robotics/ros/catkin_ws/build/joint_state_publisher/joint_state_publisher_gui/catkin_generated/installspace/joint_state_publisher_guiConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/joint_state_publisher_gui" TYPE FILE FILES "C:/kcl/robotics/ros/catkin_ws/src/joint_state_publisher/joint_state_publisher_gui/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  include("C:/kcl/robotics/ros/catkin_ws/build/joint_state_publisher/joint_state_publisher_gui/catkin_generated/safe_execute_install.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/joint_state_publisher_gui" TYPE PROGRAM FILES "C:/kcl/robotics/ros/catkin_ws/build/joint_state_publisher/joint_state_publisher_gui/catkin_generated/installspace/joint_state_publisher_gui")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/joint_state_publisher_gui" TYPE EXECUTABLE FILES "C:/kcl/robotics/ros/catkin_ws/build/joint_state_publisher/joint_state_publisher_gui/catkin_generated/windows_wrappers/joint_state_publisher_gui_executable_install_python/joint_state_publisher_gui.exe")
endif()

