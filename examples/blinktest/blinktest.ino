#include <Arduino.h>  

int LED_PIN = 13; // Pin 13 on Arduino UNO

void setup() {
    pinMode(13, OUTPUT); // Initialize the LED pin as an output
}

void loop() {
    digitalWrite(13, HIGH); // Turn the LED on
    delay(1000);                      // Wait for a second
    digitalWrite(13, LOW);  // Turn the LED off
    delay(1000);                      // Wait for a second
}

