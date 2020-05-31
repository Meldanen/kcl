# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "ros_igtl_bridge: 7 messages, 0 services")

set(MSG_I_FLAGS "-Iros_igtl_bridge:/home/pww/ros_test/src/ROS-IGTL-Bridge/msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/melodic/share/sensor_msgs/cmake/../msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(ros_igtl_bridge_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtltransform.msg" NAME_WE)
add_custom_target(_ros_igtl_bridge_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ros_igtl_bridge" "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtltransform.msg" "geometry_msgs/Transform:geometry_msgs/Quaternion:geometry_msgs/Vector3"
)

get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpointcloud.msg" NAME_WE)
add_custom_target(_ros_igtl_bridge_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ros_igtl_bridge" "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpointcloud.msg" "geometry_msgs/Point"
)

get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpoint.msg" NAME_WE)
add_custom_target(_ros_igtl_bridge_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ros_igtl_bridge" "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpoint.msg" "geometry_msgs/Point"
)

get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlimage.msg" NAME_WE)
add_custom_target(_ros_igtl_bridge_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ros_igtl_bridge" "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlimage.msg" ""
)

get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpolydata.msg" NAME_WE)
add_custom_target(_ros_igtl_bridge_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ros_igtl_bridge" "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpolydata.msg" "ros_igtl_bridge/vector:geometry_msgs/Point32"
)

get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/vector.msg" NAME_WE)
add_custom_target(_ros_igtl_bridge_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ros_igtl_bridge" "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/vector.msg" ""
)

