void to_lcd(float data1,float data2) {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("S2");
  lcd.setCursor(3, 0);
  lcd.print("US:");
  lcd.print(data1);
  lcd.setCursor(0,1);
  lcd.print("PR:");
  lcd.print(data2);
}

String post_concat(float data1,float data2) {
    String ps = "PS2 ";
  ps.concat(data1);
  ps.concat("|");
  ps.concat(data2);
  return ps;
}

void post_data(float data1,float data2) {
  digitalWrite(transmit_pin, HIGH);
  delay(50);
  Serial.println(post_concat(data1,data2));
  Serial.flush();
  digitalWrite(transmit_pin, LOW);
}


float get_ultrasonic_dist(const int trigPin, const int echoPin) {
  long duration;
  float distance;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;
  return distance;
}
