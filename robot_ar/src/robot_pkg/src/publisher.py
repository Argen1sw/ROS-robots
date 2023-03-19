#!/usr/bin/env python3

import rospy
import inputs
from std_msgs.msg import Int16


def input_publisher():
    pub = rospy.Publisher('user_output', Int16, queue_size=10)
    rospy.init_node('input_publisher')
    rate = rospy.Rate(10)

    devices = inputs.devices.gamepads
    print(f"Connected devices: {devices}")
    gamepad = inputs.devices.gamepads[0]

    while not rospy.is_shutdown():
        user_output = 0
        events = gamepad.read()
        for event in events:
            print("Loop is working")
            if event.code == "ABS_HAT0Y" and event.state < 0:
                user_output = 1
            elif event.code == "ABS_HAT0Y" and event.state > 0:
                user_output = 2
            elif event.code == "ABS_HAT0X" and event.state > 0:
                user_output = 3
            elif event.code == "ABS_HAT0X" and event.state < 0:
                user_output = 4
            else:
                user_output = 0

        pub.publish(user_output)
        rate.sleep()

if __name__ == '__main__':
    try:
        input_publisher()
    except rospy.ROSInterruptException:
        pass
