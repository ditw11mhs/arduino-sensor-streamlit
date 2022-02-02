#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

String x;
int transmit_pin = 2;
int echoPin = 3;
int trigPin = 4;
float test_data = 0;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(transmit_pin, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(14, INPUT);
  digitalWrite(transmit_pin, LOW);
  lcd.begin();
  lcd.backlight();
  lcd.setBacklight(HIGH);
}
void loop() {
  float data1 = get_ultrasonic_dist(trigPin, echoPin);
  float data2 = analogRead(14);

  to_lcd(data1,data2);
  
  while (!Serial.available());
  x = Serial.readString();
  if (x == "GS2") {
    post_data(data1, data2);
  }
}
