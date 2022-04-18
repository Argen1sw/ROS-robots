
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




# while True:
#    try:
#       if keyboard.is_pressed('w'):
#          robot.forward(0.3, 1)
#          time.sleep(3)
#       elif keyboard.is_pressed('A'):
#          robot.left(0.3, 1)
#          time.sleep(3)
#       elif keyboard.is_pressed('D'):
#          robot.right(0.3, 1)
#          time.sleep(3)
#       elif keyboard.is_pressed('S'):
#          robot.backward(0.3, 1)
#          time.sleep(3)
#    except:
#       break
