int potPin = 0;
int motor = 5;

void setup() {
  Serial.begin(9600);

  pinMode(motor, OUTPUT);
}

void loop() {
   int val = analogRead(A0);
   analogWrite(motor, (map(val, 0, 1023, 0, 255)));
   delay(1);
}
