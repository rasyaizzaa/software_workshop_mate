import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class DepthPublisher(Node):
    def __init__(self):
        super().__init__('depth_publisher')
        self.pub = self.create_publisher(Float32, 'depth', 10)
        self.depth = 0.0
        self.timer = self.create_timer(1.0, self.tick)
    
    def tick(self):
        self.depth += random.uniform(0.0, 0.8)
        msg = Float32()
        msg.data = self.depth
        self.pub.publish(msg)
        self.get_logger().info(f'Published depth: {self.depth:.2f} m')

def main():
    rclpy.init()
    node = DepthPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()