void setup() {
  Serial.begin(9600);
  Serial.println("we litty");
}

void loop() {
  char inByte = ' ' ;
  if(Serial.available()){
    char inByte = Serial.read();
    Serial.println(inByte);
  }
  delay(100);
}
