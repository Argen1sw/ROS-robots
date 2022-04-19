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
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            
            # Define the variables that will be used for navigation
            int(line)
            range = 30

            # First conditional statement to move the robot forward 
            if range >= line:
                print("robot forward")
                time.sleep(1)

            # Second conditional statement to move the robot to the right 
            elif range <= line:
                print("robot going right")
                time.sleep(1)

            elif 30 == 'E' | 5 <= line: #Stops the robot
                robot.stop()
                break


#Loop that runs the code that will register the keyboard entry