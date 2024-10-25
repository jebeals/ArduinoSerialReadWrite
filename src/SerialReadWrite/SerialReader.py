import serial
import time
from typing import Optional
from datetime import datetime
import json
import os
import pickle

class SerialReader:


    def __init__(self, port: str, baud_rate: int = 9600, timeout: int = 1,display_to_command: bool = True, log: str = None):
        """
        Initialize the SerialReader with the specified port and baud rate.
        
        :param port: The serial port to connect to (e.g., '/dev/tty.*' in UNIX-based devices or 'COM3' in Windows based devices).
        :param baud_rate: The baud rate for serial communication (default: 9600).
        :param timeout: The timeout for the serial connection in seconds (default: 1).
        """
        self.port = port           # of the computer where the arduino is connected
        self.baud_rate = baud_rate # of the serial communication
        self.timeout = timeout     # in seconds
        self.serial_connection: Optional[serial.Serial] = None
        self._displayToCmd = display_to_command # dispaly to command option
        self.log = log
        self._config_path = None
        self._pkl_path = None

    def connect(self) -> None:
        """Open the serial connection."""
        try:
            self.serial_connection = serial.Serial(self.port, self.baud_rate, timeout=self.timeout)
            time.sleep(self.timeout)  # Wait for the connection to establish
            if not self.serial_connection:
                raise Exception("Connection timed out.")
            print(f"\nSuccessfully connected to Arduino on port {self.port}")
            self.save_config()
            SerialReader.pickle_config(self)
            if self._displayToCmd:
                self.display_to_command()
        except serial.SerialException as e:
            print(f"Error: Could not open serial port {self.port}: {e}")
            raise
        except Exception as e:
            print(e)
            raise
    
    def save_config(self,filename='data/config.json') -> None:
        cwd = os.getcwd()
        if not os.path.exists(os.path.join(cwd,'data')):
            os.mkdir(os.path.join(cwd,'data'))
        if not self._config_path:
            self._config_path = os.path.join(cwd,filename)
        current_time = datetime.now().isoformat()
        connect_config = {
            "port": self.port,
            "baud_rate": self.baud_rate,
            "last_connected": current_time,  # You can dynamically get the current time
            # "other_info": {
            #     "device_name": self.device_name,
            #     "firmware_version": firmware_version
            # }
        }

        # Write the dictionary to a JSON file
        with open(self._config_path, 'w') as file:
            json.dump(connect_config, file, indent=4)
        
        print(f"Successfully saved connection configuration! ({self._config_path}).\n")

        

    def read_serial(self) -> Optional[str]:
        """Read from the serial port and return the received data."""
        if self.serial_connection and self.serial_connection.in_waiting > 0:
            return self.serial_connection.readline().decode('utf-8').rstrip()
        return None
    
    def display_to_command(self) -> Optional[str]:
        print("\n.......................Displaying Serial Monitor Output........................... \n")
        while self._displayToCmd:
            data = self.read_serial()
            if data:
                print(data)
            time.sleep(0.001)

    def log_serial_output(self,logtimesec: float = 5, file_out: str = "serial_output.txt") -> None:
        t0 = time.time()
        while time.time()-t0 > logtimesec:
            self.log += (self.read_serial() + "\n")
        self.write_to_file(file_out,self.log)

    def write_to_file(self, filename: str, data: str) -> None:
        """
        Write the received data to a file.
        
        :param filename: The name of the file where data will be written.
        :param data: The data to be written to the file.
        """
        with open(filename, 'a') as file:  # Open file in append mode
            file.write(data + '\n')
        print(f"Data written to {filename}")

    def close(self) -> None:
        """Close the serial connection."""
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print(f"Closed serial connection on port {self.port}")
            
    @staticmethod
    def load_last_config(obj_fp: str = 'data/SerialReaderObj.pkl',json_fp: str = 'data/config.json') -> Optional['SerialReader']:

        cwd = os.getcwd()
        pkl_path = os.path.join(cwd,obj_fp)
        if os.path.exists(pkl_path):
            # print(f"Loading last Serial Reader configuraiton ({pkl_path})....")
            with open(pkl_path, 'rb') as file:
                try:
                    obj = pickle.load(file)
                    print(f"SerialReader object loaded from {pkl_path}")
                    return obj
                except pickle.UnpicklingError as e:
                    #print(f"Error loading SerialReader object: {e}")
                    #return None
                    pass
        
        json_path = os.path.join(cwd,json_fp)
        if os.path.exists(json_path):
            # Step 1: Load the JSON data from the file
            with open(json_fp, 'r') as file:
                data = json.load(file)

            # Step 2: Access specific nodes (fields/values)
            port = data.get("port")
            baud_rate = data.get("baud_rate")
            last_connected = data.get("last_connected")

            # Return recontructed objet:
            return SerialReader(port=port,baud_rate=baud_rate) #gj jason
    
    @staticmethod
    def pickle_config(sr: 'SerialReader', filename = 'data/SerialReaderObj.pkl') -> None:
        cwd = os.getcwd()
        if not os.path.exists(os.path.join(cwd,'data')):
            os.mkdir(os.path.join(cwd,'data'))
        if not sr._pkl_path:
            sr._pkl_path = os.path.join(cwd,filename)

        with open(sr._pkl_path, 'wb') as file:
            pickle.dump(sr, file)
        print(f"SerialReader object saved to {sr._pkl_path}")

if __name__ == "__main__":

    print("\nThere is no default funcitonality for this class... \n")

    print("""## Example Usage: 
     from SerialReader import *
     import time
        
     port = '/dev/cu.usbmodem1101'  # Replace with your Arduino's serial port
     baud_rate = 9600
     filename = 'serial_output.txt'  # File to write data to (currently placed within python internpreters current working directory). 

     reader = SerialReader(port, baud_rate) # instantiate SerialReader modile

     try:
         reader.connect()
         while True:
             data = reader.read_serial()
             if data:
                 print(f"Received: {data}")
                 reader.write_to_file(filename, data)  # Write data to the file
             time.sleep(0.1)  # Small delay to avoid overloading the serial port
     except KeyboardInterrupt:
         print("Interrupted! Closing the connection.")
     finally:
         reader.close()""") 
    print("\n End of script.")
