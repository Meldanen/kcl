// Auto-generated. Do not edit!

// (in-package ros_igtl_bridge.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class igtlpointcloud {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.name = null;
      this.pointdata = null;
    }
    else {
      if (initObj.hasOwnProperty('name')) {
        this.name = initObj.name
      }
      else {
        this.name = '';
      }
      if (initObj.hasOwnProperty('pointdata')) {
        this.pointdata = initObj.pointdata
      }
      else {
        this.pointdata = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type igtlpointcloud
    // Serialize message field [name]
    bufferOffset = _serializer.string(obj.name, buffer, bufferOffset);
    // Serialize message field [pointdata]
    // Serialize the length for message field [pointdata]
    bufferOffset = _serializer.uint32(obj.pointdata.length, buffer, bufferOffset);
    obj.pointdata.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Point.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type igtlpointcloud
    let len;
    let data = new igtlpointcloud(null);
    // Deserialize message field [name]
    data.name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [pointdata]
    // Deserialize array length for message field [pointdata]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.pointdata = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.pointdata[i] = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.name.length;
    length += 24 * object.pointdata.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ros_igtl_bridge/igtlpointcloud';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'fb1f671d9b816bd5dbd3deb4a0885963';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #---Pointcloud Message
    
    string name
    geometry_msgs/Point[] pointdata
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new igtlpointcloud(null);
    if (msg.name !== undefined) {
      resolved.name = msg.name;
    }
    else {
      resolved.name = ''
    }

    if (msg.pointdata !== undefined) {
      resolved.pointdata = new Array(msg.pointdata.length);
      for (let i = 0; i < resolved.pointdata.length; ++i) {
        resolved.pointdata[i] = geometry_msgs.msg.Point.Resolve(msg.pointdata[i]);
      }
    }
    else {
      resolved.pointdata = []
    }

    return resolved;
    }
};

module.exports = igtlpointcloud;
