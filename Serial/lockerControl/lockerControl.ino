const int solenoidpin = 13;    //defines solenoid @pin 3

void setup() {            
  pinMode(solenoidpin, OUTPUT); //sets solenoid as Output
}

void loop() {
  digitalWrite(solenoidpin, HIGH);  //sets the solenoid into HIGH state
  delay(1000);            //duration 2 seconds
  digitalWrite(solenoidpin, LOW); //sets the solenoid into LOW state
  delay(1000);            //duration 2 seconds
}
