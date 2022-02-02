String x;
const int transmit_pin = 2;
void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 pinMode(transmit_pin,OUTPUT);
 digitalWrite(transmit_pin,LOW);
}
void loop() {
 while (!Serial.available());
 x = Serial.readString();
 if (x=="GS1"){
 Serial.println(x);
 delay(50);}
}
