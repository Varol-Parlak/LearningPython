int yellow_led = 9;
int green_led = 10;
int blue_led = 11;

int last_command = -1;

void setup() {
  Serial.begin(9600);
  pinMode(yellow_led, OUTPUT);
  pinMode(green_led, OUTPUT);
  pinMode(blue_led, OUTPUT);
  digitalWrite(green_led, LOW); 
}

void loop() {
  if (Serial.available() > 0) {
    String msg = Serial.readString();

    if (msg == "1" && last_command != 1) {  
      digitalWrite(green_led, HIGH);
      last_command = 1; 
    } 
    else if (msg == "2" && last_command != 2) { 
      digitalWrite(green_led, LOW);
      last_command = 2; 
    }
  }
}
