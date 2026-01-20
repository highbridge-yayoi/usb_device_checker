![test](https://github.com/highbridge-yayoi/usb_device_checker/actions/workflows/test.yml/badge.svg)
# usb_device_checker
特定のUSBデバイスの接続状態を監視するノードを含むROS 2パッケージ．
## 概要
指定したデバイスパス（例：`/dev/ttyUSB0`）の存在を確認し，接続状態に変化があった場合にログを表示すると同時に，現在のステータスをJSON形式で配信します．

## 内容
- USBチェッカー
- launchファイルをによる入力の簡易化

## 使用方法
1. ノードを実行:
   ```bash
   $ ros2 run usb_device_checker usb_monitor --ros-args -p device_path:=「/dev/ttyUSB0」
   ```
2. 別ターミナルでROS 2のトピックを確認:
   ```bash
   $ ros2 topic echo /usb_status_json
   data: '{"/dev/null": true, "/dev/ttys0": false, "/dev/dummy": false}'
   ---
   ```

## ノードとトピックの一覧
### ノード
- **usb_monitor_node**: 指定されたデバイスパスの存在を監視し、結果を配信します.

### 配信トピック
- **/usb_status_json** ([std_msgs/String]): 監視対象の接続状態をJSON形式で配信します.

### パラメータ
- **device_paths** (string_array): 監視するデバイスパスのリスト.
- **check_interval** (double): 監視の周期（秒）.

## 動作不良について
- WSL2環境では，USBデバイスの接続状態を監視することができない可能性があります．
    - 「USBデバイスをWSL2へ転送するツール」を使用して，WSL2内でUSBデバイスを認識する必要があります．
    - 動作確認がしたいだけなら，launch/usb_monitor.launch.py の device_paths を書き換えてください．

## 動作環境
- OS: Ubuntu 22.04 (WSL2 動作確認済み)
- ROS 2: Humble / Iron / Rolling
- 言語: Python 3

## 権利関係
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布及び使用が許可されます．
- © 2025 ryo takahashi