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
echo "# Building Get Blocks CPP Demo...                                                      #"
echo "########################################################################################"
NORMAL_TEXT

uname -a

TARGET_BUILD_FOLDER=../build

mkdir $TARGET_BUILD_FOLDER

rm $TARGET_BUILD_FOLDER/main
cd ../src/host/main
pwd
make
mv ./main ../../../build

if [ -f ../../../build/main ]; then
  GREEN_TEXT
  printf "SUCCESS "
else
  RED_TEXT
  printf "FAILURE "
fi
echo ""
