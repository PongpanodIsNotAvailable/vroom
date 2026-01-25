void setup() {
  Serial.begin(115200);
}

void loop() {
    int a0 = analogRead(A0);    // Tacho
    int a1 = analogRead(A1);    // TPS
    int a2 = analogRead(A2);    // Water Temp
    int a3 = analogRead(A3);    // Water Temp

    // CSV output (NO SPACES)
    Serial.print(a0);
    Serial.print(",");
    Serial.print(a1);
    Serial.print(",");
    Serial.print(",");
    Serial.print(a2);
    Serial.println(a3);    

    delay(10);
}