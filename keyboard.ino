uint8_t buf[8] = {
  0
};  // Keyboard Report Buffer: 8 bytes

#define PIN_UP A0
#define PIN_BACK A1
#define PIN_LEFT A2
#define PIN_RIGHT A3

#define SERIAL_DEBUG  

bool currState_UP = HIGH;
bool currState_LEFT = HIGH;
bool currState_BACK = HIGH;
bool currState_RIGHT = HIGH;
          
bool prevState_UP = HIGH; 
bool prevState_LEFT = HIGH; 
bool prevState_BACK = HIGH; 
bool prevState_RIGHT = HIGH; 

unsigned long prevTime_UP = 0;
unsigned long prevTime_LEFT = 0;
unsigned long prevTime_BACK = 0;
unsigned long prevTime_RIGHT = 0;

unsigned long waitTime_UP = 50;
unsigned long waitTime_LEFT = 50;
unsigned long waitTime_BACK = 50;
unsigned long waitTime_RIGHT = 50;

void setup() 
{
  Serial.begin(9600);

  pinMode(PIN_UP, INPUT_PULLUP);
  pinMode(PIN_LEFT, INPUT_PULLUP);
  pinMode(PIN_BACK, INPUT_PULLUP);
  pinMode(PIN_RIGHT, INPUT_PULLUP);
  
  delay(200);
}

void loop() 
{
  checkButton();
}


void checkButton() {

  bool currRead_UP = digitalRead(PIN_UP);
  bool currRead_LEFT = digitalRead(PIN_LEFT);
  bool currRead_BACK = digitalRead(PIN_BACK);
  bool currRead_RIGHT = digitalRead(PIN_RIGHT);

  if (currRead_UP != prevState_UP) {
    prevTime_UP = millis();
  }
  if (currRead_LEFT != prevState_LEFT) {
    prevTime_LEFT = millis();
  }
  if (currRead_BACK != prevState_BACK) {
    prevTime_BACK = millis();
  }
  if (currRead_RIGHT != prevState_RIGHT) {
    prevTime_RIGHT = millis();
  }

  if ((millis() - prevTime_UP) > waitTime_UP) {
    if (currRead_UP != currState_UP) {
      currState_UP = currRead_UP;
      if (currState_UP == LOW) {
        // Send the code
        buf[2] = 26;    // HID: Up arrow key 83
        Serial.write(buf, 8); // Send keypress
      } else {
        // Release the keyboard
        releaseKey();
      }
    }
  }
  if ((millis() - prevTime_LEFT) > waitTime_LEFT) {
    if (currRead_LEFT != currState_LEFT) {
      currState_LEFT = currRead_LEFT;
      if (currState_LEFT == LOW) {
        // Send the code
        buf[2] = 80;   // HID: LEFT Arrow key
        
        Serial.write(buf, 8); // Send keypress
      } else {
        // Release the keyboard
        releaseKey();
      }
    }
  }
  if ((millis() - prevTime_BACK) > waitTime_BACK) {
    if (currRead_BACK != currState_BACK) {
      currState_BACK = currRead_BACK;
      if (currState_BACK == LOW) {
        // Send the code
        buf[2] = 22;    // HID: Down Arrow key
        Serial.write(buf, 8); // Send keypress
      } else {
        // Release the keyboard
        releaseKey();
      }
    }
  }
  if ((millis() - prevTime_RIGHT) > waitTime_RIGHT) {
    if (currRead_RIGHT != currState_RIGHT) {
      currState_RIGHT = currRead_RIGHT;
      if (currState_RIGHT == LOW) {
        // Send the code
        buf[2] = 79;   // HID: RIGHT Arrow key
        Serial.write(buf, 8); // Send keypress
      } else {
        // Release the keyboard
        releaseKey();
      }
    }
  }

  prevState_UP = currRead_UP;
  prevState_LEFT = currRead_LEFT;
  prevState_BACK = currRead_BACK;
  prevState_RIGHT = currRead_RIGHT;

}

void releaseKey() 
{
  buf[0] = 0;
  buf[2] = 0;
  Serial.write(buf, 8); // Release key  
}
