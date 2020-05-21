// Auto-generated. Do not edit!

// (in-package ros_igtl_bridge.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let vector = require('./vector.js');
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class igtlpolydata {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.name = null;
      this.points = null;
      this.polygons = null;
      this.strips = null;
      this.lines = null;
      this.verts = null;
    }
    else {
      if (initObj.hasOwnProperty('name')) {
        this.name = initObj.name
      }
      else {
        this.name = '';
      }
      if (initObj.hasOwnProperty('points')) {
        this.points = initObj.points
      }
      else {
        this.points = [];
      }
      if (initObj.hasOwnProperty('polygons')) {
        this.polygons = initObj.polygons
      }
      else {
        this.polygons = [];
      }
      if (initObj.hasOwnProperty('strips')) {
        this.strips = initObj.strips
      }
      else {
        this.strips = [];
      }
      if (initObj.hasOwnProperty('lines')) {
        this.lines = initObj.lines
      }
      else {
        this.lines = [];
      }
      if (initObj.hasOwnProperty('verts')) {
        this.verts = initObj.verts
      }
      else {
        this.verts = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type igtlpolydata
    // Serialize message field [name]
    bufferOffset = _serializer.string(obj.name, buffer, bufferOffset);
    // Serialize message field [points]
    // Serialize the length for message field [points]
    bufferOffset = _serializer.uint32(obj.points.length, buffer, bufferOffset);
    obj.points.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Point32.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [polygons]
    // Serialize the length for message field [polygons]
    bufferOffset = _serializer.uint32(obj.polygons.length, buffer, bufferOffset);
    obj.polygons.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Point32.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [strips]
    // Serialize the length for message field [strips]
    bufferOffset = _serializer.uint32(obj.strips.length, buffer, bufferOffset);
    obj.strips.forEach((val) => {
      bufferOffset = vector.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [lines]
    // Serialize the length for message field [lines]
    bufferOffset = _serializer.uint32(obj.lines.length, buffer, bufferOffset);
    obj.lines.forEach((val) => {
      bufferOffset = vector.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [verts]
    // Serialize the length for message field [verts]
    bufferOffset = _serializer.uint32(obj.verts.length, buffer, bufferOffset);
    obj.verts.forEach((val) => {
      bufferOffset = vector.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type igtlpolydata
    let len;
    let data = new igtlpolydata(null);
    // Deserialize message field [name]
    data.name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [points]
    // Deserialize array length for message field [points]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.points = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.points[i] = geometry_msgs.msg.Point32.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [polygons]
    // Deserialize array length for message field [polygons]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.polygons = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.polygons[i] = geometry_msgs.msg.Point32.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [strips]
    // Deserialize array length for message field [strips]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.strips = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.strips[i] = vector.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [lines]
    // Deserialize array length for message field [lines]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.lines = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.lines[i] = vector.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [verts]
    // Deserialize array length for message field [verts]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.verts = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.verts[i] = vector.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.name.length;
    length += 12 * object.points.length;
    length += 12 * object.polygons.length;
    object.strips.forEach((val) => {
      length += vector.getMessageSize(val);
    });
    object.lines.forEach((val) => {
      length += vector.getMessageSize(val);
    });
    object.verts.forEach((val) => {
      length += vector.getMessageSize(val);
    });
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ros_igtl_bridge/igtlpolydata';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8a567809576846ce15ffb57b198e0d5a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #---PolyData Message
    
    string name
    geometry_msgs/Point32[] points
    geometry_msgs/Point32[] polygons
    vector[] strips
    vector[] lines
    vector[] verts
    
    ================================================================================
    MSG: geometry_msgs/Point32
    # This contains the position of a point in free space(with 32 bits of precision).
    # It is recommeded to use Point wherever possible instead of Point32.  
    # 
    # This recommendation is to promote interoperability.  
    #
    # This message is designed to take up less space when sending
    # lots of points at once, as in the case of a PointCloud.  
    
    float32 x
    float32 y
    float32 z
    ================================================================================
    MSG: ros_igtl_bridge/vector
    float32[] data
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new igtlpolydata(null);
    if (msg.name !== undefined) {
      resolved.name = msg.name;
    }
    else {
      resolved.name = ''
    }

    if (msg.points !== undefined) {
      resolved.points = new Array(msg.points.length);
      for (let i = 0; i < resolved.points.length; ++i) {
        resolved.points[i] = geometry_msgs.msg.Point32.Resolve(msg.points[i]);
      }
    }
    else {
      resolved.points = []
    }

    if (msg.polygons !== undefined) {
      resolved.polygons = new Array(msg.polygons.length);
      for (let i = 0; i < resolved.polygons.length; ++i) {
        resolved.polygons[i] = geometry_msgs.msg.Point32.Resolve(msg.polygons[i]);
      }
    }
    else {
      resolved.polygons = []
    }

    if (msg.strips !== undefined) {
      resolved.strips = new Array(msg.strips.length);
      for (let i = 0; i < resolved.strips.length; ++i) {
        resolved.strips[i] = vector.Resolve(msg.strips[i]);
      }
    }
    else {
      resolved.strips = []
    }

    if (msg.lines !== undefined) {
      resolved.lines = new Array(msg.lines.length);
      for (let i = 0; i < resolved.lines.length; ++i) {
        resolved.lines[i] = vector.Resolve(msg.lines[i]);
      }
    }
    else {
      resolved.lines = []
    }

    if (msg.verts !== undefined) {
      resolved.verts = new Array(msg.verts.length);
      for (let i = 0; i < resolved.verts.length; ++i) {
        resolved.verts[i] = vector.Resolve(msg.verts[i]);
      }
    }
    else {
      resolved.verts = []
    }

    return resolved;
    }
};

module.exports = igtlpolydata;
