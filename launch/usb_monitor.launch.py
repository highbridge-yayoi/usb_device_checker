# SPDX-FileCopyrightText: 2025 highbrige-yayoi <hainu738@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

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
    # WSL2で動作確認をする為の監視リスト
    # '/dev/null', '/dev/ttys0', '/dev/dummy'