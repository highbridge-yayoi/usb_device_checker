from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='usb_device_checker',
            executable='usb_monitor',
            name='usb_monitor_node',
            parameters=[{
                'device_paths': ['/dev/ttyUSB0', '/dev/video0', '/dev/ttyACM0'], # 監視したいリスト
                'check_interval': 0.5  # チェック間隔（秒）
            }],
            output='screen'
        )
    ])