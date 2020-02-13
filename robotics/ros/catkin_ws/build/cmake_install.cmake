<<<<<<< HEAD
# Install script for directory: C:/kcl/robotics/ros/catkin_ws/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/kcl/robotics/ros/catkin_ws/install")
=======
# Install script for directory: /home/mikroszolos/catkin_ws/src

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
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
<<<<<<< HEAD
   "C:/kcl/robotics/ros/catkin_ws/install/_setup_util.py")
=======
   "/home/mikroszolos/catkin_ws/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/mikroszolos/catkin_ws/install" TYPE PROGRAM FILES "/home/mikroszolos/catkin_ws/build/catkin_generated/installspace/_setup_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/mikroszolos/catkin_ws/install/env.sh")
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
<<<<<<< HEAD
file(INSTALL DESTINATION "C:/kcl/robotics/ros/catkin_ws/install" TYPE PROGRAM FILES "C:/kcl/robotics/ros/catkin_ws/build/catkin_generated/installspace/_setup_util.py")
=======
file(INSTALL DESTINATION "/home/mikroszolos/catkin_ws/install" TYPE PROGRAM FILES "/home/mikroszolos/catkin_ws/build/catkin_generated/installspace/env.sh")
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
<<<<<<< HEAD
   "C:/kcl/robotics/ros/catkin_ws/install/_setup_util.py.exe")
=======
   "/home/mikroszolos/catkin_ws/install/setup.bash;/home/mikroszolos/catkin_ws/install/local_setup.bash")
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
<<<<<<< HEAD
file(INSTALL DESTINATION "C:/kcl/robotics/ros/catkin_ws/install" TYPE EXECUTABLE FILES "C:/kcl/robotics/ros/catkin_ws/build/catkin_generated/windows_wrappers/_setup_util.py_executable_install_python/_setup_util.py.exe")
=======
file(INSTALL DESTINATION "/home/mikroszolos/catkin_ws/install" TYPE FILE FILES
    "/home/mikroszolos/catkin_ws/build/catkin_generated/installspace/setup.bash"
    "/home/mikroszolos/catkin_ws/build/catkin_generated/installspace/local_setup.bash"
    )
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
<<<<<<< HEAD
   "C:/kcl/robotics/ros/catkin_ws/install/env.bat")
=======
   "/home/mikroszolos/catkin_ws/install/setup.sh;/home/mikroszolos/catkin_ws/install/local_setup.sh")
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
<<<<<<< HEAD
file(INSTALL DESTINATION "C:/kcl/robotics/ros/catkin_ws/install" TYPE PROGRAM FILES "C:/kcl/robotics/ros/catkin_ws/build/catkin_generated/installspace/env.bat")
=======
file(INSTALL DESTINATION "/home/mikroszolos/catkin_ws/install" TYPE FILE FILES
    "/home/mikroszolos/catkin_ws/build/catkin_generated/installspace/setup.sh"
    "/home/mikroszolos/catkin_ws/build/catkin_generated/installspace/local_setup.sh"
    )
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
<<<<<<< HEAD
   "C:/kcl/robotics/ros/catkin_ws/install/setup.bat;C:/kcl/robotics/ros/catkin_ws/install/local_setup.bat")
=======
   "/home/mikroszolos/catkin_ws/install/setup.zsh;/home/mikroszolos/catkin_ws/install/local_setup.zsh")
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
<<<<<<< HEAD
file(INSTALL DESTINATION "C:/kcl/robotics/ros/catkin_ws/install" TYPE FILE FILES
    "C:/kcl/robotics/ros/catkin_ws/build/catkin_generated/installspace/setup.bat"
    "C:/kcl/robotics/ros/catkin_ws/build/catkin_generated/installspace/local_setup.bat"
=======
file(INSTALL DESTINATION "/home/mikroszolos/catkin_ws/install" TYPE FILE FILES
    "/home/mikroszolos/catkin_ws/build/catkin_generated/installspace/setup.zsh"
    "/home/mikroszolos/catkin_ws/build/catkin_generated/installspace/local_setup.zsh"
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
<<<<<<< HEAD
   "C:/kcl/robotics/ros/catkin_ws/install/.rosinstall")
=======
   "/home/mikroszolos/catkin_ws/install/.rosinstall")
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
<<<<<<< HEAD
file(INSTALL DESTINATION "C:/kcl/robotics/ros/catkin_ws/install" TYPE FILE FILES "C:/kcl/robotics/ros/catkin_ws/build/catkin_generated/installspace/.rosinstall")
=======
file(INSTALL DESTINATION "/home/mikroszolos/catkin_ws/install" TYPE FILE FILES "/home/mikroszolos/catkin_ws/build/catkin_generated/installspace/.rosinstall")
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
<<<<<<< HEAD
  include("C:/kcl/robotics/ros/catkin_ws/build/joint_state_publisher/joint_state_publisher_gui/cmake_install.cmake")
  include("C:/kcl/robotics/ros/catkin_ws/build/urdf_parser_py/cmake_install.cmake")
  include("C:/kcl/robotics/ros/catkin_ws/build/beginner_tutorials/cmake_install.cmake")
  include("C:/kcl/robotics/ros/catkin_ws/build/joint_state_publisher/joint_state_publisher/cmake_install.cmake")
  include("C:/kcl/robotics/ros/catkin_ws/build/r2d2/cmake_install.cmake")
  include("C:/kcl/robotics/ros/catkin_ws/build/learning_tf/cmake_install.cmake")
  include("C:/kcl/robotics/ros/catkin_ws/build/turtlesim_cleaner/cmake_install.cmake")
  include("C:/kcl/robotics/ros/catkin_ws/build/testbot_description/cmake_install.cmake")
  include("C:/kcl/robotics/ros/catkin_ws/build/urdf_tutorial/cmake_install.cmake")
=======
  include("/home/mikroszolos/catkin_ws/build/gtest/cmake_install.cmake")
  include("/home/mikroszolos/catkin_ws/build/turtlesim_cleaner/cmake_install.cmake")
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
<<<<<<< HEAD
file(WRITE "C:/kcl/robotics/ros/catkin_ws/build/${CMAKE_INSTALL_MANIFEST}"
=======
file(WRITE "/home/mikroszolos/catkin_ws/build/${CMAKE_INSTALL_MANIFEST}"
>>>>>>> 3dea7c5d8e72392238c46d905c351dcfde7f3140
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
