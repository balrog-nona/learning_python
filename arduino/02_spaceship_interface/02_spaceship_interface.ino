// 02 starter kit video
// https://www.youtube.com/watch?v=w-C5Ne00_wM&list=PLbJTtGdesEgEeF4PXBqOUA2_LKyVSoESU&index=4

// Create a global variable to hold the state of the switch.
// This variable is persistent throughout the program.
int switchstate = 0;

void setup() {
  // put your setup code here, to run once:
  
  // declare the LED pins as outpust
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);

  // declare the switch pin as an input
  pinMode(2, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  // read the value of the switch
  // digitalRead() checks to see if there is voltage on the pin
  switchstate = digitalRead(2);

  // if the button is not pressed, turn on the green LED and turn off the red LEDs
  if (switchstate == LOW) {
    digitalWrite(3, HIGH); // turn the LED on pin 3 on
    digitalWrite(4, LOW); // turn the LED on pin 4 off
    digitalWrite(5, LOW); // turn the LED on pin 5 off
  }
  else {
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
    digitalWrite(5, HIGH);
    // wait for the quarter of a second
    delay(250);
    digitalWrite(4, HIGH);
    digitalWrite(5, LOW);
    // wait again
    delay(250);    
  }
}
