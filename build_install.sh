#!bin/bash
set -e

sudo pip uninstall ros2bag_convert -y

python3 setup.py bdist_wheel
sudo pip install dist/ros2bag_convert-0.1.0-py3-none-any.whl
sudo rm -r build/ dist/ ros2bag_convert.egg-info/
