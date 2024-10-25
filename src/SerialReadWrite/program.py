import argparse
from typing import Optional  # Import Optional from typing
from SerialReader import * # Adjust the import based on the actual structure

class Program:

    _parser: argparse.ArgumentParser       = argparse.ArgumentParser(description="SerialReadWrite CLI for interacting with Arduino")
    _args_in: Optional[argparse.Namespace] = None 
    _SerialReader: Optional[SerialReader]  = None  # SerialReader can be None or an instance

    @staticmethod
    def main() -> int:
        """
        Entry point for the SerialReadWrite CLI application.
        Sets up the argparse commands and dispatches them to the appropriate handlers.
        """
        try:
            Program.create_parser()
            Program._args_in = Program._parser.parse_args()
            Program.handle_args(Program._args_in)
        except KeyboardInterrupt:
            print("\nExiting pyduino ~~ cya later alligator")
            return 0
        except Exception as e:
            print(e)
            return 1
        return 0 

    @staticmethod
    def create_parser() -> None:

        # Now create the arggument parser:
        parser = Program._parser

        # Add subcommands
        subparsers = parser.add_subparsers(dest='command', help="Available commands")

        # 'help' command
        help_parser = subparsers.add_parser('help', help="Show available commands")

        # 'connect' command to detect and connect to Arduino boards
        read_parser = subparsers.add_parser('read', help="Connect and read serial output from Arduino boards")
        read_parser.add_argument('-p','--port', help="Specify the serial port (e.g., /dev/tty.* or COM3)")
        read_parser.add_argument('-br','--baud_rate', type=int, default=9600, help="Specify the baud rate (default: 9600)")
        # ADD MORE FUCNTIOANLITY:`pyduino show` should show the sherial monitor from the last successful connection
        #connect_parser.add_argument('--hide',action='store_true',help="Hide the serial output to the command window.")

        # 'connect' command to detect and connect to Arduino boards
        connect_parser = subparsers.add_parser('connect', help="Detect and connect to Arduino boards")
        connect_parser.add_argument('-p','--port', required=True, help="Specify the serial port (e.g., /dev/tty.* or COM3)")
        connect_parser.add_argument('-br','--baud_rate', type=int, default=9600, help="Specify the baud rate (default: 9600)")
        connect_parser.add_argument('-s','--show',action='store_true',help="Hide the serial output to the command window.")

        # # Monitor command: Make it simple som that after an ardunio board has been connected you can jsut say monitor to load the alst connection
        # #                   and start the monitoring process
        # connect_parser = subparsers.add_parser('monitor', help="Connect to and monitor or monitor a previous connected arduino confiuraiton. Can read/write out; show text to command, etc.")
        # connect_parser.add_argument('-p','--port', required=True, help="Specify the serial port (e.g., /dev/tty.* or COM3)")
        # connect_parser.add_argument('-br','--baud_rate', type=int, default=9600, help="Specify the baud rate (default: 9600)")
        # connect_parser.add_argument('-s','--show',action='store_true',help="Hide the serial output to the command window.")

        # 



    @staticmethod
    def handle_args(args: argparse.Namespace) -> None:
        if args.command == 'connect':
            # Hidden or not hidden connect?
            _disp_to_cmd = False; 
            if args.show:
                _disp_to_cmd = True
            # Create serial reaer object
            Program._SerialReader = SerialReader(port=args.port, baud_rate=args.baud_rate, display_to_command = _disp_to_cmd)
            Program._SerialReader.connect()
            return
        
        if args.command == 'read':
            # Create serial reaer object
            if not args.port:
                pass
            Program._SerialReader = SerialReader(port=args.port, baud_rate=args.baud_rate, display_to_command = True)
            Program._SerialReader.connect()
            return
        
        elif args.commmand == 'help':
            Program._parser.print_help()

        else:
            Program._parser.print_help()


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

