
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.SerialReadWrite.SerialReader import *
import time



# Example usage
port = '/dev/cu.usbmodem1101'  # Replace with your Arduino's serial port
baud_rate = 9600

# import os
# cwd = os.getcwd(); 

filename = 'serial_output.txt'  # File to write data to

sr = SerialReader(port, baud_rate)

try:
    sr.connect()
    while True:
        data = sr.read_serial()
        if data:
            print(f"Received: {data}")
            sr.write_to_file(filename, data)  # Write data to the file
        time.sleep(0.1)  # Small delay to avoid overloading the serial port
except KeyboardInterrupt:
    print("Interrupted! Closing the connection.")
finally:
    sr.close()

# import serial
# import time

# # Replace '/dev/ttyACM0' with your Arduino's serial port (e.g., 'COM3' for Windows)
# arduino_port = '/dev/cu.usbmodem1101'  
# baud_rate = 9600  # Make sure this matches the Arduino baud rate

# # Open the serial port
# ser = serial.Serial(arduino_port, baud_rate, timeout=1)
# time.sleep(2)  # Wait for the connection to establish

# print(f"Connected to Arduino on port {arduino_port}")

# try:
#     while True:
#         if ser.in_waiting > 0:  # Check if there's data waiting in the buffer
#             line = ser.readline().decode('utf-8').rstrip()  # Read the line and decode
#             print("Received:", line)
#         time.sleep(0.1)  # Small delay to avoid overloading the serial port
# except KeyboardInterrupt:
#     print("Interrupted! Closing the connection.")
# finally:
#     ser.close()  # Close the serial port when done
