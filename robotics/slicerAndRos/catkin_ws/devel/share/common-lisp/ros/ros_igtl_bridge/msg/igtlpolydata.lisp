; Auto-generated. Do not edit!


(cl:in-package ros_igtl_bridge-msg)


;//! \htmlinclude igtlpolydata.msg.html

(cl:defclass <igtlpolydata> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (points
    :reader points
    :initarg :points
    :type (cl:vector geometry_msgs-msg:Point32)
   :initform (cl:make-array 0 :element-type 'geometry_msgs-msg:Point32 :initial-element (cl:make-instance 'geometry_msgs-msg:Point32)))
   (polygons
    :reader polygons
    :initarg :polygons
    :type (cl:vector geometry_msgs-msg:Point32)
   :initform (cl:make-array 0 :element-type 'geometry_msgs-msg:Point32 :initial-element (cl:make-instance 'geometry_msgs-msg:Point32)))
   (strips
    :reader strips
    :initarg :strips
    :type (cl:vector ros_igtl_bridge-msg:vector)
   :initform (cl:make-array 0 :element-type 'ros_igtl_bridge-msg:vector :initial-element (cl:make-instance 'ros_igtl_bridge-msg:vector)))
   (lines
    :reader lines
    :initarg :lines
    :type (cl:vector ros_igtl_bridge-msg:vector)
   :initform (cl:make-array 0 :element-type 'ros_igtl_bridge-msg:vector :initial-element (cl:make-instance 'ros_igtl_bridge-msg:vector)))
   (verts
    :reader verts
    :initarg :verts
    :type (cl:vector ros_igtl_bridge-msg:vector)
   :initform (cl:make-array 0 :element-type 'ros_igtl_bridge-msg:vector :initial-element (cl:make-instance 'ros_igtl_bridge-msg:vector))))
)

(cl:defclass igtlpolydata (<igtlpolydata>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <igtlpolydata>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'igtlpolydata)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_igtl_bridge-msg:<igtlpolydata> is deprecated: use ros_igtl_bridge-msg:igtlpolydata instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <igtlpolydata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:name-val is deprecated.  Use ros_igtl_bridge-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'points-val :lambda-list '(m))
(cl:defmethod points-val ((m <igtlpolydata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:points-val is deprecated.  Use ros_igtl_bridge-msg:points instead.")
  (points m))

(cl:ensure-generic-function 'polygons-val :lambda-list '(m))
(cl:defmethod polygons-val ((m <igtlpolydata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:polygons-val is deprecated.  Use ros_igtl_bridge-msg:polygons instead.")
  (polygons m))

(cl:ensure-generic-function 'strips-val :lambda-list '(m))
(cl:defmethod strips-val ((m <igtlpolydata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:strips-val is deprecated.  Use ros_igtl_bridge-msg:strips instead.")
  (strips m))

(cl:ensure-generic-function 'lines-val :lambda-list '(m))
(cl:defmethod lines-val ((m <igtlpolydata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:lines-val is deprecated.  Use ros_igtl_bridge-msg:lines instead.")
  (lines m))

(cl:ensure-generic-function 'verts-val :lambda-list '(m))
(cl:defmethod verts-val ((m <igtlpolydata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_igtl_bridge-msg:verts-val is deprecated.  Use ros_igtl_bridge-msg:verts instead.")
  (verts m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <igtlpolydata>) ostream)
  "Serializes a message object of type '<igtlpolydata>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'points))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'points))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'polygons))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'polygons))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'strips))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'strips))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'lines))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'lines))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'verts))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'verts))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <igtlpolydata>) istream)
  "Deserializes a message object of type '<igtlpolydata>"
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
  (cl:setf (cl:slot-value msg 'points) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'points)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geometry_msgs-msg:Point32))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'polygons) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'polygons)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geometry_msgs-msg:Point32))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'strips) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'strips)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'ros_igtl_bridge-msg:vector))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'lines) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'lines)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'ros_igtl_bridge-msg:vector))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'verts) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'verts)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'ros_igtl_bridge-msg:vector))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<igtlpolydata>)))
  "Returns string type for a message object of type '<igtlpolydata>"
  "ros_igtl_bridge/igtlpolydata")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'igtlpolydata)))
  "Returns string type for a message object of type 'igtlpolydata"
  "ros_igtl_bridge/igtlpolydata")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<igtlpolydata>)))
  "Returns md5sum for a message object of type '<igtlpolydata>"
  "8a567809576846ce15ffb57b198e0d5a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'igtlpolydata)))
  "Returns md5sum for a message object of type 'igtlpolydata"
  "8a567809576846ce15ffb57b198e0d5a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<igtlpolydata>)))
  "Returns full string definition for message of type '<igtlpolydata>"
  (cl:format cl:nil "#---PolyData Message~%~%string name~%geometry_msgs/Point32[] points~%geometry_msgs/Point32[] polygons~%vector[] strips~%vector[] lines~%vector[] verts~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%================================================================================~%MSG: ros_igtl_bridge/vector~%float32[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'igtlpolydata)))
  "Returns full string definition for message of type 'igtlpolydata"
  (cl:format cl:nil "#---PolyData Message~%~%string name~%geometry_msgs/Point32[] points~%geometry_msgs/Point32[] polygons~%vector[] strips~%vector[] lines~%vector[] verts~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%================================================================================~%MSG: ros_igtl_bridge/vector~%float32[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <igtlpolydata>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'points) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'polygons) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'strips) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'lines) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'verts) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <igtlpolydata>))
  "Converts a ROS message object to a list"
  (cl:list 'igtlpolydata
    (cl:cons ':name (name msg))
    (cl:cons ':points (points msg))
    (cl:cons ':polygons (polygons msg))
    (cl:cons ':strips (strips msg))
    (cl:cons ':lines (lines msg))
    (cl:cons ':verts (verts msg))
))
