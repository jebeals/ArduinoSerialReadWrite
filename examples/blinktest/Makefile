# MCU, Frequency, and baud rate for Arduino UNO
MCU=atmega328p
F_CPU=16000000UL
BAUD=115200
PORT=/dev/tty.usbmodem1101  # Change this to match your macOS/Linux port
PROGRAMMER=arduino

# Compiler and tools
CC=avr-gcc
OBJCOPY=avr-objcopy
AVRDUDE=avrdude

# Compilation flags
CFLAGS=-mmcu=$(MCU) -DF_CPU=$(F_CPU) -Os -Wall

# Target files
TARGET=blink
OBJ=$(TARGET).o
HEX=$(TARGET).hex

all:    $(HEX)

# Compile C++ to object file
$(OBJ): $(TARGET).cpp
	$(CC) $(CFLAGS) -o $(OBJ) -c $(TARGET).cpp

# Convert object file to hex file
$(HEX): $(OBJ)
	$(OBJCOPY) -O ihex -R .eeprom $(OBJ) $(HEX)

# Flash the Arduino
flash:  $(HEX)
	$(AVRDUDE) -v -p $(MCU) -c $(PROGRAMMER) -P $(PORT) -b $(BAUD) -D -U flash:w:$(HEX):i

clean:
	rm -f $(OBJ) $(HEX)
