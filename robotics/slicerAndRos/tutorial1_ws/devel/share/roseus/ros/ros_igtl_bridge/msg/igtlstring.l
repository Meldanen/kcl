;; Auto-generated. Do not edit!


(when (boundp 'ros_igtl_bridge::igtlstring)
  (if (not (find-package "ROS_IGTL_BRIDGE"))
    (make-package "ROS_IGTL_BRIDGE"))
  (shadow 'igtlstring (find-package "ROS_IGTL_BRIDGE")))
(unless (find-package "ROS_IGTL_BRIDGE::IGTLSTRING")
  (make-package "ROS_IGTL_BRIDGE::IGTLSTRING"))

(in-package "ROS")
;;//! \htmlinclude igtlstring.msg.html


(defclass ros_igtl_bridge::igtlstring
  :super ros::object
  :slots (_name _data ))

(defmethod ros_igtl_bridge::igtlstring
  (:init
   (&key
    ((:name __name) "")
    ((:data __data) "")
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _data (string __data))
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; string _data
    4 (length _data)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; string _data
       (write-long (length _data) s) (princ _data s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _data
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _data (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get ros_igtl_bridge::igtlstring :md5sum-) "0a150dc399b6cef3706553ca3c336ddf")
(setf (get ros_igtl_bridge::igtlstring :datatype-) "ros_igtl_bridge/igtlstring")
(setf (get ros_igtl_bridge::igtlstring :definition-)
      "#---String Message

string name
string data

")



(provide :ros_igtl_bridge/igtlstring "0a150dc399b6cef3706553ca3c336ddf")


