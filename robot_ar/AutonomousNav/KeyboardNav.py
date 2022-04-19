# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple two DC motor robot class usage example.
# Author: Tony DiCola, Chris Anderron
# License: MIT License https://opensource.org/licenses/MIT
import time

# Import the motorkit_robot.py file (must be in the same directory as this file!).
import motor_class


# Set the trim offset for each motor (left and right).  This is a value that
# will offset the speed of movement of each motor in order to make them both
# move at the same desired speed.  Because there's no feedback the robot doesn't
# know how fast each motor is spinning and the robot can pull to a side if one
# motor spins faster than the other motor.  To determine the trim values move the
# robot forward slowly (around 100 speed) and watch if it veers to the left or
# right.  If it veers left then the _right_ motor is spinning faster so try
# setting RIGHT_TRIM to a small negative value, like -0.05, to slow down the right
# motor.  Likewise if it veers right then adjust the _left_ motor trim to a small
# negative value.  Increase or decrease the trim value until the bot moves
# straight forward/backward.
LEFT_TRIM = 0
RIGHT_TRIM = 0


# Create an instance of the robot with the specified trim values.

robot = motor_class.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

#Loop that runs the code that will register the keyboard entry
while True:
   print('W = Forward; A = Left; D = Right; S = Backward Press E to exit')
   displacement = input()
   if displacement == 'W': #Displace the robot forward at 0.3 speed for 1 second 
      robot.forward(-0.3, 0.5) 
      time.sleep(1)
   elif displacement == 'A': #Displace the robot left at 0.3 speed for 1 second 
      robot.left(-0.3, 0.5)
      time.sleep(1)
   elif displacement == 'D':  #Displace the robot right at 0.3 speed for 1 second 
      robot.right(-0.3, 0.5)
      time.sleep(1)
   elif displacement == 'S': #Displace the robot backward at 0.3 speed for 1 second 
      robot.backward(-0.3, 0.5)
      time.sleep(1)
   elif displacement == 'E': #Stops the robot
      robot.stop()
      break