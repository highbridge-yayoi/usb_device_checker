#!/bin/bash
# SPDX-FileCopyrightText: 2025 highbrige-yayoi <hainu738@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/ros2_ws/install/setup.bash

ros2 run usb_device_checker usb_monitor --ros-args -p device_paths:='["/dev/null"]' &
node_pid=$!

sleep 5
timeout 10 ros2 topic echo /usb_status_json | grep -q "/dev/null"

res=$?

kill $node_pid

if [ $res -eq 0 ]; then
  echo "TEST PASSED"
  exit 0