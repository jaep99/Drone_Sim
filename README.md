# Georgia Institute of Technology 
Fall 2024 Capstone Design Project
### S31-Autonomous GT Campus Navigation Drone


# Simulation Environment Setup
Highly recommend to use conda environment to control dependencies

This project is tested/built on linux operating system; ubuntu 20.04.5 LTS.

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

## ROS 2 Iron with Gazebo Garden Installation
[ROS 2 Installation]
<br>Please follow the instruction provided 
<br>https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html

[Gazebo Installation]
<br>Install

    pip curl -sSL http://get.gazebosim.org | sh
Run
    
    gazebo

Install Packages for ROS 2 Gazebo 

    sudo apt update
    sudo apt install ros-humble-gazebo-ros-pkgs
    sudo apt install ros-humble-gazebo-ros2-control ros-humble-gazebo-ros2-control-demos ros-humble-gazebo-plugins

    # dependencies install
    sudo apt update
    sudo apt install libgz-sim7-dev rapidjson-dev
    sudo apt install libopencv-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev gstreamer1.0-plugins-bad gstreamer1.0-libav gstreamer1.0-gl

## Ardupilot Gazebo plug-in Installation

    git clone https://github.com/ArduPilot/ardupilot_gazebo.git
    # cd ardupilot_gazebo
    mkdir build
    cd build
    
    ## cmake build
    cmake ..
    make
    sudo make install

(gtnavdrone) hyeonjae@hyeonjae-ubuntu:~/Desktop/Drone_Sim/ardupilot_gazebo$ gz sim -v4 -r --render-engine ogre iris_runway.sdf
(gtnavdrone) hyeonjae@hyeonjae-ubuntu:~/Desktop/Drone_Sim/ardupilot/ArduCopter$ ../Tools/autotest/sim_vehicle.py -v ArduCopter -f gazebo-iris --model JSON --map --console

    
