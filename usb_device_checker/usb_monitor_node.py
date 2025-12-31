import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import os

class MultiUSBMonitorNode(Node):
    def __init__(self):
        super().__init__('usb_monitor_node')
        
        # 1. パラメータの宣言（デフォルトで2つのパスを指定）
        # コマンドラインやLaunchファイルからリストを上書き可能
        self.declare_parameter('device_paths', ['/dev/ttyUSB0', '/dev/video0'])
        self.declare_parameter('check_interval', 1.0)
        
        self.publisher_ = self.create_publisher(String, 'usb_status_json', 10)
        
        interval = self.get_parameter('check_interval').get_parameter_value().double_value
        self.timer = self.create_timer(interval, self.check_devices)
        
        self.get_logger().info("Multi USB Monitor started.")

    def check_devices(self):
        paths = self.get_parameter('device_paths').get_parameter_value().string_array_value
        results = {}

        for path in paths:
            # デバイスの存在チェック
            is_connected = os.path.exists(path)
            results[path] = is_connected
            
            # 切断された時だけ警告ログを出す
            if not is_connected:
                self.get_logger().warning(f"Device DISCONNECTED: {path}")

        # 結果をJSON文字列にして配信
        msg = String()
        msg.data = json.dumps(results)
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MultiUSBMonitorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
