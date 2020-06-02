// Generated by gencpp from file ros_igtl_bridge/igtlpointcloud.msg
// DO NOT EDIT!


#ifndef ROS_IGTL_BRIDGE_MESSAGE_IGTLPOINTCLOUD_H
#define ROS_IGTL_BRIDGE_MESSAGE_IGTLPOINTCLOUD_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Point.h>

namespace ros_igtl_bridge
{
template <class ContainerAllocator>
struct igtlpointcloud_
{
  typedef igtlpointcloud_<ContainerAllocator> Type;

  igtlpointcloud_()
    : name()
    , pointdata()  {
    }
  igtlpointcloud_(const ContainerAllocator& _alloc)
    : name(_alloc)
    , pointdata(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _name_type;
  _name_type name;

   typedef std::vector< ::geometry_msgs::Point_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::geometry_msgs::Point_<ContainerAllocator> >::other >  _pointdata_type;
  _pointdata_type pointdata;





  typedef boost::shared_ptr< ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator> const> ConstPtr;

}; // struct igtlpointcloud_

typedef ::ros_igtl_bridge::igtlpointcloud_<std::allocator<void> > igtlpointcloud;

typedef boost::shared_ptr< ::ros_igtl_bridge::igtlpointcloud > igtlpointcloudPtr;
typedef boost::shared_ptr< ::ros_igtl_bridge::igtlpointcloud const> igtlpointcloudConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator1> & lhs, const ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator2> & rhs)
{
  return lhs.name == rhs.name &&
    lhs.pointdata == rhs.pointdata;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator1> & lhs, const ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ros_igtl_bridge

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fb1f671d9b816bd5dbd3deb4a0885963";
  }

  static const char* value(const ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xfb1f671d9b816bd5ULL;
  static const uint64_t static_value2 = 0xdbd3deb4a0885963ULL;
};

template<class ContainerAllocator>
struct DataType< ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ros_igtl_bridge/igtlpointcloud";
  }

  static const char* value(const ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator> >
{
  static const char* value()
  {
    return "#---Pointcloud Message\n"
"\n"
"string name\n"
"geometry_msgs/Point[] pointdata\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
;
  }

  static const char* value(const ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.name);
      stream.next(m.pointdata);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct igtlpointcloud_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ros_igtl_bridge::igtlpointcloud_<ContainerAllocator>& v)
  {
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.name);
    s << indent << "pointdata[]" << std::endl;
    for (size_t i = 0; i < v.pointdata.size(); ++i)
    {
      s << indent << "  pointdata[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::geometry_msgs::Point_<ContainerAllocator> >::stream(s, indent + "    ", v.pointdata[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROS_IGTL_BRIDGE_MESSAGE_IGTLPOINTCLOUD_H
