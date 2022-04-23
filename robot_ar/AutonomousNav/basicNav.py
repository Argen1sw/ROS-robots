from operator import truediv
import motor_class
import serial
import time
import schedule


# Basic navigation using line as a input

LEFT_TRIM = 0
RIGHT_TRIM = 0

# Create an instance of the robot with the specified trim values.

robot = motor_class.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

# Arduino Serial Port Listener


def CollectUltrasonic():

    print("Inizializing Raspberry connection with Arduino")
    arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1)
    # Define the variables that will be used for navigation
    range = 30
    arduino_data = arduino.readline()
    # distance = int(arduino_data, byteorder='big')
    distance = int.from_bytes(arduino_data, byteorder='big')
    print(distance)

    # First conditional statement to move the robot forward 
    print("starting the navigation loop")
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
    
    print('Connection closed')
    print('<--------------------------------------->')

# ------------------------------------------ MAIN NAVIGATION CODE --------------------------------------------------
print("navigation started")

schedule.every(20).seconds.do(CollectUltrasonic)

while True:
    schedule.run_pending()
    time.sleep(1)