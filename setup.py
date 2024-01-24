from setuptools import setup

package_name = 'ros2bag_convert'

setup(
    name=package_name,
    version='0.1.0',
    packages=["ros2bag_convert.ros2bag_convert","ros2bag_convert"],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lee',
    maintainer_email='zwlee1714@gmail.com',
    description='Convert ROS2 bag files to CSV, JSON, etc. ',
    license='MIT License (MIT)',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "ros2bag-convert = ros2bag_convert.main:main",
        ],
    },
)
