int ledPin = 12;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if(Serial.available() > 0){
    int count = Serial.parseInt();

    if (count > 0){
      Serial.print("ur input is: ");
      Serial.println(String(count));
      blinkLED(count);
    }
  }
}

void blinkLED(int count){
  for (int i = 0; i < count; i++){
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(ledPin, LOW);
    delay(500);
  }
}

