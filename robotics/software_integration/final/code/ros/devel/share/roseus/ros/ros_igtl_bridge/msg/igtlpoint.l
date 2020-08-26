;; Auto-generated. Do not edit!


(when (boundp 'ros_igtl_bridge::igtlpoint)
  (if (not (find-package "ROS_IGTL_BRIDGE"))
    (make-package "ROS_IGTL_BRIDGE"))
  (shadow 'igtlpoint (find-package "ROS_IGTL_BRIDGE")))
(unless (find-package "ROS_IGTL_BRIDGE::IGTLPOINT")
  (make-package "ROS_IGTL_BRIDGE::IGTLPOINT"))

(in-package "ROS")
;;//! \htmlinclude igtlpoint.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass ros_igtl_bridge::igtlpoint
  :super ros::object
  :slots (_name _pointdata ))

(defmethod ros_igtl_bridge::igtlpoint
  (:init
   (&key
    ((:name __name) "")
    ((:pointdata __pointdata) (instance geometry_msgs::Point :init))
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _pointdata __pointdata)
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:pointdata
   (&rest __pointdata)
   (if (keywordp (car __pointdata))
       (send* _pointdata __pointdata)
     (progn
       (if __pointdata (setq _pointdata (car __pointdata)))
       _pointdata)))
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; geometry_msgs/Point _pointdata
    (send _pointdata :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; geometry_msgs/Point _pointdata
       (send _pointdata :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; geometry_msgs/Point _pointdata
     (send _pointdata :deserialize buf ptr-) (incf ptr- (send _pointdata :serialization-length))
   ;;
   self)
  )

(setf (get ros_igtl_bridge::igtlpoint :md5sum-) "fb1f671d9b816bd5dbd3deb4a0885963")
(setf (get ros_igtl_bridge::igtlpoint :datatype-) "ros_igtl_bridge/igtlpoint")
(setf (get ros_igtl_bridge::igtlpoint :definition-)
      "#---Point Message

string name
geometry_msgs/Point pointdata

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :ros_igtl_bridge/igtlpoint "fb1f671d9b816bd5dbd3deb4a0885963")


