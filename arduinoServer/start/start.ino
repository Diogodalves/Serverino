const int  buttonPin = 2; 
  
int buttonState = 0;         // current state of the button
int lastButtonState = 0;  
int buttonPushCounter = 0;

void setup() {
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}


void loop() {
  buttonState = digitalRead(buttonPin);
  if (buttonState != lastButtonState) {
    if (buttonState == HIGH) {
      buttonPushCounter++;
    }
    delay(50);
  }
  lastButtonState = buttonState;
  
  if (buttonPushCounter % 2 == 0) {
    Serial.println(1);
  } else {
    Serial.println(0);
  }
}
