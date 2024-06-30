import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    params_file = LaunchConfiguration('params_file')

    return LaunchDescription([
        DeclareLaunchArgument(
            'params_file',
            default_value=os.path.join(
                get_package_share_directory('vehicle_controller'),
                'config',
                'waypoint.yaml'
            ),
            description='Path to the ROS2 parameters file to use'
        ),
        Node(
            package='vehicle_controller',
            executable='controller',
            name='vehicle_controller',
            output='screen',
            parameters=[params_file]
        ),
    ])
