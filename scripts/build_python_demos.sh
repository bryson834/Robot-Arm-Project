#!/bin/bash

function WHITE_TEXT {
  printf "\033[1;37m"
}
function NORMAL_TEXT {
  printf "\033[0m"
}
function GREEN_TEXT {
  printf "\033[1;32m"
}
function RED_TEXT {
  printf "\033[1;31m"
}

WHITE_TEXT
echo "########################################################################################"
echo "# Building Python Demo...                                                      #"
echo "########################################################################################"
NORMAL_TEXT

uname -a

TARGET_BUILD_FOLDER=../build

mkdir $TARGET_BUILD_FOLDER

cd ../src/host/python_demos

swig -c++ -python pixy.i
python swig.dat build_ext --inplace -D__LINUX__

files=(../../../build/*.so)
if (( ${#files[@]} )); then
  rm ../../../build/*.so
fi

cp * ../../../build

files=(../../../build/*.so)
if (( ${#files[@]} )); then
  GREEN_TEXT
  printf "SUCCESS "
else
  RED_TEXT
  printf "FAILURE "
fi
echo ""
