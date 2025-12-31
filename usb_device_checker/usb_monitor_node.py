import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import os

class USBMonitorNode(Node):
    def __init__(self):
        super().__init__('usb_monitor_node')
        
        # 1. パラメータの宣言（監視したいデバイスパスとチェック間隔）
        self.declare_parameter('device_path', '/dev/ttyUSB0')
        self.declare_parameter('check_interval', 1.0) # 秒
        
        # 2. パブリッシャーの作成（トピック名: /usb_status）
        self.publisher_ = self.create_publisher(Bool, 'usb_status', 10)
        
        # 3. タイマーの作成（定期的にチェック）
        interval = self.get_parameter('check_interval').get_parameter_value().double_value
        self.timer = self.create_timer(interval, self.check_device)
        
        self.get_logger().info(f'USB Monitor Node started. Checking: {self.get_parameter("device_path").value}')

    def check_device(self):
        path = self.get_parameter('device_path').get_parameter_value().string_value
        msg = Bool()
        
        # デバイスファイルが存在するか確認
        if os.path.exists(path):
            msg.data = True
        else:
            msg.data = False
        
        self.publisher_.publish(msg)
        
        # ログ出力（デバッグ用）
        status = "Connected" if msg.data else "Disconnected"
        self.get_logger().debug(f'Device {path}: {status}')

def main(args=None):
    rclpy.init(args=args)
    node = USBMonitorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
