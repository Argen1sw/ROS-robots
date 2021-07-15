import time
import first_class_test

LEFT_TRIM = 0
RIGHT_TRIM = 0

# Create an instance of the robot with the specified trim values.

robot = motorkit_robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

# Now move the robot around!
# Each call below takes two parameters:
#  - speed: The speed of the movement, a value from -1.0 to +1.0.  The higher the value
#           the faster the movement.  You need to start with a value around 0.10
#           to get enough torque to move the robot.
#  - time (seconds):  Amount of time to perform the movement.  After moving for
#                     this amount of seconds the robot will stop.  This parameter
#                     is optional and if not specified the robot will start moving
#                     forever.

robot.left(0.5, 1)
robot.right(0.5, 1)
robot.steer(0.5, 0.2)
time.sleep(3)
robot.stop()  # Stop the robot from moving.