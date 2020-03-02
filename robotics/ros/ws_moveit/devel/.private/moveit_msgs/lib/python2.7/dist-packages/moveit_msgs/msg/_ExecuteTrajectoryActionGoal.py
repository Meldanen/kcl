# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from moveit_msgs/ExecuteTrajectoryActionGoal.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import trajectory_msgs.msg
import actionlib_msgs.msg
import geometry_msgs.msg
import moveit_msgs.msg
import genpy
import std_msgs.msg

class ExecuteTrajectoryActionGoal(genpy.Message):
  _md5sum = "36f350977c67bc94e8cd408452bad0f0"
  _type = "moveit_msgs/ExecuteTrajectoryActionGoal"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalID goal_id
ExecuteTrajectoryGoal goal

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: actionlib_msgs/GoalID
# The stamp should store the time at which this goal was requested.
# It is used by an action server when it tries to preempt all
# goals that were requested before a certain time
time stamp

# The id provides a way to associate feedback and
# result message with specific goal requests. The id
# specified must be unique.
string id


================================================================================
MSG: moveit_msgs/ExecuteTrajectoryGoal
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# The trajectory to execute
RobotTrajectory trajectory


================================================================================
MSG: moveit_msgs/RobotTrajectory
trajectory_msgs/JointTrajectory joint_trajectory
trajectory_msgs/MultiDOFJointTrajectory multi_dof_joint_trajectory

================================================================================
MSG: trajectory_msgs/JointTrajectory
Header header
string[] joint_names
JointTrajectoryPoint[] points
================================================================================
MSG: trajectory_msgs/JointTrajectoryPoint
# Each trajectory point specifies either positions[, velocities[, accelerations]]
# or positions[, effort] for the trajectory to be executed.
# All specified values are in the same order as the joint names in JointTrajectory.msg

float64[] positions
float64[] velocities
float64[] accelerations
float64[] effort
duration time_from_start

================================================================================
MSG: trajectory_msgs/MultiDOFJointTrajectory
# The header is used to specify the coordinate frame and the reference time for the trajectory durations
Header header

# A representation of a multi-dof joint trajectory (each point is a transformation)
# Each point along the trajectory will include an array of positions/velocities/accelerations
# that has the same length as the array of joint names, and has the same order of joints as 
# the joint names array.

string[] joint_names
MultiDOFJointTrajectoryPoint[] points

================================================================================
MSG: trajectory_msgs/MultiDOFJointTrajectoryPoint
# Each multi-dof joint can specify a transform (up to 6 DOF)
geometry_msgs/Transform[] transforms

# There can be a velocity specified for the origin of the joint 
geometry_msgs/Twist[] velocities

# There can be an acceleration specified for the origin of the joint 
geometry_msgs/Twist[] accelerations

duration time_from_start

================================================================================
MSG: geometry_msgs/Transform
# This represents the transform between two coordinate frames in free space.

