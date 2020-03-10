;; Auto-generated. Do not edit!


(when (boundp 'moveit_msgs::ChangeDriftDimensions)
  (if (not (find-package "MOVEIT_MSGS"))
    (make-package "MOVEIT_MSGS"))
  (shadow 'ChangeDriftDimensions (find-package "MOVEIT_MSGS")))
(unless (find-package "MOVEIT_MSGS::CHANGEDRIFTDIMENSIONS")
  (make-package "MOVEIT_MSGS::CHANGEDRIFTDIMENSIONS"))
(unless (find-package "MOVEIT_MSGS::CHANGEDRIFTDIMENSIONSREQUEST")
  (make-package "MOVEIT_MSGS::CHANGEDRIFTDIMENSIONSREQUEST"))
(unless (find-package "MOVEIT_MSGS::CHANGEDRIFTDIMENSIONSRESPONSE")
  (make-package "MOVEIT_MSGS::CHANGEDRIFTDIMENSIONSRESPONSE"))

(in-package "ROS")

(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))




(defclass moveit_msgs::ChangeDriftDimensionsRequest
  :super ros::object
  :slots (_drift_x_translation _drift_y_translation _drift_z_translation _drift_x_rotation _drift_y_rotation _drift_z_rotation _transform_jog_frame_to_drift_frame ))

(defmethod moveit_msgs::ChangeDriftDimensionsRequest
  (:init
   (&key
    ((:drift_x_translation __drift_x_translation) nil)
    ((:drift_y_translation __drift_y_translation) nil)
    ((:drift_z_translation __drift_z_translation) nil)
    ((:drift_x_rotation __drift_x_rotation) nil)
    ((:drift_y_rotation __drift_y_rotation) nil)
    ((:drift_z_rotation __drift_z_rotation) nil)
    ((:transform_jog_frame_to_drift_frame __transform_jog_frame_to_drift_frame) (instance geometry_msgs::Transform :init))
    )
   (send-super :init)
   (setq _drift_x_translation __drift_x_translation)
   (setq _drift_y_translation __drift_y_translation)
   (setq _drift_z_translation __drift_z_translation)
   (setq _drift_x_rotation __drift_x_rotation)
   (setq _drift_y_rotation __drift_y_rotation)
   (setq _drift_z_rotation __drift_z_rotation)
   (setq _transform_jog_frame_to_drift_frame __transform_jog_frame_to_drift_frame)
   self)
  (:drift_x_translation
   (&optional __drift_x_translation)
   (if __drift_x_translation (setq _drift_x_translation __drift_x_translation)) _drift_x_translation)
  (:drift_y_translation
   (&optional __drift_y_translation)
   (if __drift_y_translation (setq _drift_y_translation __drift_y_translation)) _drift_y_translation)
  (:drift_z_translation
   (&optional __drift_z_translation)
   (if __drift_z_translation (setq _drift_z_translation __drift_z_translation)) _drift_z_translation)
  (:drift_x_rotation
   (&optional __drift_x_rotation)
   (if __drift_x_rotation (setq _drift_x_rotation __drift_x_rotation)) _drift_x_rotation)
  (:drift_y_rotation
   (&optional __drift_y_rotation)
   (if __drift_y_rotation (setq _drift_y_rotation __drift_y_rotation)) _drift_y_rotation)
  (:drift_z_rotation
   (&optional __drift_z_rotation)
   (if __drift_z_rotation (setq _drift_z_rotation __drift_z_rotation)) _drift_z_rotation)
  (:transform_jog_frame_to_drift_frame
   (&rest __transform_jog_frame_to_drift_frame)
   (if (keywordp (car __transform_jog_frame_to_drift_frame))
       (send* _transform_jog_frame_to_drift_frame __transform_jog_frame_to_drift_frame)
     (progn
       (if __transform_jog_frame_to_drift_frame (setq _transform_jog_frame_to_drift_frame (car __transform_jog_frame_to_drift_frame)))
       _transform_jog_frame_to_drift_frame)))
  (:serialization-length
   ()
   (+
    ;; bool _drift_x_translation
    1
    ;; bool _drift_y_translation
    1
    ;; bool _drift_z_translation
    1
    ;; bool _drift_x_rotation
    1
    ;; bool _drift_y_rotation
    1
    ;; bool _drift_z_rotation
    1
    ;; geometry_msgs/Transform _transform_jog_frame_to_drift_frame
    (send _transform_jog_frame_to_drift_frame :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _drift_x_translation
       (if _drift_x_translation (write-byte -1 s) (write-byte 0 s))
     ;; bool _drift_y_translation
       (if _drift_y_translation (write-byte -1 s) (write-byte 0 s))
     ;; bool _drift_z_translation
       (if _drift_z_translation (write-byte -1 s) (write-byte 0 s))
     ;; bool _drift_x_rotation
       (if _drift_x_rotation (write-byte -1 s) (write-byte 0 s))
     ;; bool _drift_y_rotation
       (if _drift_y_rotation (write-byte -1 s) (write-byte 0 s))
     ;; bool _drift_z_rotation
       (if _drift_z_rotation (write-byte -1 s) (write-byte 0 s))
     ;; geometry_msgs/Transform _transform_jog_frame_to_drift_frame
       (send _transform_jog_frame_to_drift_frame :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _drift_x_translation
     (setq _drift_x_translation (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _drift_y_translation
     (setq _drift_y_translation (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _drift_z_translation
     (setq _drift_z_translation (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _drift_x_rotation
     (setq _drift_x_rotation (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _drift_y_rotation
     (setq _drift_y_rotation (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _drift_z_rotation
     (setq _drift_z_rotation (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; geometry_msgs/Transform _transform_jog_frame_to_drift_frame
     (send _transform_jog_frame_to_drift_frame :deserialize buf ptr-) (incf ptr- (send _transform_jog_frame_to_drift_frame :serialization-length))
   ;;
   self)
  )

(defclass moveit_msgs::ChangeDriftDimensionsResponse
  :super ros::object
  :slots (_success ))

(defmethod moveit_msgs::ChangeDriftDimensionsResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass moveit_msgs::ChangeDriftDimensions
  :super ros::object
  :slots ())

(setf (get moveit_msgs::ChangeDriftDimensions :md5sum-) "0d34c8d563fea2efff65829c37132a15")
(setf (get moveit_msgs::ChangeDriftDimensions :datatype-) "moveit_msgs/ChangeDriftDimensions")
(setf (get moveit_msgs::ChangeDriftDimensions :request) moveit_msgs::ChangeDriftDimensionsRequest)
(setf (get moveit_msgs::ChangeDriftDimensions :response) moveit_msgs::ChangeDriftDimensionsResponse)

(defmethod moveit_msgs::ChangeDriftDimensionsRequest
  (:response () (instance moveit_msgs::ChangeDriftDimensionsResponse :init)))

(setf (get moveit_msgs::ChangeDriftDimensionsRequest :md5sum-) "0d34c8d563fea2efff65829c37132a15")
(setf (get moveit_msgs::ChangeDriftDimensionsRequest :datatype-) "moveit_msgs/ChangeDriftDimensionsRequest")
(setf (get moveit_msgs::ChangeDriftDimensionsRequest :definition-)
      "




bool drift_x_translation
bool drift_y_translation
bool drift_z_translation
bool drift_x_rotation
bool drift_y_rotation
bool drift_z_rotation



geometry_msgs/Transform transform_jog_frame_to_drift_frame

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
---
bool success

")

(setf (get moveit_msgs::ChangeDriftDimensionsResponse :md5sum-) "0d34c8d563fea2efff65829c37132a15")
(setf (get moveit_msgs::ChangeDriftDimensionsResponse :datatype-) "moveit_msgs/ChangeDriftDimensionsResponse")
(setf (get moveit_msgs::ChangeDriftDimensionsResponse :definition-)
      "




bool drift_x_translation
bool drift_y_translation
bool drift_z_translation
bool drift_x_rotation
bool drift_y_rotation
bool drift_z_rotation



geometry_msgs/Transform transform_jog_frame_to_drift_frame

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
---
bool success

")



(provide :moveit_msgs/ChangeDriftDimensions "0d34c8d563fea2efff65829c37132a15")


