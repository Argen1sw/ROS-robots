import motor_class
import serial
import time


# Basic navigation using line as a input

LEFT_TRIM = 0
RIGHT_TRIM = 0

# Create an instance of the robot with the specified trim values.

robot = motor_class.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

# Arduino Serial Port Listener
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        # Define the variables that will be used for navigation
        range = 30
        number = ser.read()

        if number != b'':
            distance = int.from_bytes(number, byteorder='big')
            # First conditional statement to move the robot forward 
            if range >= distance:
                print("robot forward" + distance)
                time.sleep(1)

            # Second conditional statement to move the robot to the right 
            elif range <= distance:
                print("robot going right" + distance)
                time.sleep(1)

            elif 5 <= distance: #Stops the robot
                print("robot will stop" + distance)
                robot.stop()
                break


#Loop that runs the code that will register the keyboard entry