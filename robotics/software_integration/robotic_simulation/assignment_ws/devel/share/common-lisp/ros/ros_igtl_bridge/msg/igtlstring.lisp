; Auto-generated. Do not edit!


(cl:in-package ros_igtl_bridge-msg)


;//! \htmlinclude igtlstring.msg.html

(cl:defclass <igtlstring> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (data
    :reader data
    :initarg :data
    :type cl:string
    :initform ""))
)

(cl:defclass igtlstring (<igtlstring>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <igtlstring>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'igtlstring)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_igtl_bridge-msg:<igtlstring> is deprecated: use ros_igtl_bridge-msg:igtlstring instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <igtlstring>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:name-val is deprecated.  Use ros_igtl_bridge-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <igtlstring>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:data-val is deprecated.  Use ros_igtl_bridge-msg:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <igtlstring>) ostream)
  "Serializes a message object of type '<igtlstring>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <igtlstring>) istream)
  "Deserializes a message object of type '<igtlstring>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'data) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'data) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<igtlstring>)))
  "Returns string type for a message object of type '<igtlstring>"
  "ros_igtl_bridge/igtlstring")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'igtlstring)))
  "Returns string type for a message object of type 'igtlstring"
  "ros_igtl_bridge/igtlstring")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<igtlstring>)))
  "Returns md5sum for a message object of type '<igtlstring>"
  "0a150dc399b6cef3706553ca3c336ddf")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'igtlstring)))
  "Returns md5sum for a message object of type 'igtlstring"
  "0a150dc399b6cef3706553ca3c336ddf")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<igtlstring>)))
  "Returns full string definition for message of type '<igtlstring>"
  (cl:format cl:nil "#---String Message~%~%string name~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'igtlstring)))
  "Returns full string definition for message of type 'igtlstring"
  (cl:format cl:nil "#---String Message~%~%string name~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <igtlstring>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     4 (cl:length (cl:slot-value msg 'data))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <igtlstring>))
  "Converts a ROS message object to a list"
  (cl:list 'igtlstring
    (cl:cons ':name (name msg))
    (cl:cons ':data (data msg))
))
