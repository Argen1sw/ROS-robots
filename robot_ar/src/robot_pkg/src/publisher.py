#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Int16

def input_publisher():
    pub = rospy.Publisher('user_output', Int16, queue_size=10)
    rospy.init_node('input_publisher')
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        user_output = 1
        pub.publish(user_output)
        rate.sleep()

if __name__ == '__main__':
    try:
        input_publisher()
    except rospy.ROSInterruptException:
        pass
