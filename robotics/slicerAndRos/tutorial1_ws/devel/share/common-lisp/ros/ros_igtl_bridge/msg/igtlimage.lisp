; Auto-generated. Do not edit!


(cl:in-package ros_igtl_bridge-msg)


;//! \htmlinclude igtlimage.msg.html

(cl:defclass <igtlimage> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (x_steps
    :reader x_steps
    :initarg :x_steps
    :type cl:integer
    :initform 0)
   (y_steps
    :reader y_steps
    :initarg :y_steps
    :type cl:integer
    :initform 0)
   (z_steps
    :reader z_steps
    :initarg :z_steps
    :type cl:integer
    :initform 0)
   (x_spacing
    :reader x_spacing
    :initarg :x_spacing
    :type cl:float
    :initform 0.0)
   (y_spacing
    :reader y_spacing
    :initarg :y_spacing
    :type cl:float
    :initform 0.0)
   (z_spacing
    :reader z_spacing
    :initarg :z_spacing
    :type cl:float
    :initform 0.0)
   (data
    :reader data
    :initarg :data
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass igtlimage (<igtlimage>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <igtlimage>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'igtlimage)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_igtl_bridge-msg:<igtlimage> is deprecated: use ros_igtl_bridge-msg:igtlimage instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <igtlimage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:name-val is deprecated.  Use ros_igtl_bridge-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'x_steps-val :lambda-list '(m))
(cl:defmethod x_steps-val ((m <igtlimage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:x_steps-val is deprecated.  Use ros_igtl_bridge-msg:x_steps instead.")
  (x_steps m))

(cl:ensure-generic-function 'y_steps-val :lambda-list '(m))
(cl:defmethod y_steps-val ((m <igtlimage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:y_steps-val is deprecated.  Use ros_igtl_bridge-msg:y_steps instead.")
  (y_steps m))

(cl:ensure-generic-function 'z_steps-val :lambda-list '(m))
(cl:defmethod z_steps-val ((m <igtlimage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:z_steps-val is deprecated.  Use ros_igtl_bridge-msg:z_steps instead.")
  (z_steps m))

(cl:ensure-generic-function 'x_spacing-val :lambda-list '(m))
(cl:defmethod x_spacing-val ((m <igtlimage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:x_spacing-val is deprecated.  Use ros_igtl_bridge-msg:x_spacing instead.")
  (x_spacing m))

(cl:ensure-generic-function 'y_spacing-val :lambda-list '(m))
(cl:defmethod y_spacing-val ((m <igtlimage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:y_spacing-val is deprecated.  Use ros_igtl_bridge-msg:y_spacing instead.")
  (y_spacing m))

(cl:ensure-generic-function 'z_spacing-val :lambda-list '(m))
(cl:defmethod z_spacing-val ((m <igtlimage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:z_spacing-val is deprecated.  Use ros_igtl_bridge-msg:z_spacing instead.")
  (z_spacing m))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <igtlimage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:data-val is deprecated.  Use ros_igtl_bridge-msg:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <igtlimage>) ostream)
  "Serializes a message object of type '<igtlimage>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let* ((signed (cl:slot-value msg 'x_steps)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'y_steps)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'z_steps)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x_spacing))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y_spacing))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'z_spacing))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream))
   (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <igtlimage>) istream)
  "Deserializes a message object of type '<igtlimage>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'x_steps) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'y_steps) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'z_steps) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x_spacing) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y_spacing) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'z_spacing) (roslisp-utils:decode-single-float-bits bits)))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<igtlimage>)))
  "Returns string type for a message object of type '<igtlimage>"
  "ros_igtl_bridge/igtlimage")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'igtlimage)))
  "Returns string type for a message object of type 'igtlimage"
  "ros_igtl_bridge/igtlimage")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<igtlimage>)))
  "Returns md5sum for a message object of type '<igtlimage>"
  "e004951b468cda99488e8b1294df4cef")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'igtlimage)))
  "Returns md5sum for a message object of type 'igtlimage"
  "e004951b468cda99488e8b1294df4cef")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<igtlimage>)))
  "Returns full string definition for message of type '<igtlimage>"
  (cl:format cl:nil "# Image Message~%string name~%# Steps~%int32 x_steps           ~%int32 y_steps           ~%int32 z_steps        ~%~%float32 x_spacing           ~%float32 y_spacing           ~%float32 z_spacing           ~%~%#sensor_msgs/Image rosimg~%# Image data~%uint8[] data		  ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'igtlimage)))
  "Returns full string definition for message of type 'igtlimage"
  (cl:format cl:nil "# Image Message~%string name~%# Steps~%int32 x_steps           ~%int32 y_steps           ~%int32 z_steps        ~%~%float32 x_spacing           ~%float32 y_spacing           ~%float32 z_spacing           ~%~%#sensor_msgs/Image rosimg~%# Image data~%uint8[] data		  ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <igtlimage>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     4
     4
     4
     4
     4
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <igtlimage>))
  "Converts a ROS message object to a list"
  (cl:list 'igtlimage
    (cl:cons ':name (name msg))
    (cl:cons ':x_steps (x_steps msg))
    (cl:cons ':y_steps (y_steps msg))
    (cl:cons ':z_steps (z_steps msg))
    (cl:cons ':x_spacing (x_spacing msg))
    (cl:cons ':y_spacing (y_spacing msg))
    (cl:cons ':z_spacing (z_spacing msg))
    (cl:cons ':data (data msg))
))
