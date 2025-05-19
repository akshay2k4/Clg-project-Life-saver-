const int irSensorPin = 2; // Connect the digital IR sensor's output pin to Arduino digital pin 2
int doorOpen = false; // Flag to track if the door is considered "open"

void setup() {
  Serial.begin(9600);
  pinMode(irSensorPin, INPUT);
  Serial.println("Digital IR Sensor Ready");
}

void loop() {
  int sensorValue = digitalRead(irSensorPin);

  // Check for door opening (HIGH signal) and only trigger once
  if (sensorValue == HIGH && !doorOpen) {
    Serial.println("DOOR_OPENED");
    doorOpen = true; // Set the flag to prevent repeated triggers
  }

  // Check for door closing (LOW signal) and reset the flag
  if (sensorValue == LOW && doorOpen) {
    doorOpen = false; // Reset the flag, ready for the next opening
  }

  delay(100); // Small delay
}