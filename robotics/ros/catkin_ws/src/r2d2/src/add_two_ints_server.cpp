#include "ros/ros.h"
#include "r2d2/AddTwoInts.h"
#include <string>
#include <sensor_msgs/JointState.h>
#include <tf/transform_broadcaster.h>
#include "std_msgs/String.h"
#include <iostream>
#include <sstream>

bool add(r2d2::AddTwoInts::Request &req,
         r2d2::AddTwoInts::Response &res) {
    res.sum = req.a + req.b;
    ROS_INFO("request: x=%ld, y=%ld", (long int) req.a, (long int) req.b);
    ROS_INFO("sending back response: [%ld]", (long int) res.sum);
    return true;
}

int main(int argc, char **argv) {
    ros::init(argc, argv, "add_two_ints_server");
    ros::NodeHandle n;

    ros::Publisher joint_pub = n.advertise<sensor_msgs::JointState>("joint_states", 1);
    tf::TransformBroadcaster broadcaster;
    ros::Rate loop_rate(30);
//    ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);
    const double degree = M_PI / 180;

    // robot state
    double tilt = 0, tinc = degree, joint1 = 0, joint2 = 0, x = 0, angle = 0, height = 0, hinc = 0.005;
    geometry_msgs::TransformStamped odom_trans;
    sensor_msgs::JointState joint_state;

    joint_state.header.stamp = ros::Time::now();
    joint_state.name.resize(2);
    joint_state.position.resize(2);
    joint_state.name[0] = "base_link__link_01";
    joint_state.position[0] = joint1;
//    joint_state.name[1] = "joint2";
//    joint_state.position[1] = joint2;
    //joint_state.name[1] ="tilt";
    //joint_state.position[1] = tilt;
    //joint_state.name[2] ="periscope";
    //joint_state.position[2] = height;


    // update transform
    // (moving in a circle with radius=2)
    // odom_trans.header.stamp = ros::Time::now();
    //odom_trans.transform.translation.x = cos(angle)*2;
    //odom_trans.transform.translation.y = sin(angle)*2;
    //odom_trans.transform.translation.z = .7;
    //odom_trans.transform.rotation = tf::createQuaternionMsgFromYaw(angle+M_PI/2);

    //send the joint state and transform
    joint_pub.publish(joint_state);
    //broadcaster.sendTransform(odom_trans);

    // Create new robot state
    tilt += tinc;
    if (tilt < -.5 || tilt > 0) tinc *= -1;
    height += hinc;
    if (height > .2 || height < 0) hinc *= -1;
    joint1 += x;
    joint2 += x;
    angle += degree / 4;

    // This will adjust as needed per iteration
    loop_rate.sleep();


    ros::ServiceServer service = n.advertiseService("add_two_ints", add);
    ROS_INFO("Ready to add two ints.");
    ros::spin();

    return 0;
}