int solenoidPin = 9;

void setup() 
{
  pinMode(solenoidPin, OUTPUT);
}

void lock(int control){
  if (control == 0) {digitalWrite(solenoidPin, LOW);}
  else if (control == 1) {digitalWrite(solenoidPin, HIGH);}
  
  }

void loop() 
{
  lock(1);
  delay(1000);
  
  lock(0);
  delay(1000);
}
