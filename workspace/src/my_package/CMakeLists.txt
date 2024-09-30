cmake_minimum_required(VERSION 3.0.3)
project(my_package)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

add_message_files(
  FILES
  Num.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

# Create a catkin package
catkin_package(
  CATKIN_DEPENDS message_runtime
)