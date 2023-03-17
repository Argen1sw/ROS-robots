import time
import first_class_test

LEFT_TRIM = 0
RIGHT_TRIM = 0

# Create an instance of the robot with the specified trim values.

robot = first_class_test.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)


robot.left(0.5, 1)
robot.right(0.5, 1)
robot.forward(0.2, 5)
time.sleep(7)
robot.stop()  # Stop the robot from moving.
