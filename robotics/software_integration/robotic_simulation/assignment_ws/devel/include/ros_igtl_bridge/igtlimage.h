// Generated by gencpp from file ros_igtl_bridge/igtlimage.msg
// DO NOT EDIT!


#ifndef ROS_IGTL_BRIDGE_MESSAGE_IGTLIMAGE_H
#define ROS_IGTL_BRIDGE_MESSAGE_IGTLIMAGE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ros_igtl_bridge
{
template <class ContainerAllocator>
struct igtlimage_
{
  typedef igtlimage_<ContainerAllocator> Type;

  igtlimage_()
    : name()
    , x_steps(0)
    , y_steps(0)
    , z_steps(0)
    , x_spacing(0.0)
    , y_spacing(0.0)
    , z_spacing(0.0)
    , data()  {
    }
  igtlimage_(const ContainerAllocator& _alloc)
    : name(_alloc)
    , x_steps(0)
    , y_steps(0)
    , z_steps(0)
    , x_spacing(0.0)
    , y_spacing(0.0)
    , z_spacing(0.0)
    , data(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _name_type;
  _name_type name;

   typedef int32_t _x_steps_type;
  _x_steps_type x_steps;

   typedef int32_t _y_steps_type;
  _y_steps_type y_steps;

   typedef int32_t _z_steps_type;
  _z_steps_type z_steps;

   typedef float _x_spacing_type;
  _x_spacing_type x_spacing;

   typedef float _y_spacing_type;
  _y_spacing_type y_spacing;

   typedef float _z_spacing_type;
  _z_spacing_type z_spacing;

   typedef std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other >  _data_type;
  _data_type data;





  typedef boost::shared_ptr< ::ros_igtl_bridge::igtlimage_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ros_igtl_bridge::igtlimage_<ContainerAllocator> const> ConstPtr;

}; // struct igtlimage_

typedef ::ros_igtl_bridge::igtlimage_<std::allocator<void> > igtlimage;

typedef boost::shared_ptr< ::ros_igtl_bridge::igtlimage > igtlimagePtr;
typedef boost::shared_ptr< ::ros_igtl_bridge::igtlimage const> igtlimageConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ros_igtl_bridge::igtlimage_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ros_igtl_bridge::igtlimage_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ros_igtl_bridge

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/melodic/share/sensor_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/melodic/share/geometry_msgs/cmake/../msg'], 'ros_igtl_bridge': ['/home/mikroszolos/kcl/robotics/slicerAndRos/assignment_ws/src/ROS-IGTL-Bridge/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ros_igtl_bridge::igtlimage_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ros_igtl_bridge::igtlimage_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_igtl_bridge::igtlimage_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_igtl_bridge::igtlimage_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_igtl_bridge::igtlimage_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_igtl_bridge::igtlimage_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ros_igtl_bridge::igtlimage_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e004951b468cda99488e8b1294df4cef";
  }

  static const char* value(const ::ros_igtl_bridge::igtlimage_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe004951b468cda99ULL;
  static const uint64_t static_value2 = 0x488e8b1294df4cefULL;
};

template<class ContainerAllocator>
struct DataType< ::ros_igtl_bridge::igtlimage_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ros_igtl_bridge/igtlimage";
  }

  static const char* value(const ::ros_igtl_bridge::igtlimage_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ros_igtl_bridge::igtlimage_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Image Message\n"
"string name\n"
"# Steps\n"
"int32 x_steps           \n"
"int32 y_steps           \n"
"int32 z_steps        \n"
"\n"
"float32 x_spacing           \n"
"float32 y_spacing           \n"
"float32 z_spacing           \n"
"\n"
"#sensor_msgs/Image rosimg\n"
"# Image data\n"
"uint8[] data		  \n"
;
  }

  static const char* value(const ::ros_igtl_bridge::igtlimage_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ros_igtl_bridge::igtlimage_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.name);
      stream.next(m.x_steps);
      stream.next(m.y_steps);
      stream.next(m.z_steps);
      stream.next(m.x_spacing);
      stream.next(m.y_spacing);
      stream.next(m.z_spacing);
      stream.next(m.data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct igtlimage_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ros_igtl_bridge::igtlimage_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ros_igtl_bridge::igtlimage_<ContainerAllocator>& v)
  {
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.name);
    s << indent << "x_steps: ";
    Printer<int32_t>::stream(s, indent + "  ", v.x_steps);
    s << indent << "y_steps: ";
    Printer<int32_t>::stream(s, indent + "  ", v.y_steps);
    s << indent << "z_steps: ";
    Printer<int32_t>::stream(s, indent + "  ", v.z_steps);
    s << indent << "x_spacing: ";
    Printer<float>::stream(s, indent + "  ", v.x_spacing);
    s << indent << "y_spacing: ";
    Printer<float>::stream(s, indent + "  ", v.y_spacing);
    s << indent << "z_spacing: ";
    Printer<float>::stream(s, indent + "  ", v.z_spacing);
    s << indent << "data[]" << std::endl;
    for (size_t i = 0; i < v.data.size(); ++i)
    {
      s << indent << "  data[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.data[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROS_IGTL_BRIDGE_MESSAGE_IGTLIMAGE_H