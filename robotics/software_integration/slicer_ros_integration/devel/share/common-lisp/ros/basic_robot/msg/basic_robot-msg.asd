
(cl:in-package :asdf)

(defsystem "basic_robot-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "instructionsMessage" :depends-on ("_package_instructionsMessage"))
    (:file "_package_instructionsMessage" :depends-on ("_package"))
  ))