// Generated by gencpp from file moveit_msgs/PlannerParams.msg
// DO NOT EDIT!


#ifndef MOVEIT_MSGS_MESSAGE_PLANNERPARAMS_H
#define MOVEIT_MSGS_MESSAGE_PLANNERPARAMS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace moveit_msgs
{
template <class ContainerAllocator>
struct PlannerParams_
{
  typedef PlannerParams_<ContainerAllocator> Type;

  PlannerParams_()
    : keys()
    , values()
    , descriptions()  {
    }
  PlannerParams_(const ContainerAllocator& _alloc)
    : keys(_alloc)
    , values(_alloc)
    , descriptions(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _keys_type;
  _keys_type keys;

   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _values_type;
  _values_type values;

   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _descriptions_type;
  _descriptions_type descriptions;





  typedef boost::shared_ptr< ::moveit_msgs::PlannerParams_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::moveit_msgs::PlannerParams_<ContainerAllocator> const> ConstPtr;

}; // struct PlannerParams_

typedef ::moveit_msgs::PlannerParams_<std::allocator<void> > PlannerParams;

typedef boost::shared_ptr< ::moveit_msgs::PlannerParams > PlannerParamsPtr;
typedef boost::shared_ptr< ::moveit_msgs::PlannerParams const> PlannerParamsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::moveit_msgs::PlannerParams_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::moveit_msgs::PlannerParams_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace moveit_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'shape_msgs': ['/opt/ros/melodic/share/shape_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'moveit_msgs': ['/home/mikroszolos/kcl/robotics/ros/ws_moveit/devel/.private/moveit_msgs/share/moveit_msgs/msg', '/home/mikroszolos/kcl/robotics/ros/ws_moveit/src/moveit_msgs/msg'], 'trajectory_msgs': ['/opt/ros/melodic/share/trajectory_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/melodic/share/sensor_msgs/cmake/../msg'], 'object_recognition_msgs': ['/opt/ros/melodic/share/object_recognition_msgs/cmake/../msg'], 'octomap_msgs': ['/opt/ros/melodic/share/octomap_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/melodic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/melodic/share/actionlib_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::moveit_msgs::PlannerParams_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::moveit_msgs::PlannerParams_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::moveit_msgs::PlannerParams_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::moveit_msgs::PlannerParams_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::moveit_msgs::PlannerParams_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::moveit_msgs::PlannerParams_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::moveit_msgs::PlannerParams_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cebdf4927996b9026bcf59a160d64145";
  }

  static const char* value(const ::moveit_msgs::PlannerParams_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xcebdf4927996b902ULL;
  static const uint64_t static_value2 = 0x6bcf59a160d64145ULL;
};

template<class ContainerAllocator>
struct DataType< ::moveit_msgs::PlannerParams_<ContainerAllocator> >
{
  static const char* value()
  {
    return "moveit_msgs/PlannerParams";
  }

  static const char* value(const ::moveit_msgs::PlannerParams_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::moveit_msgs::PlannerParams_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# parameter names (same size as values)\n"
"string[] keys\n"
"\n"
"# parameter values (same size as keys)\n"
"string[] values\n"
"\n"
"# parameter description (can be empty)\n"
"string[] descriptions\n"
;
  }

  static const char* value(const ::moveit_msgs::PlannerParams_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::moveit_msgs::PlannerParams_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.keys);
      stream.next(m.values);
      stream.next(m.descriptions);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PlannerParams_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::moveit_msgs::PlannerParams_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::moveit_msgs::PlannerParams_<ContainerAllocator>& v)
  {
    s << indent << "keys[]" << std::endl;
    for (size_t i = 0; i < v.keys.size(); ++i)
    {
      s << indent << "  keys[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.keys[i]);
    }
    s << indent << "values[]" << std::endl;
    for (size_t i = 0; i < v.values.size(); ++i)
    {
      s << indent << "  values[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.values[i]);
    }
    s << indent << "descriptions[]" << std::endl;
    for (size_t i = 0; i < v.descriptions.size(); ++i)
    {
      s << indent << "  descriptions[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.descriptions[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOVEIT_MSGS_MESSAGE_PLANNERPARAMS_H
