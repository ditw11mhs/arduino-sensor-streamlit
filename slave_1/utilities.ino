void to_lcd(float data) {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("S1");
  lcd.setCursor(0, 1);
  lcd.print("US: ");
  lcd.print(data);
}

String post_concat(float data) {
  String ps = "PS1 ";
  ps.concat(data);
  return ps;
}

void post_data(float data) {
  digitalWrite(transmit_pin, HIGH);
  delay(50);
  Serial.println(post_concat(data));
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
