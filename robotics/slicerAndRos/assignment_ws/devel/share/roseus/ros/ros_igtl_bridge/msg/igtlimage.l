;; Auto-generated. Do not edit!


(when (boundp 'ros_igtl_bridge::igtlimage)
  (if (not (find-package "ROS_IGTL_BRIDGE"))
    (make-package "ROS_IGTL_BRIDGE"))
  (shadow 'igtlimage (find-package "ROS_IGTL_BRIDGE")))
(unless (find-package "ROS_IGTL_BRIDGE::IGTLIMAGE")
  (make-package "ROS_IGTL_BRIDGE::IGTLIMAGE"))

(in-package "ROS")
;;//! \htmlinclude igtlimage.msg.html


(defclass ros_igtl_bridge::igtlimage
  :super ros::object
  :slots (_name _x_steps _y_steps _z_steps _x_spacing _y_spacing _z_spacing _data ))

(defmethod ros_igtl_bridge::igtlimage
  (:init
   (&key
    ((:name __name) "")
    ((:x_steps __x_steps) 0)
    ((:y_steps __y_steps) 0)
    ((:z_steps __z_steps) 0)
    ((:x_spacing __x_spacing) 0.0)
    ((:y_spacing __y_spacing) 0.0)
    ((:z_spacing __z_spacing) 0.0)
    ((:data __data) (make-array 0 :initial-element 0 :element-type :char))
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _x_steps (round __x_steps))
   (setq _y_steps (round __y_steps))
   (setq _z_steps (round __z_steps))
   (setq _x_spacing (float __x_spacing))
   (setq _y_spacing (float __y_spacing))
   (setq _z_spacing (float __z_spacing))
   (setq _data __data)
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:x_steps
   (&optional __x_steps)
   (if __x_steps (setq _x_steps __x_steps)) _x_steps)
  (:y_steps
   (&optional __y_steps)
   (if __y_steps (setq _y_steps __y_steps)) _y_steps)
  (:z_steps
   (&optional __z_steps)
   (if __z_steps (setq _z_steps __z_steps)) _z_steps)
  (:x_spacing
   (&optional __x_spacing)
   (if __x_spacing (setq _x_spacing __x_spacing)) _x_spacing)
  (:y_spacing
   (&optional __y_spacing)
   (if __y_spacing (setq _y_spacing __y_spacing)) _y_spacing)
  (:z_spacing
   (&optional __z_spacing)
   (if __z_spacing (setq _z_spacing __z_spacing)) _z_spacing)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; int32 _x_steps
    4
    ;; int32 _y_steps
    4
    ;; int32 _z_steps
    4
    ;; float32 _x_spacing
    4
    ;; float32 _y_spacing
    4
    ;; float32 _z_spacing
    4
    ;; uint8[] _data
    (* 1    (length _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; int32 _x_steps
       (write-long _x_steps s)
     ;; int32 _y_steps
       (write-long _y_steps s)
     ;; int32 _z_steps
       (write-long _z_steps s)
     ;; float32 _x_spacing
       (sys::poke _x_spacing (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y_spacing
       (sys::poke _y_spacing (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _z_spacing
       (sys::poke _z_spacing (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; uint8[] _data
     (write-long (length _data) s)
     (princ _data s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int32 _x_steps
     (setq _x_steps (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _y_steps
     (setq _y_steps (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _z_steps
     (setq _z_steps (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _x_spacing
     (setq _x_spacing (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y_spacing
     (setq _y_spacing (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _z_spacing
     (setq _z_spacing (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; uint8[] _data
   (let ((n (sys::peek buf ptr- :integer))) (incf ptr- 4)
     (setq _data (make-array n :element-type :char))
     (replace _data buf :start2 ptr-) (incf ptr- n))
   ;;
   self)
  )

(setf (get ros_igtl_bridge::igtlimage :md5sum-) "e004951b468cda99488e8b1294df4cef")
(setf (get ros_igtl_bridge::igtlimage :datatype-) "ros_igtl_bridge/igtlimage")
(setf (get ros_igtl_bridge::igtlimage :definition-)
      "# Image Message
string name
# Steps
int32 x_steps           
int32 y_steps           
int32 z_steps        

float32 x_spacing           
float32 y_spacing           
float32 z_spacing           

#sensor_msgs/Image rosimg
# Image data
uint8[] data		  

")



(provide :ros_igtl_bridge/igtlimage "e004951b468cda99488e8b1294df4cef")


