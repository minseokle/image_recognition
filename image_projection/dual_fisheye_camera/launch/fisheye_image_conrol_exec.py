# /*
#  * Copyright 2024 Myeong Jin Lee
#  *
#  * Licensed under the Apache License, Version 2.0 (the "License");
#  * you may not use this file except in compliance with the License.
#  * You may obtain a copy of the License at
#  *
#  *     http://www.apache.org/licenses/LICENSE-2.0
#  *
#  * Unless required by applicable law or agreed to in writing, software
#  * distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.
#  */
 
import os
import yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    config_dir = os.path.join(
        get_package_share_directory('dual_fisheye_camera'),
        'config',
        'sample_insta360_air.yaml'  
    )
    
    with open(config_dir, 'r') as file:
        config_params = yaml.safe_load(file)
        camera_name = config_params['/**']['ros__parameters']['camera_name']
        topic = config_params['/**']['ros__parameters']['topic']
        viewer_enabled = config_params['/**']['ros__parameters'].get('viewer', False) 
    
    node_name = f'dual_fisheye_control_node_{camera_name}'
    image_topic = f'/{camera_name}{topic}'
    image_topic_left = f'/{camera_name}/left{topic}'
    image_topic_right = f'/{camera_name}/right{topic}'
    
    launch_nodes = [
        Node(
            package='dual_fisheye_camera',
            executable='fisheye_image_control_node',
            name=node_name,  
            output='screen',
            parameters=[config_dir]
        )
    ]
    return LaunchDescription(launch_nodes)
