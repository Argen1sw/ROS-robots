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

# if __name__ == '__main__':
#     ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
#     ser.reset_input_buffer()

#     while True:
#         ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
#         ser.reset_input_buffer()
#         arduino = ser.read()
#         if arduino != b'':
#             arduino_data = int.from_bytes(arduino, byteorder='big')
#             print(arduino_data)
#             range = 30
#             #First conditional statement to move the robot forward 
#             print("starting the navigation loop")
#             if arduino_data <= 5: #Stops the robot
#                 print("robot will stop" + str(arduino_data))
#                 robot.stop()
#                 break

#             elif range <= arduino_data:
#                 print("robot forward" + str(arduino_data))
#                 robot.forward(0.2, 0.2)
#                 time.sleep(1)

#             # Second conditional statement to move the robot to the right 
#             elif range >= arduino_data:
#                 print("robot going right" + str(arduino_data))
#                 robot.right(0.2, 0.5)
#                 time.sleep(1)

#         time.sleep(2)



def CollectUltrasonic():

    if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        ser.reset_input_buffer()
        arduino = ser.read()
        if arduino != b'':
            arduino_data = int.from_bytes(arduino, byteorder='big')
            print(arduino_data)
            range = 30
            #First conditional statement to move the robot forward 
            print("starting the navigation loop")
            if arduino_data <= 5: #Stops the robot
                print("robot will stop" + str(arduino_data))
                robot.stop()
                return 0

            elif range <= arduino_data:
                print("robot forward" + str(arduino_data))
                robot.forward(0.2, 0.2)
                time.sleep(1)

            # Second conditional statement to move the robot to the right 
            elif range >= arduino_data:
                print("robot going right" + str(arduino_data))
                robot.right(0.2, 0.5)
                time.sleep(1)

        time.sleep(2)


#<---------------------------- Main code -------------------->
while True:
    CollectUltrasonic()