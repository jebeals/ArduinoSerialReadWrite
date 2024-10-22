#!/bin/bash
# Script to compile and flash Arduino UNO

# Navigate to the directory containing the Makefile (if necessary)
# cd $(dirname $0) # Uncomment if needed

# Clean previous build files
make clean

# Compile the blink.cpp program
make

# Flash the compiled program to the Arduino
make flash
