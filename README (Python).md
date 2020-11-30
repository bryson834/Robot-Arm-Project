# Python Demo README

### How to use on Raspberry Pi

#### 1. Access Raspberry Pi terminal with PuTTY, VNC Viewer, or SSH (instructions below)

``
$C:/User/.../ ssh pi@<IP address>
``

#### 2. Make sure all dependencies are installed

- install git, g++, swig, libusb-1.0-0-dev build-essential

``
sudo apt-get install swig git libusb-1.0-0-dev g++ build-essential
``

#### 3. Make 'Python_Demo' you current directory

``
cd Robot-Arm-Project
``

#### 4. Build the project using these commands:

``
cd scripts && ./build_libpixyusb2.sh
``

``
./build_python_demo.sh
``

``
cd ../build
``

``
sudo python get_blocks_python_demo.py
``

#### Note: If permission denied, bash error, or any error in running *.sh files, run these commands:

``
chmod +x build_libpixyusb2.sh
``

``
chmod +x build_python_demos.sh
``

``
sed -i -e 's/\r$//' build_libpixyusb2.sh
``

``
sed -i -e 's/\r$//' build_python_demos.sh
``