get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlstring.msg" NAME_WE)
add_custom_target(_ros_igtl_bridge_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ros_igtl_bridge" "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlstring.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtltransform.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_cpp(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpointcloud.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_cpp(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpoint.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_cpp(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlimage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_cpp(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpolydata.msg"
  "${MSG_I_FLAGS}"
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/vector.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point32.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_cpp(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/vector.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_cpp(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlstring.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_igtl_bridge
)

### Generating Services

### Generating Module File
_generate_module_cpp(ros_igtl_bridge
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_igtl_bridge
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(ros_igtl_bridge_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(ros_igtl_bridge_generate_messages ros_igtl_bridge_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtltransform.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_cpp _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpointcloud.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_cpp _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpoint.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_cpp _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlimage.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_cpp _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpolydata.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_cpp _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/vector.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_cpp _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlstring.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_cpp _ros_igtl_bridge_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ros_igtl_bridge_gencpp)
add_dependencies(ros_igtl_bridge_gencpp ros_igtl_bridge_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ros_igtl_bridge_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtltransform.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_eus(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpointcloud.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_eus(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpoint.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_eus(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlimage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_eus(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpolydata.msg"
  "${MSG_I_FLAGS}"
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/vector.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point32.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_eus(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/vector.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_eus(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlstring.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_igtl_bridge
)

### Generating Services

### Generating Module File
_generate_module_eus(ros_igtl_bridge
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_igtl_bridge
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(ros_igtl_bridge_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(ros_igtl_bridge_generate_messages ros_igtl_bridge_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtltransform.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_eus _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpointcloud.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_eus _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpoint.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_eus _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlimage.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_eus _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpolydata.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_eus _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/vector.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_eus _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlstring.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_eus _ros_igtl_bridge_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ros_igtl_bridge_geneus)
add_dependencies(ros_igtl_bridge_geneus ros_igtl_bridge_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ros_igtl_bridge_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtltransform.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_lisp(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpointcloud.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_lisp(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpoint.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_lisp(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlimage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_lisp(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpolydata.msg"
  "${MSG_I_FLAGS}"
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/vector.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point32.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_lisp(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/vector.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_lisp(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlstring.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_igtl_bridge
)

### Generating Services

### Generating Module File
_generate_module_lisp(ros_igtl_bridge
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_igtl_bridge
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(ros_igtl_bridge_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(ros_igtl_bridge_generate_messages ros_igtl_bridge_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtltransform.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_lisp _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpointcloud.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_lisp _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpoint.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_lisp _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlimage.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_lisp _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpolydata.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_lisp _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/vector.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_lisp _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlstring.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_lisp _ros_igtl_bridge_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ros_igtl_bridge_genlisp)
add_dependencies(ros_igtl_bridge_genlisp ros_igtl_bridge_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ros_igtl_bridge_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtltransform.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_nodejs(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpointcloud.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_nodejs(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpoint.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_nodejs(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlimage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_nodejs(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpolydata.msg"
  "${MSG_I_FLAGS}"
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/vector.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point32.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_nodejs(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/vector.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_nodejs(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlstring.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_igtl_bridge
)

### Generating Services

### Generating Module File
_generate_module_nodejs(ros_igtl_bridge
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_igtl_bridge
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(ros_igtl_bridge_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(ros_igtl_bridge_generate_messages ros_igtl_bridge_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtltransform.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_nodejs _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpointcloud.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_nodejs _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpoint.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_nodejs _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlimage.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_nodejs _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpolydata.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_nodejs _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/vector.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_nodejs _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlstring.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_nodejs _ros_igtl_bridge_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ros_igtl_bridge_gennodejs)
add_dependencies(ros_igtl_bridge_gennodejs ros_igtl_bridge_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ros_igtl_bridge_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtltransform.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_py(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpointcloud.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_py(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpoint.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_py(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlimage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_py(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpolydata.msg"
  "${MSG_I_FLAGS}"
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/vector.msg;/opt/ros/melodic/share/geometry_msgs/cmake/../msg/Point32.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_py(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/vector.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_igtl_bridge
)
_generate_msg_py(ros_igtl_bridge
  "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlstring.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_igtl_bridge
)

### Generating Services

### Generating Module File
_generate_module_py(ros_igtl_bridge
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_igtl_bridge
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(ros_igtl_bridge_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(ros_igtl_bridge_generate_messages ros_igtl_bridge_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtltransform.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_py _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpointcloud.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_py _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpoint.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_py _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlimage.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_py _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlpolydata.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_py _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/vector.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_py _ros_igtl_bridge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pww/ros_test/src/ROS-IGTL-Bridge/msg/igtlstring.msg" NAME_WE)
add_dependencies(ros_igtl_bridge_generate_messages_py _ros_igtl_bridge_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ros_igtl_bridge_genpy)
add_dependencies(ros_igtl_bridge_genpy ros_igtl_bridge_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ros_igtl_bridge_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_igtl_bridge)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_igtl_bridge
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(ros_igtl_bridge_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET sensor_msgs_generate_messages_cpp)
  add_dependencies(ros_igtl_bridge_generate_messages_cpp sensor_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(ros_igtl_bridge_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_igtl_bridge)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_igtl_bridge
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(ros_igtl_bridge_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET sensor_msgs_generate_messages_eus)
  add_dependencies(ros_igtl_bridge_generate_messages_eus sensor_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(ros_igtl_bridge_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_igtl_bridge)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_igtl_bridge
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(ros_igtl_bridge_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET sensor_msgs_generate_messages_lisp)
  add_dependencies(ros_igtl_bridge_generate_messages_lisp sensor_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(ros_igtl_bridge_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_igtl_bridge)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_igtl_bridge
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(ros_igtl_bridge_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET sensor_msgs_generate_messages_nodejs)
  add_dependencies(ros_igtl_bridge_generate_messages_nodejs sensor_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(ros_igtl_bridge_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_igtl_bridge)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_igtl_bridge\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_igtl_bridge
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(ros_igtl_bridge_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET sensor_msgs_generate_messages_py)
  add_dependencies(ros_igtl_bridge_generate_messages_py sensor_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(ros_igtl_bridge_generate_messages_py std_msgs_generate_messages_py)
endif()
