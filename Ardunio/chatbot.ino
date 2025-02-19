#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// LCD Display (16x2)
LiquidCrystal_I2C lcd(0x27, 16, 2);

// LED Pins
int redLED = 8;    // Red LED (Listening)
int greenLED = 9;  // Green LED (Responding)

void setup() {
    Serial.begin(9600);
    lcd.init();
    lcd.backlight();

    pinMode(redLED, OUTPUT);
    pinMode(greenLED, OUTPUT);
    digitalWrite(redLED, LOW);
    digitalWrite(greenLED, LOW);

    // Show startup message
    lcd.setCursor(0, 0);
    lcd.print("Chatbot Ready");
    lcd.setCursor(0, 1);
    lcd.print("by Dhananjay.");
    delay(2000);  // Show startup message briefly
    lcd.clear();
}

void displayMessage(String message) {
    int length = message.length();
    int index = 0;

    digitalWrite(greenLED, HIGH); // Turn ON Green LED while displaying response

    while (index < length) {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(message.substring(index, index + 16));

        lcd.setCursor(0, 1);
        if (index + 16 < length) {
            lcd.print(message.substring(index + 16, index + 32));
        }

        delay(1500);  // Shorter delay for smooth transition
        index += 32;
    }

    digitalWrite(greenLED, LOW); // Turn OFF Green LED after response is fully displayed
}

void loop() {
    if (Serial.available() > 0) {
        String data = Serial.readStringUntil('\n');
        data.trim();  // Remove any unwanted whitespace

        if (data == "Listening") {
            digitalWrite(redLED, HIGH);
            digitalWrite(greenLED, LOW);
            lcd.clear();
            lcd.setCursor(0, 0);
            lcd.print("Listening...");
        } 
        else if (data == "Exit") {
            digitalWrite(redLED, LOW);
            digitalWrite(greenLED, LOW);
            lcd.clear();
            lcd.setCursor(0, 0);
            lcd.print("Chatbot Stopped");
            Serial.end();  // Safely stop serial communication
            delay(2000);
            return;  // Allow loop to restart safely
        }
        else {
            digitalWrite(redLED, LOW);
            displayMessage(data);  // Show chatbot response properly
        }
    }
}
