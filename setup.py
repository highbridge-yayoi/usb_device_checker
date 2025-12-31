# SPDX-FileCopyrightText: 2025 highbrige-yayoi <hainu738@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'usb_device_checker'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ryi',
    maintainer_email='hainu738@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'usb_monitor = usb_device_checker.usb_monitor_node:main'
        ],
    },
)
