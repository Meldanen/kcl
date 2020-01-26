cmake_minimum_required(VERSION 3.5)

project(Assignment1)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "http://slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/Assignment1")
set(EXTENSION_CATEGORY "Examples")
set(EXTENSION_CONTRIBUTORS "Alexandros Megalemos (N/A)")
set(EXTENSION_DESCRIPTION "Assignment 1 ")
set(EXTENSION_ICONURL "http://www.example.com/Slicer/Extensions/Assignment1.png")
set(EXTENSION_SCREENSHOTURLS "http://www.example.com/Slicer/Extensions/Assignment1/Screenshots/1.png")
set(EXTENSION_DEPENDS "NA") # Specified as a space separated string, a list or 'NA' if any

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
