execute_process(COMMAND "C:/kcl/robotics/ros/catkin_ws/build/universal_robot/ur_driver/catkin_generated/python_distutils_install.bat" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(C:/kcl/robotics/ros/catkin_ws/build/universal_robot/ur_driver/catkin_generated/python_distutils_install.bat) returned error code ")
endif()
