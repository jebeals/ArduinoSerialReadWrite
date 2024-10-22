#include <avr/io.h>
#include <util/delay.h>

#define LED_PIN 5 // Pin 13 on Arduino UNO

void setup() {
    DDRB |= (1 << LED_PIN); // Set LED pin as output
}

void loop() {
    PORTB |= (1 << LED_PIN);  // Turn LED on
    _delay_ms(1000);          // Delay 1 second
    PORTB &= ~(1 << LED_PIN); // Turn LED off
    _delay_ms(1000);          // Delay 1 second
}

int main() {
    setup();
    while (1) {
        loop();
    }
}

