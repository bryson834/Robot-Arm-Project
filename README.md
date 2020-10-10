# Robot-Arm-Project README

<Enter Description Here>

### How to use on Raspberry Pi and/or Linux System (*to run on windows, check below for instructions)

#### 1. Install Dependencies:

- install, git, libusb-1.0-0-dev g++ build-essential

``
sudo apt-get install git libusb-1.0-0-dev g++ build-essential
``

#### 2. Make sure you have this repository cloned to your desired location

- https://github.com/bryson834/Robot-Arm-Project.git

``
git clone https://github.com/bryson834/Robot-Arm-Project.git
``

#### 3. Make the 'Robot-Arm-Project' repo your current working directory

``
cd Robot-Arm-Project
``

#### 4. In the terminal window, type:

``
cd scripts && ./build_libpixyusb2.sh
``

``
./build_project.sh
``

``
cd ../build/build_project
``

``
sudo ./build_project
``

### ***How to use on Windows System (if applicable):

#### 1. Download Ubuntu.

- https://ubuntu.com/download/desktop

#### 2. Enable Windows Subsystem for Linux (WSL)**

- Follow the instructions in the link:

https://docs.microsoft.com/en-us/windows/wsl/install-win10

#### 3. Once WSL is enabled, open command prompt.

#### 4. Type wsl:

``
C:\...\ wsl
``

#### 5. Make sure everything is up to date, and follow steps for Raspberry Pi/Linux Systems

## **Directory Information:**

**/build:** containts the actual 'build' files needed to build project

**/misc:** contains miscellaneous files and reference information

**/scripts:** contains scripts to build the libraries & modules used for
pixy cam

**/src/common:** contains include & source files needed for pixymon 

**/src/device:** contains code (firmware) that runs on the pixy cam device

**/src/host:** contains the code that runs on your computer (arduino, header, 
and driver files)
