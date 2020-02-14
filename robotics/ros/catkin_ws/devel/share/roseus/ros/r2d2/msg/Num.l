;; Auto-generated. Do not edit!


(when (boundp 'r2d2::Num)
  (if (not (find-package "R2D2"))
    (make-package "R2D2"))
  (shadow 'Num (find-package "R2D2")))
(unless (find-package "R2D2::NUM")
  (make-package "R2D2::NUM"))

(in-package "ROS")
;;//! \htmlinclude Num.msg.html


(defclass r2d2::Num
  :super ros::object
  :slots (_msg ))

(defmethod r2d2::Num
  (:init
   (&key
    ((:msg __msg) 0)
    )
   (send-super :init)
   (setq _msg (round __msg))
   self)
  (:msg
   (&optional __msg)
   (if __msg (setq _msg __msg)) _msg)
  (:serialization-length
   ()
   (+
    ;; int64 _msg
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _msg
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _msg (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _msg) (= (length (_msg . bv)) 2)) ;; bignum
              (write-long (ash (elt (_msg . bv) 0) 0) s)
              (write-long (ash (elt (_msg . bv) 1) -1) s))
             ((and (class _msg) (= (length (_msg . bv)) 1)) ;; big1
              (write-long (elt (_msg . bv) 0) s)
              (write-long (if (>= _msg 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _msg s)(write-long (if (>= _msg 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _msg
#+(or :alpha :irix6 :x86_64)
      (setf _msg (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _msg (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(setf (get r2d2::Num :md5sum-) "97ee05ea4c4bbaede097b37470a3a7c6")
(setf (get r2d2::Num :datatype-) "r2d2/Num")
(setf (get r2d2::Num :definition-)
      "int64 msg

")



(provide :r2d2/Num "97ee05ea4c4bbaede097b37470a3a7c6")


