# Georgia Institute of Technology 
Fall 2024 Capstone Design Project
### S31-Autonomous GT Campus Navigation Drone

Highly recommend to use conda environment to control dependencies

This project is tested/built on linux operating system; ubuntu 20.04.5 LTS.

## Dependencies Installation

    $ pip install dronekit
    $ pip install pymavlink
    $ pip install MAVProxy

    ## Install GTK+3 library
    $ sudo apt update
    $ sudo apt install -y \
        libgtk-3-dev \
        libjpeg-dev \
        libtiff-dev \
        libgl1-mesa-dev \
        libglu1-mesa-dev \
        freeglut3-dev \
        libnotify-dev \
        libsdl2-2.0-0 \
        libsdl2-dev

    $ pip install matplotlib
    $ pip install wxPython

Test MAVProxy

    $ mavproxy.py --console --map

If the map and console shows up, MAVProxy is successfully installed

## Ardupilot Installation
Ardupilot repository clone & update

    $ git clone https://github.com/ArduPilot/ardupilot.git
    $ cd ardupilot
    $ git submodule update --init --recursive

STIL build

    $ ./waf configure --board sitl
    
    ## Install additional python packages
    $ python -m pip install empy==3.3.4
    $ python -m pip install pexpect
    
    ## Build may take a while
    $ ./waf build


## ROS 2 Humble with Gazebo 11 Installation
[ROS 2 Installation]
<br>Please follow the instruction provided 
<br>https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html

[Gazebo 11 Installation]
<br>Install

    $ pip curl -sSL http://get.gazebosim.org | sh
Run
    
    $ gazebo

Install Packages for ROS 2 Gazebo

    $ sudo apt update
    $ sudo apt install ros-humble-gazebo-ros-pkgs
    $ sudo apt install ros-humble-gazebo-ros2-control ros-humble-gazebo-ros2-control-demos ros-humble-gazebo-plugins

Verification

    $ ros2 launch gazebo_ros gazebo.launch.py

