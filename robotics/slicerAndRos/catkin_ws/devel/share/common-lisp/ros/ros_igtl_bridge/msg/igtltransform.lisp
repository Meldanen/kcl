; Auto-generated. Do not edit!


(cl:in-package ros_igtl_bridge-msg)


;//! \htmlinclude igtltransform.msg.html

(cl:defclass <igtltransform> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (transform
    :reader transform
    :initarg :transform
    :type geometry_msgs-msg:Transform
    :initform (cl:make-instance 'geometry_msgs-msg:Transform)))
)

(cl:defclass igtltransform (<igtltransform>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <igtltransform>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'igtltransform)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_igtl_bridge-msg:<igtltransform> is deprecated: use ros_igtl_bridge-msg:igtltransform instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <igtltransform>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:name-val is deprecated.  Use ros_igtl_bridge-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'transform-val :lambda-list '(m))
(cl:defmethod transform-val ((m <igtltransform>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:transform-val is deprecated.  Use ros_igtl_bridge-msg:transform instead.")
  (transform m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <igtltransform>) ostream)
  "Serializes a message object of type '<igtltransform>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'transform) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <igtltransform>) istream)
  "Deserializes a message object of type '<igtltransform>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'transform) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<igtltransform>)))
  "Returns string type for a message object of type '<igtltransform>"
  "ros_igtl_bridge/igtltransform")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'igtltransform)))
  "Returns string type for a message object of type 'igtltransform"
  "ros_igtl_bridge/igtltransform")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<igtltransform>)))
  "Returns md5sum for a message object of type '<igtltransform>"
  "5b37f5c9159d09ed0eb53ad625b51f59")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'igtltransform)))
  "Returns md5sum for a message object of type 'igtltransform"
  "5b37f5c9159d09ed0eb53ad625b51f59")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<igtltransform>)))
  "Returns full string definition for message of type '<igtltransform>"
  (cl:format cl:nil "#---Transform Message~% ~%string name~%geometry_msgs/Transform transform~%~%================================================================================~%MSG: geometry_msgs/Transform~%# This represents the transform between two coordinate frames in free space.~%~%Vector3 translation~%Quaternion rotation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'igtltransform)))
  "Returns full string definition for message of type 'igtltransform"
  (cl:format cl:nil "#---Transform Message~% ~%string name~%geometry_msgs/Transform transform~%~%================================================================================~%MSG: geometry_msgs/Transform~%# This represents the transform between two coordinate frames in free space.~%~%Vector3 translation~%Quaternion rotation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <igtltransform>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'transform))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <igtltransform>))
  "Converts a ROS message object to a list"
  (cl:list 'igtltransform
    (cl:cons ':name (name msg))
    (cl:cons ':transform (transform msg))
))
