// Generated by gencpp from file moveit_msgs/GetPlanningSceneRequest.msg
// DO NOT EDIT!


#ifndef MOVEIT_MSGS_MESSAGE_GETPLANNINGSCENEREQUEST_H
#define MOVEIT_MSGS_MESSAGE_GETPLANNINGSCENEREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <moveit_msgs/PlanningSceneComponents.h>

namespace moveit_msgs
{
template <class ContainerAllocator>
struct GetPlanningSceneRequest_
{
  typedef GetPlanningSceneRequest_<ContainerAllocator> Type;

  GetPlanningSceneRequest_()
    : components()  {
    }
  GetPlanningSceneRequest_(const ContainerAllocator& _alloc)
    : components(_alloc)  {
  (void)_alloc;
    }



   typedef  ::moveit_msgs::PlanningSceneComponents_<ContainerAllocator>  _components_type;
  _components_type components;





  typedef boost::shared_ptr< ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator> const> ConstPtr;

}; // struct GetPlanningSceneRequest_

typedef ::moveit_msgs::GetPlanningSceneRequest_<std::allocator<void> > GetPlanningSceneRequest;

typedef boost::shared_ptr< ::moveit_msgs::GetPlanningSceneRequest > GetPlanningSceneRequestPtr;
typedef boost::shared_ptr< ::moveit_msgs::GetPlanningSceneRequest const> GetPlanningSceneRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace moveit_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'shape_msgs': ['/opt/ros/melodic/share/shape_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'moveit_msgs': ['/home/mikroszolos/kcl/robotics/ros/ws_moveit/devel/.private/moveit_msgs/share/moveit_msgs/msg', '/home/mikroszolos/kcl/robotics/ros/ws_moveit/src/moveit_msgs/msg'], 'trajectory_msgs': ['/opt/ros/melodic/share/trajectory_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/melodic/share/sensor_msgs/cmake/../msg'], 'object_recognition_msgs': ['/opt/ros/melodic/share/object_recognition_msgs/cmake/../msg'], 'octomap_msgs': ['/opt/ros/melodic/share/octomap_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/melodic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/melodic/share/actionlib_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d81da6c0e5e015646a4efe344f33d7dc";
  }

  static const char* value(const ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd81da6c0e5e01564ULL;
  static const uint64_t static_value2 = 0x6a4efe344f33d7dcULL;
};

template<class ContainerAllocator>
struct DataType< ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "moveit_msgs/GetPlanningSceneRequest";
  }

  static const char* value(const ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
"\n"
"PlanningSceneComponents components\n"
"\n"
"================================================================================\n"
"MSG: moveit_msgs/PlanningSceneComponents\n"
"# This message defines the components that make up the PlanningScene message.\n"
"# The values can be used as a bitfield to specify which parts of the PlanningScene message\n"
"# are of interest\n"
"\n"
"# Scene name, model name, model root\n"
"uint32 SCENE_SETTINGS=1\n"
"\n"
"# Joint values of the robot state\n"
"uint32 ROBOT_STATE=2\n"
"\n"
"# Attached objects (including geometry) for the robot state\n"
"uint32 ROBOT_STATE_ATTACHED_OBJECTS=4\n"
"\n"
"# The names of the world objects\n"
"uint32 WORLD_OBJECT_NAMES=8\n"
"\n"
"# The geometry of the world objects\n"
"uint32 WORLD_OBJECT_GEOMETRY=16\n"
"\n"
"# The maintained octomap \n"
"uint32 OCTOMAP=32\n"
"\n"
"# The maintained list of transforms\n"
"uint32 TRANSFORMS=64\n"
"\n"
"# The allowed collision matrix\n"
"uint32 ALLOWED_COLLISION_MATRIX=128\n"
"\n"
"# The default link padding and link scaling\n"
"uint32 LINK_PADDING_AND_SCALING=256\n"
"\n"
"# The stored object colors\n"
"uint32 OBJECT_COLORS=512\n"
"\n"
"# Bitfield combining options indicated above\n"
"uint32 components\n"
;
  }

  static const char* value(const ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.components);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GetPlanningSceneRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::moveit_msgs::GetPlanningSceneRequest_<ContainerAllocator>& v)
  {
    s << indent << "components: ";
    s << std::endl;
    Printer< ::moveit_msgs::PlanningSceneComponents_<ContainerAllocator> >::stream(s, indent + "  ", v.components);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOVEIT_MSGS_MESSAGE_GETPLANNINGSCENEREQUEST_H
