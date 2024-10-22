#include <Arduino.h>

int data = 0;
unsigned long startTime; 
unsigned long currentTime;

void setup(){
    Serial.begin(9600);
    startTime = millis(); 
}

void loop(){
    currentTime = millis(); 
    Serial.print("Time since start: "); 
    Serial.print(currentTime-startTime);
    Serial.print("  ... Data = ");
    Serial.println(data);
    data++;
    delay(1000); 

}


