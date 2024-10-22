This is a directory containing a test to compile a C++ file to Arduino to test the main CLI application contained in this repo (Serial Read Write API). In order to do so, a make file is present to flash this *.cpp file to Arduino. This includes instrucitons on how to use this exmaple folder. 

## Requirements:
avr-gcc # This is a library used to flash to arduino --> 'brew tap osx-cross/avr; brew install avr-gcc'
avrdude # This is a library used to flash to arduino as well --> 'brew install avrdude'

## How to Use:
1. Make sure to check which USB port Arudino is on with `ls /dev/tty.*` and set this with the `PORT=/dev/tty.usbmodem101`
2. 
