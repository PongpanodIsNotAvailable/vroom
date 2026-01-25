const unsigned long SAMPLE_PERIOD_MS = 10;  // 100 Hz
unsigned long lastSample = 0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  unsigned long now = millis();

  if (now - lastSample >= SAMPLE_PERIOD_MS) {
    lastSample = now;

    // Read ADCs
    int a0 = analogRead(A0);
    int a1 = analogRead(A1);
    int a2 = analogRead(A2);
    int a3 = analogRead(A3);

    // CSV output (NO SPACES)
    Serial.print(a0);
    Serial.print(",");
    Serial.print(a1);
    Serial.print(",");
    Serial.print(a2);
    Serial.print(",");
    Serial.println(a3);
  }
}