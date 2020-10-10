# Robot-Arm-Project README

## How to Build and Run??

### How to use on Raspberry Pi and/or Linux System (*to run on windows, check below for instructions)

1. Install Dependencies
    - install, git, libusb-1.0-0-dev g++ build-essential
    
    ``
    sudo apt-get install git libusb-1.0-0-dev g++ build-essential
    ``

2. Make sure you have this repository cloned
    - https://github.com/bryson834/Robot-Arm-Project.git

    ``
    git clone https://github.com/bryson834/Robot-Arm-Project.git
    ``
3. Make the location of the repo your current working directory

4. In the terminal window, type:

    ``
    cd Robot-Arm-Project && ./build_libpixyusb2.sh
    ``

    ``
    ./build_project
    ``

    ``
    cd ../build/mainfunction
    ``

    ``
    sudo ./build_project
    ``




``
hello world
``



Directory Information:

/build: containts the actual 'build' files needed to build project

/misc: contains miscellaneous files and reference information

/scripts: contains scripts to build the libraries & modules used for
pixy cam

/src/common: contains include & source files needed for pixymon 

/src/device: contains code (firmware) that runs on the pixy cam device

/src/host: contains the code that runs on your computer (arduino, header, 
and driver files)

