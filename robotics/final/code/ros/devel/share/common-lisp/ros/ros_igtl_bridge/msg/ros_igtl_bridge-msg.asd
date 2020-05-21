
(cl:in-package :asdf)

(defsystem "ros_igtl_bridge-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "igtlimage" :depends-on ("_package_igtlimage"))
    (:file "_package_igtlimage" :depends-on ("_package"))
    (:file "igtlpoint" :depends-on ("_package_igtlpoint"))
    (:file "_package_igtlpoint" :depends-on ("_package"))
    (:file "igtlpointcloud" :depends-on ("_package_igtlpointcloud"))
    (:file "_package_igtlpointcloud" :depends-on ("_package"))
    (:file "igtlpolydata" :depends-on ("_package_igtlpolydata"))
    (:file "_package_igtlpolydata" :depends-on ("_package"))
    (:file "igtlstring" :depends-on ("_package_igtlstring"))
    (:file "_package_igtlstring" :depends-on ("_package"))
    (:file "igtltransform" :depends-on ("_package_igtltransform"))
    (:file "_package_igtltransform" :depends-on ("_package"))
    (:file "vector" :depends-on ("_package_vector"))
    (:file "_package_vector" :depends-on ("_package"))
  ))