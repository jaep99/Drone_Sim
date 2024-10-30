# Georgia Institute of Technology 
Fall 2024 Capstone Design Project
### S31-Autonomous GT Campus Navigation Drone


# Simulation Environment Setup
Highly recommend to use conda environment to control dependencies

This project is tested/built on linux operating system

## Dependencies Installation

    pip install dronekit
    pip install pymavlink
    pip install MAVProxy

    ## Install GTK+3 library
    sudo apt update
    sudo apt install -y \
        libgtk-3-dev \
        libjpeg-dev \
        libtiff-dev \
        libgl1-mesa-dev \
        libglu1-mesa-dev \
        freeglut3-dev \
        libnotify-dev \
        libsdl2-2.0-0 \
        libsdl2-dev

    sudo apt install python-opencv=3.2.0+dfsg-4ubuntu0.1

    pip install matplotlib
    pip install wxPython

Test MAVProxy

    mavproxy.py --console --map

If the map and console shows up, MAVProxy is successfully installed

## Ardupilot Installation
Ardupilot repository clone & update

    git clone https://github.com/ArduPilot/ardupilot.git
    cd ardupilot
    git submodule update --init --recursive

STIL build

    ./waf configure --board sitl
    
    ## Install additional python packages
    python -m pip install empy==3.3.4
    python -m pip install pexpect
    
    ## Build may take a while
    ./waf build

## QGroundControl Installation
Before installing

    sudo usermod -a -G dialout $USER
    sudo apt-get remove modemmanager -y
    sudo apt install gstreamer1.0-plugins-bad gstreamer1.0-libav gstreamer1.0-gl -y
    sudo apt install libfuse2 -y
    sudo apt install libxcb-xinerama0 libxkbcommon-x11-0 libxcb-cursor-dev -y

Logout and login to enable the changes

Download QGroundControl.AppImage from the following link
<br>https://docs.qgroundcontrol.com/master/en/qgc-user-guide/getting_started/download_and_install.html

Grant permission and run

    chmod +x ./QGroundControl.AppImage
    ./QGroundControl.AppImage  (or double click)

## Gazebo 9 Installation
[Gazebo Installation]

    sudo apt install gazebo9 libgazebo9-dev

<br>[Ardupilio-Gazebo Installation]

    git clone https://github.com/dronedojo/ardupilot_gazebo
    cd ardupilot_gazebo
    mkdir build
    cd build
    sudo apt install cmake   
    cmake ..
    make -j4
    sudo make install

## ROS Melodic Installation

    sudo sh -c ‘echo “deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main”
    > /etc/apt/sources.list.d/ros-latest.list’
    sudo apt-key adv –keyserver ‘hkp://keyserver.ubuntu.com:80’ 
    –recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
    sudo apt install ros-melodic-desktop-full

Add this to .bashrc:

    source /opt/ros/melodic/setup.bash

<br>Finish installation

    sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
    sudo apt install python-rosdep
    sudo rosdep init
    rosdep update

## Install Gazebo-Ros

    sudo apt-get install ros-melodic-gazebo-ros-pkgs ros-melodic-gazebo-ros-control





    
