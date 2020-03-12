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

class igtlpoint {
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
        this.pointdata = new geometry_msgs.msg.Point();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type igtlpoint
    // Serialize message field [name]
    bufferOffset = _serializer.string(obj.name, buffer, bufferOffset);
    // Serialize message field [pointdata]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.pointdata, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type igtlpoint
    let len;
    let data = new igtlpoint(null);
    // Deserialize message field [name]
    data.name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [pointdata]
    data.pointdata = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.name.length;
    return length + 28;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ros_igtl_bridge/igtlpoint';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'fb1f671d9b816bd5dbd3deb4a0885963';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #---Point Message
    
    string name
    geometry_msgs/Point pointdata
    
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
    const resolved = new igtlpoint(null);
    if (msg.name !== undefined) {
      resolved.name = msg.name;
    }
    else {
      resolved.name = ''
    }

    if (msg.pointdata !== undefined) {
      resolved.pointdata = geometry_msgs.msg.Point.Resolve(msg.pointdata)
    }
    else {
      resolved.pointdata = new geometry_msgs.msg.Point()
    }

    return resolved;
    }
};

module.exports = igtlpoint;
