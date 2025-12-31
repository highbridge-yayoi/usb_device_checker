# usb_device_checker
特定のUSBデバイスの接続状態を監視するROS 2パッケージ。

## 使用方法
1. ノードを実行:
   ```bash
   ros2 run usb_device_checker usb_monitor --ros-args -p device_path:=「/dev/ttyUSB0」