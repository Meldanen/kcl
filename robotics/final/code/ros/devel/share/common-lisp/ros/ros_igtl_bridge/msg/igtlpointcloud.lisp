; Auto-generated. Do not edit!


(cl:in-package ros_igtl_bridge-msg)


;//! \htmlinclude igtlpointcloud.msg.html

(cl:defclass <igtlpointcloud> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (pointdata
    :reader pointdata
    :initarg :pointdata
    :type (cl:vector geometry_msgs-msg:Point)
   :initform (cl:make-array 0 :element-type 'geometry_msgs-msg:Point :initial-element (cl:make-instance 'geometry_msgs-msg:Point))))
)

(cl:defclass igtlpointcloud (<igtlpointcloud>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <igtlpointcloud>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'igtlpointcloud)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_igtl_bridge-msg:<igtlpointcloud> is deprecated: use ros_igtl_bridge-msg:igtlpointcloud instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <igtlpointcloud>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:name-val is deprecated.  Use ros_igtl_bridge-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'pointdata-val :lambda-list '(m))
(cl:defmethod pointdata-val ((m <igtlpointcloud>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:pointdata-val is deprecated.  Use ros_igtl_bridge-msg:pointdata instead.")
  (pointdata m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <igtlpointcloud>) ostream)
  "Serializes a message object of type '<igtlpointcloud>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'pointdata))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'pointdata))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <igtlpointcloud>) istream)
  "Deserializes a message object of type '<igtlpointcloud>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'pointdata) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'pointdata)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geometry_msgs-msg:Point))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<igtlpointcloud>)))
  "Returns string type for a message object of type '<igtlpointcloud>"
  "ros_igtl_bridge/igtlpointcloud")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'igtlpointcloud)))
  "Returns string type for a message object of type 'igtlpointcloud"
  "ros_igtl_bridge/igtlpointcloud")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<igtlpointcloud>)))
  "Returns md5sum for a message object of type '<igtlpointcloud>"
  "fb1f671d9b816bd5dbd3deb4a0885963")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'igtlpointcloud)))
  "Returns md5sum for a message object of type 'igtlpointcloud"
  "fb1f671d9b816bd5dbd3deb4a0885963")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<igtlpointcloud>)))
  "Returns full string definition for message of type '<igtlpointcloud>"
  (cl:format cl:nil "#---Pointcloud Message~%~%string name~%geometry_msgs/Point[] pointdata~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'igtlpointcloud)))
  "Returns full string definition for message of type 'igtlpointcloud"
  (cl:format cl:nil "#---Pointcloud Message~%~%string name~%geometry_msgs/Point[] pointdata~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <igtlpointcloud>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'pointdata) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <igtlpointcloud>))
  "Converts a ROS message object to a list"
  (cl:list 'igtlpointcloud
    (cl:cons ':name (name msg))
    (cl:cons ':pointdata (pointdata msg))
))
