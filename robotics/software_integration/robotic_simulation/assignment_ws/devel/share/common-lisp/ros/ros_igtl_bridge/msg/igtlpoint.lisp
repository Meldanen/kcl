; Auto-generated. Do not edit!


(cl:in-package ros_igtl_bridge-msg)


;//! \htmlinclude igtlpoint.msg.html

(cl:defclass <igtlpoint> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (pointdata
    :reader pointdata
    :initarg :pointdata
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point)))
)

(cl:defclass igtlpoint (<igtlpoint>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <igtlpoint>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'igtlpoint)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_igtl_bridge-msg:<igtlpoint> is deprecated: use ros_igtl_bridge-msg:igtlpoint instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <igtlpoint>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:name-val is deprecated.  Use ros_igtl_bridge-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'pointdata-val :lambda-list '(m))
(cl:defmethod pointdata-val ((m <igtlpoint>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:pointdata-val is deprecated.  Use ros_igtl_bridge-msg:pointdata instead.")
  (pointdata m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <igtlpoint>) ostream)
  "Serializes a message object of type '<igtlpoint>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pointdata) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <igtlpoint>) istream)
  "Deserializes a message object of type '<igtlpoint>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pointdata) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<igtlpoint>)))
  "Returns string type for a message object of type '<igtlpoint>"
  "ros_igtl_bridge/igtlpoint")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'igtlpoint)))
  "Returns string type for a message object of type 'igtlpoint"
  "ros_igtl_bridge/igtlpoint")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<igtlpoint>)))
  "Returns md5sum for a message object of type '<igtlpoint>"
  "fb1f671d9b816bd5dbd3deb4a0885963")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'igtlpoint)))
  "Returns md5sum for a message object of type 'igtlpoint"
  "fb1f671d9b816bd5dbd3deb4a0885963")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<igtlpoint>)))
  "Returns full string definition for message of type '<igtlpoint>"
  (cl:format cl:nil "#---Point Message~%~%string name~%geometry_msgs/Point pointdata~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'igtlpoint)))
  "Returns full string definition for message of type 'igtlpoint"
  (cl:format cl:nil "#---Point Message~%~%string name~%geometry_msgs/Point pointdata~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <igtlpoint>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pointdata))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <igtlpoint>))
  "Converts a ROS message object to a list"
  (cl:list 'igtlpoint
    (cl:cons ':name (name msg))
    (cl:cons ':pointdata (pointdata msg))
))
