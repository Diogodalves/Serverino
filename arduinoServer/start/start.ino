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
  //After you read your sensor values (A0, A1 and A2)
  if (buttonPushCounter % 2 == 0) {
    Serial.print(1);
    Serial.print(',');
    Serial.print(A0);
    Serial.print(',');
    Serial.print(A1);
    Serial.print(',');
    Serial.printn(A2);
  } else {
    Serial.println(0);
  }
}
