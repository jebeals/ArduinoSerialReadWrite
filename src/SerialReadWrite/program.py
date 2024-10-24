import argparse
from typing import Optional  # Import Optional from typing
from .SerialReader import SerialReader  # Adjust the import based on the actual structure

class Program:

    _parser: argparse.ArgumentParser      = argparse.ArgumentParser(description="SerialReadWrite CLI for interacting with Arduino")
    _args_in: Optional[str]               = None 
    _SerialReader: Optional[SerialReader] = None  # SerialReader can be None or an instance

    @staticmethod
    def main() -> int:
        """
        Entry point for the SerialReadWrite CLI application.
        Sets up the argparse commands and dispatches them to the appropriate handlers.
        """

        try:
            Program.create_parser()
            args = Program._parser.parse_args(); Program._args_in = args; 
            Program.handle_args(args)
        except Exception as e:
            print(e)
            return 1
        return 0 

    @staticmethod
    def create_parser() -> Optional[argparse.ArgumentParser]:
        pass

    @staticmethod
    def handle_args() -> None:
        pass

        # # Create an argument parser
        # parser = argparse.ArgumentParser(description="SerialReadWrite CLI for interacting with Arduino")
        
        # # Add subcommands
        # subparsers = parser.add_subparsers(dest='command', help="Available commands")
        
        # # 'connect' command to detect and connect to Arduino boards
        # connect_parser = subparsers.add_parser('connect', help="Detect and connect to Arduino boards")
        # connect_parser.add_argument('--port', required=True, help="Specify the serial port (e.g., /dev/tty.* or COM3)")
        # connect_parser.add_argument('--baud_rate', type=int, default=9600, help="Specify the baud rate (default: 9600)")
        
        # # Parse the arguments
        # args = parser.parse_args()
        
        # # Dispatch commands to the appropriate methods
        # if args.command == 'connect':
        #     # Create an instance of SerialReader with provided arguments
        #     Program._SerialReader = SerialReader(port=args.port, baud_rate=args.baud_rate)
            
        #     # Connect to the board
        #     Program._SerialReader.connect()
        # else:
        #     parser.print_help()


if __name__ == "__main__":
    Program.main()

