import subprocess
import platform
import os
from typing import Optional
import time
from .utils import input_with_timeout

class ArduinoCLIHandler:

    _recommendation_given = False  # Class-level flag
    _arduino_cli_installed = False
    _package_manager = None
    
    def __init__(self):
        """
        Initialize the ArduinoCLIHandler class.
        Detect the operating system and check for available package managers.
        """
        print("ArduinoCLIHandler class initiated. Static use is recommended for this class.")
        self.os_name = platform.system()
        self.package_manager = self.check_package_manager()
        self.is_installed = self.check_arduino_cli_installed()

    @staticmethod
    def print_rec():

        # Recommend based on user operatin system.
        os_name = platform.system()

        if os_name == "Darwin":
            print("""
            To install arduino-cli on macOS, you can run:
            brew install arduino-cli

            Alternatively, visit the official installation page:
            https://arduino.github.io/arduino-cli/installation/#macos
            """)
        
        elif os_name == "Linux":
            print("""
            
            To install arduino-cli on Linux, run the following commands:
            curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh

            Alternatively, visit the official installation page:
            https://arduino.github.io/arduino-cli/installation/#linux
            """)
        
        elif os_name == "Windows":
            print("""
            To install arduino-cli on Windows, download it from the following link:
            https://arduino.github.io/arduino-cli/installation/#windows

            Or use Chocolatey if it's installed:
            choco install arduino-cli
            """)
        
        else:
            print(f"""
            Unsrecognized operating system {os_name}. Please visit the official arduino-cli installation page:
            https://arduino.github.io/arduino-cli/installation/
            """)

    @staticmethod
    def recommend_arduino_cli_installation():
        """
        Recommend the user how and where to manually install arduino-cli based on their OS.
        """
        
        print("It is recommended to install `ardunio-cli` on your machine to enable automation of Arudino boards with this SerialReadWrite console application.\n")
        if ArduinoCLIHandler._recommendation_given:  # Class-level flag
            out = input_with_timeout("Would you like to know how where/how to install ardunio-cli? (Y/n):", 2.5)
            if out.lower() == "y" or out is "":
                ArduinoCLIHandler.print_rec()
                return
        
        ArduinoCLIHandler.print_rec()
        ArduinoCLIHandler._recommendation_given = True
        return

    @staticmethod
    def check_package_manager() -> Optional[str]:
        """
        Check for available package managers on the system (Homebrew, apt-get, Chocolatey).
        Returns the package manager as a string, or None if no package manager is found.
        """
        os_name = platform.system()

        if os_name == "Darwin":
            expected_manager = "brew"
        elif os_name == "Linux":
            expected_manager = "apt-get"
        elif os_name == "Windows":
            expected_manager = "choco"
        else:
            print(f"Unrecognized operating system '{os_name}' found using platform.system()...")
            expected_manager = ""; 
        
        # Return expected manaegr per the operating system defined above
        if ArduinoCLIHandler.is_command_available(expected_manager):
            ArduinoCLIHandler._package_manager = expected_manager
            return expected_manager
        
        # Let user nkow no pacakge manager was found.
        print(f"Unable to find expected package manager '{expected_manager}'")
        #ArduinoCLIHandler.recommend_arduino_cli_installation()
        
        # Return none if no package manager is found
        return None
    
    @staticmethod
    def is_command_available(command: str) -> bool:
        """
        Check if a given command is available on the system (e.g., brew, apt-get, choco).
        """
        try:
            subprocess.run([command, "--version"], capture_output=True, check=True)
            return True
        except subprocess.CalledProcessError:
            return False
        except FileNotFoundError:
            return False

    @staticmethod
    def install_arduino_cli_with_manager(manager: str) -> None:
        """
        Install arduino-cli using the provided package manager (brew, apt-get, choco).
        Ensures the user returns to the CLI after the installation completes.
        """
        try:
            print(f"Starting installation of arduino-cli using {manager}...\n")
            
            if manager.lower() == "brew":
                subprocess.run(["brew", "install", "arduino-cli"], check=True)
            elif manager.lower() == "apt-get":
                subprocess.run(["sudo", "apt-get", "install", "arduino-cli"], check=True)
            elif manager.lower() == "choco":
                subprocess.run(["choco", "install", "arduino-cli"], check=True)
            else:
                raise Exception(f"Unsupported package manager: {manager}")

            # Confirm installation success
            print(f"Successfully installed arduino-cli using {manager}.\n")
        
        except subprocess.CalledProcessError as e:
            # Handle errors during the installation process
            print(f"Installation failed using {manager}: {e}")
        except Exception as e:
            # Handle any other exceptions
            print(f"Error: {e}")

        # # Return to CLI with confirmation message
        # print("Returning to CLI...")

    @staticmethod
    def install_arduino_cli() -> None:
        """
        Prompt the user to install arduino-cli using available package managers or direct download.
        """
        manager = ArduinoCLIHandler.check_package_manager()
        
        if manager:
            consent = input(f"Would you like to install arduino-cli using {manager}? (Y/n): ")
            if consent.lower() == 'y' or consent == ("" or None): # Y is default here
                print(f"Installing arduino-cli via {manager}")
                ArduinoCLIHandler.install_arduino_cli_with_manager(manager)
            else:
                print(f"Skipping installation via {manager}. Please install arduino-cli manually.")
                ArduinoCLIHandler.recommend_arduino_cli_installation()

        else:
            print("No supported package manager found. Please install arduino-cli manually from https://arduino.github.io/arduino-cli/installation/")

    @staticmethod
    def check_arduino_cli_installed() -> bool:
        """
        Check if 'arduino-cli' is installed by running 'arduino-cli --version'.
        Returns True if installed, False otherwise.
        """
        try:
            result = subprocess.run(["arduino-cli", "--version"], capture_output=True, text=True, check=True)
            print(f"arduino-cli version: {result.stdout.strip()}")
            ArduinoCLIHandler._arduino_cli_installed = True
            return True
        except subprocess.CalledProcessError:
            print("Error: 'arduino-cli' is installed but returned an error.")
            return False
        except FileNotFoundError:
            print("'arduino-cli' is not installed.")
            return False

    @staticmethod
    def check_and_install_arduino_cli() -> None:
        """
        Check if arduino-cli is installed, and if not, prompt the user to install it.
        """
        if ArduinoCLIHandler.check_arduino_cli_installed():
            print("arduino-cli is already installed and ready to use!")
            return
        
        # If arduino-cli is not installed
        print("'arduino-cli' is not installed on your system... (`arduino-cli --version` was not a vali command).\n")
        out = input_with_timeout("Would you like to check for automatic installation capability of `aruino-cli` on your mahine? (Y/n):",5)
        if out.lower() is ("y" or "" or None):
            # Check available package manager
            manager = ArduinoCLIHandler.check_package_manager()

            if ArduinoCLIHandler._package_manager:
                consent = input_with_timeout(f"Would you like to install arduino-cli using {manager}? (Y/n): ",10)
                if consent.lower() == 'y' or consent == "":
                    ArduinoCLIHandler.install_arduino_cli_with_manager(manager)
                else:
                    ArduinoCLIHandler.recommend_arduino_cli_installation()
            else:
                # If no package manager found, recommend installation manually
                ArduinoCLIHandler.recommend_arduino_cli_installation()
