import rclpy
from rclpy.node import node
from std_msgs.msg import String
import time
import motor_class

LEFT_TRIM = 0
RIGHT_TRIM = 0


class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'move',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        robot = motor_class.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)
        """Instatiate the "motor_class" which is actually the movement of the robot"""

def listener_callback(self, msg):
        command = msg.data
        if command == 'forward':
            print('Moving forward')
            self.robot.forward()
        elif command == 'backward':
            print('Moving backward')
            self.robot.backward()
        elif command == 'left':
            print('Turning left')
            self.robot.left()
        elif command == 'right':
            print('Turning right')
            self.robot.right()
        elif command == 'stop':
            print('Stopping')
            self.robot.stop()
        else:
            print('Unknown command, stopping instead')
            self.robot.stop()

def main(args=None):
    #  initialize the wheelie node
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()

    #  wait for incoming commands
    rclpy.spin(minimal_subscriber)

    #  Interrupt detected, shut down
    minimal_subscriber.robot.stop()
    GPIO.cleanup()
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()