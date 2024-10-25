import serial
import time
from typing import Optional


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

    def connect(self) -> None:
        """Open the serial connection."""
        try:
            self.serial_connection = serial.Serial(self.port, self.baud_rate, timeout=self.timeout)
            time.sleep(self.timeout)  # Wait for the connection to establish
            if not self.serial_connection:
                raise Exception("Connection timed out.")
            print(f"Connected to Arduino on port {self.port}")
            if self._displayToCmd:
                self.display_to_command()
        except serial.SerialException as e:
            print(f"Error: Could not open serial port {self.port}: {e}")
            raise
        except Exception as e:
            print(e)
            raise

    def read_serial(self) -> Optional[str]:
        """Read from the serial port and return the received data."""
        if self.serial_connection and self.serial_connection.in_waiting > 0:
            return self.serial_connection.readline().decode('utf-8').rstrip()
        return None
    
    def display_to_command(self) -> Optional[str]:
        print("Displaying Serial Monitor Output... \n")
        while self._displayToCmd():
            print(self.read_serial())

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
