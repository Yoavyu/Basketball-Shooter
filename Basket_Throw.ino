#include <Servo.h>
#include <time.h>
Servo xServo;
Servo yServo;
Servo CamServo;

int xServoPin = 9; // x axis servo attached
int yServoPin = 10; // y axis servo attached
int CamServoPin = 11; // camera Servo attached
int potPin = A0; // potentiometer pin
int buttonPin = 2; // button pin
int pos;
int position;
int prev_pos=0;
int button=0;
int start = 35;  // angle starting the throw
int stop = 150; // angle finishing the throw


void setup() {
  // setting up the parts
  Serial.begin(9600);
   xServo.attach(xServoPin);
   yServo.attach(yServoPin);
   CamServo.attach(CamServoPin);
   pinMode(potPin,INPUT);
   pinMode(buttonPin,INPUT);
   yServo.write(start);
}

void loop() {
  pos = analogRead(potPin);
  position = int(map(pos,0,674,60,120)); // getting the value from pot' and mapping it in angle between 60 and 120 
  // then moving xAxisServo and CameraServo toward this value
  xServo.write(position);
  CamServo.write((position));
  Serial.println(position);
  
  delay(100);
  button = digitalRead(buttonPin);
  delay(100);
  if(button == HIGH){ // if button is pressed
    yServo.write(stop);  // throw the ball
    delay(1000);
    yServo.write(start); // return to original posetion
  }
}