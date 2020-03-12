;; Auto-generated. Do not edit!


(when (boundp 'ros_igtl_bridge::igtltransform)
  (if (not (find-package "ROS_IGTL_BRIDGE"))
    (make-package "ROS_IGTL_BRIDGE"))
  (shadow 'igtltransform (find-package "ROS_IGTL_BRIDGE")))
(unless (find-package "ROS_IGTL_BRIDGE::IGTLTRANSFORM")
  (make-package "ROS_IGTL_BRIDGE::IGTLTRANSFORM"))

(in-package "ROS")
;;//! \htmlinclude igtltransform.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass ros_igtl_bridge::igtltransform
  :super ros::object
  :slots (_name _transform ))

(defmethod ros_igtl_bridge::igtltransform
  (:init
   (&key
    ((:name __name) "")
    ((:transform __transform) (instance geometry_msgs::Transform :init))
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _transform __transform)
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:transform
   (&rest __transform)
   (if (keywordp (car __transform))
       (send* _transform __transform)
     (progn
       (if __transform (setq _transform (car __transform)))
       _transform)))
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; geometry_msgs/Transform _transform
    (send _transform :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; geometry_msgs/Transform _transform
       (send _transform :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; geometry_msgs/Transform _transform
     (send _transform :deserialize buf ptr-) (incf ptr- (send _transform :serialization-length))
   ;;
   self)
  )

(setf (get ros_igtl_bridge::igtltransform :md5sum-) "5b37f5c9159d09ed0eb53ad625b51f59")
(setf (get ros_igtl_bridge::igtltransform :datatype-) "ros_igtl_bridge/igtltransform")
(setf (get ros_igtl_bridge::igtltransform :definition-)
      "#---Transform Message
 
string name
geometry_msgs/Transform transform

================================================================================
MSG: geometry_msgs/Transform
# This represents the transform between two coordinate frames in free space.

Vector3 translation
Quaternion rotation

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :ros_igtl_bridge/igtltransform "5b37f5c9159d09ed0eb53ad625b51f59")


