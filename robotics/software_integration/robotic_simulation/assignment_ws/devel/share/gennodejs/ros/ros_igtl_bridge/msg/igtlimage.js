// Auto-generated. Do not edit!

// (in-package ros_igtl_bridge.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class igtlimage {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.name = null;
      this.x_steps = null;
      this.y_steps = null;
      this.z_steps = null;
      this.x_spacing = null;
      this.y_spacing = null;
      this.z_spacing = null;
      this.data = null;
    }
    else {
      if (initObj.hasOwnProperty('name')) {
        this.name = initObj.name
      }
      else {
        this.name = '';
      }
      if (initObj.hasOwnProperty('x_steps')) {
        this.x_steps = initObj.x_steps
      }
      else {
        this.x_steps = 0;
      }
      if (initObj.hasOwnProperty('y_steps')) {
        this.y_steps = initObj.y_steps
      }
      else {
        this.y_steps = 0;
      }
      if (initObj.hasOwnProperty('z_steps')) {
        this.z_steps = initObj.z_steps
      }
      else {
        this.z_steps = 0;
      }
      if (initObj.hasOwnProperty('x_spacing')) {
        this.x_spacing = initObj.x_spacing
      }
      else {
        this.x_spacing = 0.0;
      }
      if (initObj.hasOwnProperty('y_spacing')) {
        this.y_spacing = initObj.y_spacing
      }
      else {
        this.y_spacing = 0.0;
      }
      if (initObj.hasOwnProperty('z_spacing')) {
        this.z_spacing = initObj.z_spacing
      }
      else {
        this.z_spacing = 0.0;
      }
      if (initObj.hasOwnProperty('data')) {
        this.data = initObj.data
      }
      else {
        this.data = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type igtlimage
    // Serialize message field [name]
    bufferOffset = _serializer.string(obj.name, buffer, bufferOffset);
    // Serialize message field [x_steps]
    bufferOffset = _serializer.int32(obj.x_steps, buffer, bufferOffset);
    // Serialize message field [y_steps]
    bufferOffset = _serializer.int32(obj.y_steps, buffer, bufferOffset);
    // Serialize message field [z_steps]
    bufferOffset = _serializer.int32(obj.z_steps, buffer, bufferOffset);
    // Serialize message field [x_spacing]
    bufferOffset = _serializer.float32(obj.x_spacing, buffer, bufferOffset);
    // Serialize message field [y_spacing]
    bufferOffset = _serializer.float32(obj.y_spacing, buffer, bufferOffset);
    // Serialize message field [z_spacing]
    bufferOffset = _serializer.float32(obj.z_spacing, buffer, bufferOffset);
    // Serialize message field [data]
    bufferOffset = _arraySerializer.uint8(obj.data, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type igtlimage
    let len;
    let data = new igtlimage(null);
    // Deserialize message field [name]
    data.name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [x_steps]
    data.x_steps = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [y_steps]
    data.y_steps = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [z_steps]
    data.z_steps = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [x_spacing]
    data.x_spacing = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [y_spacing]
    data.y_spacing = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [z_spacing]
    data.z_spacing = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [data]
    data.data = _arrayDeserializer.uint8(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.name.length;
    length += object.data.length;
    return length + 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ros_igtl_bridge/igtlimage';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e004951b468cda99488e8b1294df4cef';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Image Message
    string name
    # Steps
    int32 x_steps           
    int32 y_steps           
    int32 z_steps        
    
    float32 x_spacing           
    float32 y_spacing           
    float32 z_spacing           
    
    #sensor_msgs/Image rosimg
    # Image data
    uint8[] data		  
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new igtlimage(null);
    if (msg.name !== undefined) {
      resolved.name = msg.name;
    }
    else {
      resolved.name = ''
    }

    if (msg.x_steps !== undefined) {
      resolved.x_steps = msg.x_steps;
    }
    else {
      resolved.x_steps = 0
    }

    if (msg.y_steps !== undefined) {
      resolved.y_steps = msg.y_steps;
    }
    else {
      resolved.y_steps = 0
    }

    if (msg.z_steps !== undefined) {
      resolved.z_steps = msg.z_steps;
    }
    else {
      resolved.z_steps = 0
    }

    if (msg.x_spacing !== undefined) {
      resolved.x_spacing = msg.x_spacing;
    }
    else {
      resolved.x_spacing = 0.0
    }

    if (msg.y_spacing !== undefined) {
      resolved.y_spacing = msg.y_spacing;
    }
    else {
      resolved.y_spacing = 0.0
    }

    if (msg.z_spacing !== undefined) {
      resolved.z_spacing = msg.z_spacing;
    }
    else {
      resolved.z_spacing = 0.0
    }

    if (msg.data !== undefined) {
      resolved.data = msg.data;
    }
    else {
      resolved.data = []
    }

    return resolved;
    }
};

module.exports = igtlimage;
