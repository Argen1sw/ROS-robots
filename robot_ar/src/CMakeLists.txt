cmake_minimum_required(VERSION 3.5)
project(robot_ar)

# Find packages and declare dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

# Add each package as a subdirectory
add_subdirectory(motor_control)
add_subdirectory(control_input)

# Install scripts and launch files
install(DIRECTORY
  motor_control/scripts
  control_input/scripts
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY
  motor_control/launch
  control_input/launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
