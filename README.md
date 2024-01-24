# ros2bag_convert

[中文](README.md) | [English](README_EN.md)

**将ROS2的Bag文件转换为CSV。**

## 一、安装

下载并用以下的命令安装.

```
cd ros2_convert
python3 setup.py bdist_wheel
sudo pip install dist/ros2bag_convert-0.1.0-py3-none-any.whl
echo 'export PATH=$PATH:/usr/lib/ros2bag_convert' >> ~/.bashrc
source ~/.bashrc
```

可以用``build_install.sh``进行安装

```
bash build_install.sh
```

## 二、使用

目前仅支持将数据转换为csv格式，结果将输出到`xxx.db3`同级目录。

```
ros2bag-convert xxxx.db3
```

### 测试指令

#### 手动发布Pose数据

```
ros2 topic pub test geometry_msgs/msg/Pose  '{position:{x: 0.0,y: 0.0,z: 0.0}, orientation: {x: 0.0,y: 0.0,z: 0.0,w: 1.0}}'
```

#### 记录

```
ros2 bag record test
```

#### 转换

```
ros2bag-convert xxxx.db3
```

## 版本记录

- 20240124 
  - 完成了bag话题的基本转化和嵌套列表的转化
