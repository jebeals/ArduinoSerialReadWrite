## How to Use
This example folder uses `arduino-cli` commands to run and compile .ino files

## Example usage
1. Compilation:
    SerialReadWrite/examples/blinktest >$ `arduino-cli compile -b ardunio:avr:uno ./blinktest.ino` 
2. Upload
    A. Check Ports: SerialReadWrite/examples/blinktest >$ `arduino-cli board list`

    Port                            Protocol Type              Board Name  FQBN            Core
    /dev/cu.Bluetooth-Incoming-Port serial   Serial Port       Unknown
    /dev/cu.usbmodem1101            serial   Serial Port (USB) Arduino Uno arduino:avr:uno arduino:avr

    B. Upload using the port that the Arduino is specified to: 
    The specified port looks like `/dev/cu.usbmodem1101` --> 
    SerialReadWrite/examples/blinktest >$ `arduino-cli upload -p /dev/cu.usbmodem1101 --fqbn arduino:avr:uno ./blinktest.ino`

## Clean build
SerialReadWrite/examples/blinktest >$ `arduino-cli compile --fqbn arduino:avr:uno ./blinktest.ino --clean`
