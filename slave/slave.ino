String x;
int transmit_pin = 2;
float test_data = 0;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(transmit_pin, OUTPUT);
  digitalWrite(transmit_pin, LOW);
}
void loop() {
  while (!Serial.available());
  x = Serial.readString();
  if (x == "GS1") {
    test_data = test_data + 1;
    digitalWrite(transmit_pin, HIGH);
    delay(50);
    Serial.println(post_data(test_data));
    Serial.flush();
    digitalWrite(transmit_pin, LOW);

  }
}

String post_data(float data) {
  String ps = "PS1 ";
  ps.concat(data);
  return ps;
}
