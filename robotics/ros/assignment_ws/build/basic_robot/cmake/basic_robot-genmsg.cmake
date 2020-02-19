# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "basic_robot: 1 messages, 0 services")

set(MSG_I_FLAGS "-Ibasic_robot:C:/kcl/robotics/ros/assignment_ws/src/basic_robot/msg;-Istd_msgs:C:/opt/ros/melodic/x64/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(basic_robot_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "C:/kcl/robotics/ros/assignment_ws/src/basic_robot/msg/instructionsMessage.msg" NAME_WE)
add_custom_target(_basic_robot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "basic_robot" "C:/kcl/robotics/ros/assignment_ws/src/basic_robot/msg/instructionsMessage.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(basic_robot
  "C:/kcl/robotics/ros/assignment_ws/src/basic_robot/msg/instructionsMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/basic_robot
)

### Generating Services

### Generating Module File
_generate_module_cpp(basic_robot
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/basic_robot
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(basic_robot_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(basic_robot_generate_messages basic_robot_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "C:/kcl/robotics/ros/assignment_ws/src/basic_robot/msg/instructionsMessage.msg" NAME_WE)
add_dependencies(basic_robot_generate_messages_cpp _basic_robot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(basic_robot_gencpp)
add_dependencies(basic_robot_gencpp basic_robot_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS basic_robot_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(basic_robot
  "C:/kcl/robotics/ros/assignment_ws/src/basic_robot/msg/instructionsMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/basic_robot
)

### Generating Services

### Generating Module File
_generate_module_eus(basic_robot
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/basic_robot
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(basic_robot_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(basic_robot_generate_messages basic_robot_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "C:/kcl/robotics/ros/assignment_ws/src/basic_robot/msg/instructionsMessage.msg" NAME_WE)
add_dependencies(basic_robot_generate_messages_eus _basic_robot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(basic_robot_geneus)
add_dependencies(basic_robot_geneus basic_robot_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS basic_robot_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(basic_robot
  "C:/kcl/robotics/ros/assignment_ws/src/basic_robot/msg/instructionsMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/basic_robot
)

### Generating Services

### Generating Module File
_generate_module_lisp(basic_robot
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/basic_robot
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(basic_robot_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(basic_robot_generate_messages basic_robot_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "C:/kcl/robotics/ros/assignment_ws/src/basic_robot/msg/instructionsMessage.msg" NAME_WE)
add_dependencies(basic_robot_generate_messages_lisp _basic_robot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(basic_robot_genlisp)
add_dependencies(basic_robot_genlisp basic_robot_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS basic_robot_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(basic_robot
  "C:/kcl/robotics/ros/assignment_ws/src/basic_robot/msg/instructionsMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/basic_robot
)

### Generating Services

### Generating Module File
_generate_module_nodejs(basic_robot
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/basic_robot
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(basic_robot_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(basic_robot_generate_messages basic_robot_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "C:/kcl/robotics/ros/assignment_ws/src/basic_robot/msg/instructionsMessage.msg" NAME_WE)
add_dependencies(basic_robot_generate_messages_nodejs _basic_robot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(basic_robot_gennodejs)
add_dependencies(basic_robot_gennodejs basic_robot_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS basic_robot_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(basic_robot
  "C:/kcl/robotics/ros/assignment_ws/src/basic_robot/msg/instructionsMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/basic_robot
)

### Generating Services

### Generating Module File
_generate_module_py(basic_robot
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/basic_robot
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(basic_robot_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(basic_robot_generate_messages basic_robot_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "C:/kcl/robotics/ros/assignment_ws/src/basic_robot/msg/instructionsMessage.msg" NAME_WE)
add_dependencies(basic_robot_generate_messages_py _basic_robot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(basic_robot_genpy)
add_dependencies(basic_robot_genpy basic_robot_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS basic_robot_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/basic_robot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/basic_robot
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(basic_robot_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/basic_robot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/basic_robot
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(basic_robot_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/basic_robot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/basic_robot
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(basic_robot_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/basic_robot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/basic_robot
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(basic_robot_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/basic_robot)
  install(CODE "execute_process(COMMAND \"C:/opt/python27amd64/python.exe\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/basic_robot\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/basic_robot
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(basic_robot_generate_messages_py std_msgs_generate_messages_py)
endif()
