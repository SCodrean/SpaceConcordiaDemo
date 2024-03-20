import random
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'vector_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def random_robot_position(self):
        # return (random.uniform(-100.0, 100.0))
        # return 0
        return 1
        
    def distance_calculator(self, msg):
        position_str = msg.data.split()[-1]
        position_object = float(position_str)
        print(self.random_robot_position())
        return (position_object - self.random_robot_position())

    def listener_callback(self, msg):    
        distance = self.distance_calculator(msg)
        self.get_logger().info('Distance: "%s"' % distance) 

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()