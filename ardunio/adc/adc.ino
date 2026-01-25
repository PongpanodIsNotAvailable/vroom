void setup() {
  Serial.begin(115200);
}

void loop() {

  currentSample = millis();

    a0 = analogRead(A0);    // Tacho
    a1 = analogRead(A1);    // TPS
    a2 = analogRead(A2);    // Water Temp
    a3 = analogRead(A3);    // Water Temp

    // CSV output (NO SPACES)
    Serial.print(a0);
    Serial.print(",");
    Serial.print(a1);
    Serial.print(",");
    Serial.print(",");
    Serial.print(a2);
    Serial.println(a3);    
}