#include <Arduino.h>  

int LED_PIN = 13; // Pin 13 on Arduino UNO

void setup() {
    pinMode(LED_PIN, OUTPUT); // Initialize the LED pin as an output
}

void loop() {
    digitalWrite(LED_PIN, HIGH); // Turn the LED on
    delay(1000);                      // Wait for a second
    digitalWrite(LED_PIN, LOW);  // Turn the LED off
    delay(1000);                      // Wait for a second
}

int main(){
    setup();
    while(1){
        loop();
    }
}