Vector3 translation
Quaternion rotation

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular
"""
  __slots__ = ['header','goal_id','goal']
  _slot_types = ['std_msgs/Header','actionlib_msgs/GoalID','moveit_msgs/ExecuteTrajectoryGoal']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,goal_id,goal

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ExecuteTrajectoryActionGoal, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.goal_id is None:
        self.goal_id = actionlib_msgs.msg.GoalID()
      if self.goal is None:
        self.goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
    else:
      self.header = std_msgs.msg.Header()
      self.goal_id = actionlib_msgs.msg.GoalID()
      self.goal = moveit_msgs.msg.ExecuteTrajectoryGoal()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs))
      _x = self.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.goal.trajectory.joint_trajectory.header.seq, _x.goal.trajectory.joint_trajectory.header.stamp.secs, _x.goal.trajectory.joint_trajectory.header.stamp.nsecs))
      _x = self.goal.trajectory.joint_trajectory.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.goal.trajectory.joint_trajectory.joint_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.goal.trajectory.joint_trajectory.joint_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.goal.trajectory.joint_trajectory.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.goal.trajectory.joint_trajectory.points:
        length = len(val1.positions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.positions))
        length = len(val1.velocities)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.velocities))
        length = len(val1.accelerations)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.accelerations))
        length = len(val1.effort)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.effort))
        _v1 = val1.time_from_start
        _x = _v1
        buff.write(_get_struct_2i().pack(_x.secs, _x.nsecs))
      _x = self
      buff.write(_get_struct_3I().pack(_x.goal.trajectory.multi_dof_joint_trajectory.header.seq, _x.goal.trajectory.multi_dof_joint_trajectory.header.stamp.secs, _x.goal.trajectory.multi_dof_joint_trajectory.header.stamp.nsecs))
      _x = self.goal.trajectory.multi_dof_joint_trajectory.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.goal.trajectory.multi_dof_joint_trajectory.joint_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.goal.trajectory.multi_dof_joint_trajectory.joint_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.goal.trajectory.multi_dof_joint_trajectory.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.goal.trajectory.multi_dof_joint_trajectory.points:
        length = len(val1.transforms)
        buff.write(_struct_I.pack(length))
        for val2 in val1.transforms:
          _v2 = val2.translation
          _x = _v2
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v3 = val2.rotation
          _x = _v3
          buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        length = len(val1.velocities)
        buff.write(_struct_I.pack(length))
        for val2 in val1.velocities:
          _v4 = val2.linear
          _x = _v4
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v5 = val2.angular
          _x = _v5
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        length = len(val1.accelerations)
        buff.write(_struct_I.pack(length))
        for val2 in val1.accelerations:
          _v6 = val2.linear
          _x = _v6
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v7 = val2.angular
          _x = _v7
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v8 = val1.time_from_start
        _x = _v8
        buff.write(_get_struct_2i().pack(_x.secs, _x.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.goal_id is None:
        self.goal_id = actionlib_msgs.msg.GoalID()
      if self.goal is None:
        self.goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal_id.id = str[start:end].decode('utf-8')
      else:
        self.goal_id.id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.goal.trajectory.joint_trajectory.header.seq, _x.goal.trajectory.joint_trajectory.header.stamp.secs, _x.goal.trajectory.joint_trajectory.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal.trajectory.joint_trajectory.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.goal.trajectory.joint_trajectory.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.goal.trajectory.joint_trajectory.joint_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.goal.trajectory.joint_trajectory.joint_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.goal.trajectory.joint_trajectory.points = []
      for i in range(0, length):
        val1 = trajectory_msgs.msg.JointTrajectoryPoint()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.positions = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.velocities = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.accelerations = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.effort = struct.unpack(pattern, str[start:end])
        _v9 = val1.time_from_start
        _x = _v9
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2i().unpack(str[start:end])
        self.goal.trajectory.joint_trajectory.points.append(val1)
      _x = self
      start = end
      end += 12
      (_x.goal.trajectory.multi_dof_joint_trajectory.header.seq, _x.goal.trajectory.multi_dof_joint_trajectory.header.stamp.secs, _x.goal.trajectory.multi_dof_joint_trajectory.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal.trajectory.multi_dof_joint_trajectory.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.goal.trajectory.multi_dof_joint_trajectory.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.goal.trajectory.multi_dof_joint_trajectory.joint_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.goal.trajectory.multi_dof_joint_trajectory.joint_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.goal.trajectory.multi_dof_joint_trajectory.points = []
      for i in range(0, length):
        val1 = trajectory_msgs.msg.MultiDOFJointTrajectoryPoint()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.transforms = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Transform()
          _v10 = val2.translation
          _x = _v10
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v11 = val2.rotation
          _x = _v11
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
          val1.transforms.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.velocities = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Twist()
          _v12 = val2.linear
          _x = _v12
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v13 = val2.angular
          _x = _v13
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          val1.velocities.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.accelerations = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Twist()
          _v14 = val2.linear
          _x = _v14
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v15 = val2.angular
          _x = _v15
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          val1.accelerations.append(val2)
        _v16 = val1.time_from_start
        _x = _v16
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2i().unpack(str[start:end])
        self.goal.trajectory.multi_dof_joint_trajectory.points.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs))
      _x = self.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.goal.trajectory.joint_trajectory.header.seq, _x.goal.trajectory.joint_trajectory.header.stamp.secs, _x.goal.trajectory.joint_trajectory.header.stamp.nsecs))
      _x = self.goal.trajectory.joint_trajectory.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.goal.trajectory.joint_trajectory.joint_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.goal.trajectory.joint_trajectory.joint_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.goal.trajectory.joint_trajectory.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.goal.trajectory.joint_trajectory.points:
        length = len(val1.positions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.positions.tostring())
        length = len(val1.velocities)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.velocities.tostring())
        length = len(val1.accelerations)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.accelerations.tostring())
        length = len(val1.effort)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.effort.tostring())
        _v17 = val1.time_from_start
        _x = _v17
        buff.write(_get_struct_2i().pack(_x.secs, _x.nsecs))
      _x = self
      buff.write(_get_struct_3I().pack(_x.goal.trajectory.multi_dof_joint_trajectory.header.seq, _x.goal.trajectory.multi_dof_joint_trajectory.header.stamp.secs, _x.goal.trajectory.multi_dof_joint_trajectory.header.stamp.nsecs))
      _x = self.goal.trajectory.multi_dof_joint_trajectory.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.goal.trajectory.multi_dof_joint_trajectory.joint_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.goal.trajectory.multi_dof_joint_trajectory.joint_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.goal.trajectory.multi_dof_joint_trajectory.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.goal.trajectory.multi_dof_joint_trajectory.points:
        length = len(val1.transforms)
        buff.write(_struct_I.pack(length))
        for val2 in val1.transforms:
          _v18 = val2.translation
          _x = _v18
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v19 = val2.rotation
          _x = _v19
          buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        length = len(val1.velocities)
        buff.write(_struct_I.pack(length))
        for val2 in val1.velocities:
          _v20 = val2.linear
          _x = _v20
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v21 = val2.angular
          _x = _v21
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        length = len(val1.accelerations)
        buff.write(_struct_I.pack(length))
        for val2 in val1.accelerations:
          _v22 = val2.linear
          _x = _v22
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v23 = val2.angular
          _x = _v23
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v24 = val1.time_from_start
        _x = _v24
        buff.write(_get_struct_2i().pack(_x.secs, _x.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.goal_id is None:
        self.goal_id = actionlib_msgs.msg.GoalID()
      if self.goal is None:
        self.goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal_id.id = str[start:end].decode('utf-8')
      else:
        self.goal_id.id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.goal.trajectory.joint_trajectory.header.seq, _x.goal.trajectory.joint_trajectory.header.stamp.secs, _x.goal.trajectory.joint_trajectory.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal.trajectory.joint_trajectory.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.goal.trajectory.joint_trajectory.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.goal.trajectory.joint_trajectory.joint_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.goal.trajectory.joint_trajectory.joint_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.goal.trajectory.joint_trajectory.points = []
      for i in range(0, length):
        val1 = trajectory_msgs.msg.JointTrajectoryPoint()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.positions = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.velocities = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.accelerations = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.effort = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        _v25 = val1.time_from_start
        _x = _v25
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2i().unpack(str[start:end])
        self.goal.trajectory.joint_trajectory.points.append(val1)
      _x = self
      start = end
      end += 12
      (_x.goal.trajectory.multi_dof_joint_trajectory.header.seq, _x.goal.trajectory.multi_dof_joint_trajectory.header.stamp.secs, _x.goal.trajectory.multi_dof_joint_trajectory.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal.trajectory.multi_dof_joint_trajectory.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.goal.trajectory.multi_dof_joint_trajectory.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.goal.trajectory.multi_dof_joint_trajectory.joint_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.goal.trajectory.multi_dof_joint_trajectory.joint_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.goal.trajectory.multi_dof_joint_trajectory.points = []
      for i in range(0, length):
        val1 = trajectory_msgs.msg.MultiDOFJointTrajectoryPoint()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.transforms = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Transform()
          _v26 = val2.translation
          _x = _v26
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v27 = val2.rotation
          _x = _v27
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
          val1.transforms.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.velocities = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Twist()
          _v28 = val2.linear
          _x = _v28
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v29 = val2.angular
          _x = _v29
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          val1.velocities.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.accelerations = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Twist()
          _v30 = val2.linear
          _x = _v30
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v31 = val2.angular
          _x = _v31
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          val1.accelerations.append(val2)
        _v32 = val1.time_from_start
        _x = _v32
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2i().unpack(str[start:end])
        self.goal.trajectory.multi_dof_joint_trajectory.points.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_2i = None
def _get_struct_2i():
    global _struct_2i
    if _struct_2i is None:
        _struct_2i = struct.Struct("<2i")
    return _struct_2i
