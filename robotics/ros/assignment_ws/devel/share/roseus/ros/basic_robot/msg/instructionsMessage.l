;; Auto-generated. Do not edit!


(when (boundp 'basic_robot::instructionsMessage)
  (if (not (find-package "BASIC_ROBOT"))
    (make-package "BASIC_ROBOT"))
  (shadow 'instructionsMessage (find-package "BASIC_ROBOT")))
(unless (find-package "BASIC_ROBOT::INSTRUCTIONSMESSAGE")
  (make-package "BASIC_ROBOT::INSTRUCTIONSMESSAGE"))

(in-package "ROS")
;;//! \htmlinclude instructionsMessage.msg.html


(defclass basic_robot::instructionsMessage
  :super ros::object
  :slots (_mode _node _x _y _z _joint1 _joint2 _success _position ))

(defmethod basic_robot::instructionsMessage
  (:init
   (&key
    ((:mode __mode) "")
    ((:node __node) "")
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:joint1 __joint1) 0.0)
    ((:joint2 __joint2) 0.0)
    ((:success __success) "")
    ((:position __position) "")
    )
   (send-super :init)
   (setq _mode (string __mode))
   (setq _node (string __node))
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   (setq _joint1 (float __joint1))
   (setq _joint2 (float __joint2))
   (setq _success (string __success))
   (setq _position (string __position))
   self)
  (:mode
   (&optional __mode)
   (if __mode (setq _mode __mode)) _mode)
  (:node
   (&optional __node)
   (if __node (setq _node __node)) _node)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:joint1
   (&optional __joint1)
   (if __joint1 (setq _joint1 __joint1)) _joint1)
  (:joint2
   (&optional __joint2)
   (if __joint2 (setq _joint2 __joint2)) _joint2)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:position
   (&optional __position)
   (if __position (setq _position __position)) _position)
  (:serialization-length
   ()
   (+
    ;; string _mode
    4 (length _mode)
    ;; string _node
    4 (length _node)
    ;; float32 _x
    4
    ;; float32 _y
    4
    ;; float32 _z
    4
    ;; float32 _joint1
    4
    ;; float32 _joint2
    4
    ;; string _success
    4 (length _success)
    ;; string _position
    4 (length _position)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _mode
       (write-long (length _mode) s) (princ _mode s)
     ;; string _node
       (write-long (length _node) s) (princ _node s)
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _z
       (sys::poke _z (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _joint1
       (sys::poke _joint1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _joint2
       (sys::poke _joint2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; string _success
       (write-long (length _success) s) (princ _success s)
     ;; string _position
       (write-long (length _position) s) (princ _position s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _mode
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _mode (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _node
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _node (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _z
     (setq _z (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _joint1
     (setq _joint1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _joint2
     (setq _joint2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; string _success
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _success (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _position
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _position (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get basic_robot::instructionsMessage :md5sum-) "dce5d09282a85b8a1e1879ae10e63b6f")
(setf (get basic_robot::instructionsMessage :datatype-) "basic_robot/instructionsMessage")
(setf (get basic_robot::instructionsMessage :definition-)
      "string mode
string node
float32 x
float32 y
float32 z
float32 joint1
float32 joint2
string success
string position
")



(provide :basic_robot/instructionsMessage "dce5d09282a85b8a1e1879ae10e63b6f")


