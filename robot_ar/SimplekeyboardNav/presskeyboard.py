
import time
import motor_class
import keyboard


LEFT_TRIM = 0
RIGHT_TRIM = 0


# Create an instance of the robot with the specified trim values.

robot = motor_class.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

while True:
   try:
      if keyboard.is_pressed('w'):
         robot.forward(0.3, 1)
         time.sleep(3)
      elif keyboard.is_pressed('A'):
         robot.left(0.3, 1)
         time.sleep(3)
      elif keyboard.is_pressed('D'):
         robot.right(0.3, 1)
         time.sleep(3)
      elif keyboard.is_pressed('S'):
         robot.backward(0.3, 1)
         time.sleep(3)
   except:
      break
