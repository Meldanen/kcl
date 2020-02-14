# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "r2d2: 1 messages, 1 services")

set(MSG_I_FLAGS "-Ir2d2:C:/kcl/robotics/ros/catkin_ws/src/r2d2/msg;-Istd_msgs:C:/opt/ros/melodic/x64/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(r2d2_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "C:/kcl/robotics/ros/catkin_ws/src/r2d2/msg/Num.msg" NAME_WE)
add_custom_target(_r2d2_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "r2d2" "C:/kcl/robotics/ros/catkin_ws/src/r2d2/msg/Num.msg" ""
)

get_filename_component(_filename "C:/kcl/robotics/ros/catkin_ws/src/r2d2/srv/AddTwoInts.srv" NAME_WE)
add_custom_target(_r2d2_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "r2d2" "C:/kcl/robotics/ros/catkin_ws/src/r2d2/srv/AddTwoInts.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(r2d2
  "C:/kcl/robotics/ros/catkin_ws/src/r2d2/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/r2d2
)

### Generating Services
_generate_srv_cpp(r2d2
  "C:/kcl/robotics/ros/catkin_ws/src/r2d2/srv/AddTwoInts.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/r2d2
)

### Generating Module File
_generate_module_cpp(r2d2
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/r2d2
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(r2d2_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(r2d2_generate_messages r2d2_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "C:/kcl/robotics/ros/catkin_ws/src/r2d2/msg/Num.msg" NAME_WE)
add_dependencies(r2d2_generate_messages_cpp _r2d2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/kcl/robotics/ros/catkin_ws/src/r2d2/srv/AddTwoInts.srv" NAME_WE)
add_dependencies(r2d2_generate_messages_cpp _r2d2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(r2d2_gencpp)
add_dependencies(r2d2_gencpp r2d2_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS r2d2_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(r2d2
  "C:/kcl/robotics/ros/catkin_ws/src/r2d2/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/r2d2
)

### Generating Services
_generate_srv_eus(r2d2
  "C:/kcl/robotics/ros/catkin_ws/src/r2d2/srv/AddTwoInts.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/r2d2
)

### Generating Module File
_generate_module_eus(r2d2
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/r2d2
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(r2d2_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(r2d2_generate_messages r2d2_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "C:/kcl/robotics/ros/catkin_ws/src/r2d2/msg/Num.msg" NAME_WE)
add_dependencies(r2d2_generate_messages_eus _r2d2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/kcl/robotics/ros/catkin_ws/src/r2d2/srv/AddTwoInts.srv" NAME_WE)
add_dependencies(r2d2_generate_messages_eus _r2d2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(r2d2_geneus)
add_dependencies(r2d2_geneus r2d2_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS r2d2_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(r2d2
  "C:/kcl/robotics/ros/catkin_ws/src/r2d2/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/r2d2
)

### Generating Services
_generate_srv_lisp(r2d2
  "C:/kcl/robotics/ros/catkin_ws/src/r2d2/srv/AddTwoInts.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/r2d2
)

### Generating Module File
_generate_module_lisp(r2d2
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/r2d2
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(r2d2_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(r2d2_generate_messages r2d2_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "C:/kcl/robotics/ros/catkin_ws/src/r2d2/msg/Num.msg" NAME_WE)
add_dependencies(r2d2_generate_messages_lisp _r2d2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/kcl/robotics/ros/catkin_ws/src/r2d2/srv/AddTwoInts.srv" NAME_WE)
add_dependencies(r2d2_generate_messages_lisp _r2d2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(r2d2_genlisp)
add_dependencies(r2d2_genlisp r2d2_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS r2d2_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(r2d2
  "C:/kcl/robotics/ros/catkin_ws/src/r2d2/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/r2d2
)

### Generating Services
_generate_srv_nodejs(r2d2
  "C:/kcl/robotics/ros/catkin_ws/src/r2d2/srv/AddTwoInts.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/r2d2
)

### Generating Module File
_generate_module_nodejs(r2d2
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/r2d2
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(r2d2_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(r2d2_generate_messages r2d2_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "C:/kcl/robotics/ros/catkin_ws/src/r2d2/msg/Num.msg" NAME_WE)
add_dependencies(r2d2_generate_messages_nodejs _r2d2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/kcl/robotics/ros/catkin_ws/src/r2d2/srv/AddTwoInts.srv" NAME_WE)
add_dependencies(r2d2_generate_messages_nodejs _r2d2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(r2d2_gennodejs)
add_dependencies(r2d2_gennodejs r2d2_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS r2d2_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(r2d2
  "C:/kcl/robotics/ros/catkin_ws/src/r2d2/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/r2d2
)

### Generating Services
_generate_srv_py(r2d2
  "C:/kcl/robotics/ros/catkin_ws/src/r2d2/srv/AddTwoInts.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/r2d2
)

### Generating Module File
_generate_module_py(r2d2
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/r2d2
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(r2d2_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(r2d2_generate_messages r2d2_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "C:/kcl/robotics/ros/catkin_ws/src/r2d2/msg/Num.msg" NAME_WE)
add_dependencies(r2d2_generate_messages_py _r2d2_generate_messages_check_deps_${_filename})
get_filename_component(_filename "C:/kcl/robotics/ros/catkin_ws/src/r2d2/srv/AddTwoInts.srv" NAME_WE)
add_dependencies(r2d2_generate_messages_py _r2d2_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(r2d2_genpy)
add_dependencies(r2d2_genpy r2d2_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS r2d2_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/r2d2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/r2d2
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(r2d2_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/r2d2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/r2d2
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(r2d2_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/r2d2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/r2d2
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(r2d2_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/r2d2)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/r2d2
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(r2d2_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/r2d2)
  install(CODE "execute_process(COMMAND \"C:/opt/python27amd64/python.exe\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/r2d2\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/r2d2
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(r2d2_generate_messages_py std_msgs_generate_messages_py)
endif()
