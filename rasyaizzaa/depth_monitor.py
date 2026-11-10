import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

LIMIT = 5.0

class DepthMonitor(Node):
    def __init__(self):
        super().__init__('depth_monitor')
        self.sub = self.create_subscription(Float32, 'depth', self.on_depth, 10)
    def on_depth(self, msg):
        if msg.data > LIMIT:
            self.get_logger().warn(f'WARNING: too deep! {msg.data:.2f} m')
        else:
            self.get_logger().info(f'Depth OK: {msg.data:.2f} m')

def main():
    rclpy.init()
    node = DepthMonitor()
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