;; Auto-generated. Do not edit!


(when (boundp 'ros_igtl_bridge::igtlpolydata)
  (if (not (find-package "ROS_IGTL_BRIDGE"))
    (make-package "ROS_IGTL_BRIDGE"))
  (shadow 'igtlpolydata (find-package "ROS_IGTL_BRIDGE")))
(unless (find-package "ROS_IGTL_BRIDGE::IGTLPOLYDATA")
  (make-package "ROS_IGTL_BRIDGE::IGTLPOLYDATA"))

(in-package "ROS")
;;//! \htmlinclude igtlpolydata.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass ros_igtl_bridge::igtlpolydata
  :super ros::object
  :slots (_name _points _polygons _strips _lines _verts ))

(defmethod ros_igtl_bridge::igtlpolydata
  (:init
   (&key
    ((:name __name) "")
    ((:points __points) (let (r) (dotimes (i 0) (push (instance geometry_msgs::Point32 :init) r)) r))
    ((:polygons __polygons) (let (r) (dotimes (i 0) (push (instance geometry_msgs::Point32 :init) r)) r))
    ((:strips __strips) (let (r) (dotimes (i 0) (push (instance ros_igtl_bridge::vector :init) r)) r))
    ((:lines __lines) (let (r) (dotimes (i 0) (push (instance ros_igtl_bridge::vector :init) r)) r))
    ((:verts __verts) (let (r) (dotimes (i 0) (push (instance ros_igtl_bridge::vector :init) r)) r))
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _points __points)
   (setq _polygons __polygons)
   (setq _strips __strips)
   (setq _lines __lines)
   (setq _verts __verts)
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:points
   (&rest __points)
   (if (keywordp (car __points))
       (send* _points __points)
     (progn
       (if __points (setq _points (car __points)))
       _points)))
  (:polygons
   (&rest __polygons)
   (if (keywordp (car __polygons))
       (send* _polygons __polygons)
     (progn
       (if __polygons (setq _polygons (car __polygons)))
       _polygons)))
  (:strips
   (&rest __strips)
   (if (keywordp (car __strips))
       (send* _strips __strips)
     (progn
       (if __strips (setq _strips (car __strips)))
       _strips)))
  (:lines
   (&rest __lines)
   (if (keywordp (car __lines))
       (send* _lines __lines)
     (progn
       (if __lines (setq _lines (car __lines)))
       _lines)))
  (:verts
   (&rest __verts)
   (if (keywordp (car __verts))
       (send* _verts __verts)
     (progn
       (if __verts (setq _verts (car __verts)))
       _verts)))
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; geometry_msgs/Point32[] _points
    (apply #'+ (send-all _points :serialization-length)) 4
    ;; geometry_msgs/Point32[] _polygons
    (apply #'+ (send-all _polygons :serialization-length)) 4
    ;; ros_igtl_bridge/vector[] _strips
    (apply #'+ (send-all _strips :serialization-length)) 4
    ;; ros_igtl_bridge/vector[] _lines
    (apply #'+ (send-all _lines :serialization-length)) 4
    ;; ros_igtl_bridge/vector[] _verts
    (apply #'+ (send-all _verts :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; geometry_msgs/Point32[] _points
     (write-long (length _points) s)
     (dolist (elem _points)
       (send elem :serialize s)
       )
     ;; geometry_msgs/Point32[] _polygons
     (write-long (length _polygons) s)
     (dolist (elem _polygons)
       (send elem :serialize s)
       )
     ;; ros_igtl_bridge/vector[] _strips
     (write-long (length _strips) s)
     (dolist (elem _strips)
       (send elem :serialize s)
       )
     ;; ros_igtl_bridge/vector[] _lines
     (write-long (length _lines) s)
     (dolist (elem _lines)
       (send elem :serialize s)
       )
     ;; ros_igtl_bridge/vector[] _verts
     (write-long (length _verts) s)
     (dolist (elem _verts)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; geometry_msgs/Point32[] _points
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _points (let (r) (dotimes (i n) (push (instance geometry_msgs::Point32 :init) r)) r))
     (dolist (elem- _points)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geometry_msgs/Point32[] _polygons
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _polygons (let (r) (dotimes (i n) (push (instance geometry_msgs::Point32 :init) r)) r))
     (dolist (elem- _polygons)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; ros_igtl_bridge/vector[] _strips
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _strips (let (r) (dotimes (i n) (push (instance ros_igtl_bridge::vector :init) r)) r))
     (dolist (elem- _strips)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; ros_igtl_bridge/vector[] _lines
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _lines (let (r) (dotimes (i n) (push (instance ros_igtl_bridge::vector :init) r)) r))
     (dolist (elem- _lines)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; ros_igtl_bridge/vector[] _verts
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _verts (let (r) (dotimes (i n) (push (instance ros_igtl_bridge::vector :init) r)) r))
     (dolist (elem- _verts)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get ros_igtl_bridge::igtlpolydata :md5sum-) "8a567809576846ce15ffb57b198e0d5a")
(setf (get ros_igtl_bridge::igtlpolydata :datatype-) "ros_igtl_bridge/igtlpolydata")
(setf (get ros_igtl_bridge::igtlpolydata :definition-)
      "#---PolyData Message

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

")



(provide :ros_igtl_bridge/igtlpolydata "8a567809576846ce15ffb57b198e0d5a")


