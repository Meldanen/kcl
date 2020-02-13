execute_process(COMMAND "C:/kcl/robotics/ros/catkin_ws/build/urdf_parser_py/catkin_generated/python_distutils_install.bat" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(C:/kcl/robotics/ros/catkin_ws/build/urdf_parser_py/catkin_generated/python_distutils_install.bat) returned error code ")
endif()
