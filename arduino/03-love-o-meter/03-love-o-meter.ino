// 03 starter kit video
// https://www.youtube.com/watch?v=UwTFfa_f4-0&list=PLbJTtGdesEgEeF4PXBqOUA2_LKyVSoESU&index=4

// named constant for the pin sensor is connected to
const int sensorPIN = A0;
// room temperature in Celsius
const float baselineTemp = 30.0;

void setup() {
  // put your setup code here, to run once:

  // open a serial connection to display values
  Serial.begin(9600);
  // set the led pins as outputs
  for (int pinNumber = 2; pinNumber < 5; pinNumber ++) {
    pinMode(pinNumber,OUTPUT);
    digitalWrite(pinNumber, LOW);
  }
}

void loop() {
  // put your main code here, to run repeatedly:

  // read the value on AnalogIn pin 0 and store it in a variable
  int sensorVal = analogRead(sensorPIN);

  // send the 10-bit sensor value out the serial port
  Serial.print("sensor value: ");
  Serial.print(sensorVal);

  // convert the ADC reading to voltage
  float voltage = (sensorVal / 1024.0) * 5.0;

  // send the voltage level out the serial port
  Serial.print(", Volts: ");
  Serial.print(voltage);

  // convert the voltage to temperature in degrees C
  // the sensor changes 10mV per degree
  // datasheet says there's a 500 mV offset
  // (voltage - 500 mV) times 100
  Serial.print(", degrees C: ");
  float temperature = (voltage - 0.5) * 100;

  // if the current temperature is lower than the baseline, turn off all LEDs
  if (temperature < baselineTemp + 2) {
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  } // if the temperature rises 2-4 degrees, turn the first LED on
  else if (temperature >= baselineTemp + 2 && temperature < baselineTemp +4) {
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  } // if the temperature rises 4-6 degrees, turn the second LED on
  else if (temperature >= baselineTemp +4 && temperature < baselineTemp + 6) {
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, LOW);
  } // if the temperature rises more than 6 degrees, turn all the LEDs on
  else if (temperature >= baselineTemp + 6) {
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, HIGH);
  }
  delay(1);
}
