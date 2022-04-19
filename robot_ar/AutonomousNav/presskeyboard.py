#This was a attend to use the a keyboard listener/recorded so the robot can be controlled by it 
#Still I could not used because its being controlled using SSH
import time
import motor_class
from pynput.keyboard import listener



LEFT_TRIM = 0
RIGHT_TRIM = 0


# Create an instance of the robot with the specified trim values.

robot = motor_class.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)


with Listener(on_press=on_press, on_release=on_release) as listener:
   listener.join()

   def on_press(key):
      print('key pressed')

   def on_release(key):
      print('key released')