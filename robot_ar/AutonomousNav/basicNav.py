from operator import truediv
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
        arduino = ser.read()
        if arduino != b'':
            arduino_data = int.from_bytes(arduino, byteorder='big')
            print(arduino_data)
            range = 30
            #First conditional statement to move the robot forward 
            print("starting the navigation loop")
            if range >= arduino_data:
                print("robot forward" + arduino_data)
                time.sleep(1)

            # Second conditional statement to move the robot to the right 
            elif range <= arduino_data:
                print("robot going right" + arduino_data)
                time.sleep(1)

            elif 5 <= arduino_data: #Stops the robot
                print("robot will stop" + arduino_data)
                robot.stop()








# def CollectUltrasonic():

#     print("Inizializing Raspberry connection with Arduino")
#     arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1)
#     arduino.reset_input_buffer()
#     # Define the variables that will be used for navigation
#     range = 30
#     if arduino.in_waiting > 0:
#         arduino_data = arduino.readline().decode('utf-8')
#         print(arduino_data)
#         distance = int(arduino_data)

#         # First conditional statement to move the robot forward 
#         print("starting the navigation loop")
#         if range >= distance:
#             print("robot forward" + distance)
#             time.sleep(1)

#         # Second conditional statement to move the robot to the right 
#         elif range <= distance:
#             print("robot going right" + distance)
#             time.sleep(1)

#         elif 5 <= distance: #Stops the robot
#             print("robot will stop" + distance)
#             robot.stop()
    
#     print('Connection closed')
#     print('<--------------------------------------->')

# # ------------------------------------------ MAIN NAVIGATION CODE --------------------------------------------------
# print("navigation started")

# schedule.every(20).seconds.do(CollectUltrasonic)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
