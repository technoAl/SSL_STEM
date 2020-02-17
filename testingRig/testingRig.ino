//Declare pin functions on Arduino
#define stp 2
#define dir 3
#define MS1 4
#define MS2 5
#define MS3 6
#define EN  7
#define SP  9

//Declare variables for functions
char user_input;
int r = 1;
int x;
int y;
int state;

void setup() {
  pinMode(stp, OUTPUT);
  pinMode(dir, OUTPUT);
  pinMode(MS1, OUTPUT);
  pinMode(MS2, OUTPUT);
  pinMode(MS3, OUTPUT);
  pinMode(EN, OUTPUT);
  pinMode(SP, OUTPUT);
  resetBEDPins(); //Set step, direction, microstep and enable pins to default states
  Serial.begin(9600); //Open Serial connection for debugging
//  Serial.println("Begin motor control");
//  Serial.println();
//  Serial.println("Enter number for control option:");
//  Serial.println("1 for forward");
//  Serial.println("2 for micro");
//  Serial.println();
  //Print function list for user selection
  
}
//Main loop
void loop() {
  if(Serial.available()){  
      user_input = Serial.read(); //Read user input and trigger appropriate function
      char input2 = Serial.read();
      r = r * (user_input - '0');  //conveting the value of chars to integer
      digitalWrite(EN, LOW); //Pull enable pin low to set FETs active and allow motor control
      //StepForwardDefault();
      //Serial.println("got one");
      if (user_input == '1')
      { 
         StepForwardDefault();
         //tone(13,440);
         delay(50);
         //mtone(13, 0);
      }
      else if(user_input == '0')
      {
       delay(1000);
       tone(11, 600, 500);
       delay(750);
       digitalWrite(11, LOW);
      }

//      else
//      {
//        Serial.println("Bad Communication");
//      }
//      resetBEDPins();
//      if(user_input == 'p'){
//        playFrequency(440);
//      }
  }
}

void playFrequency(int tones){
  tone(SP, tones);
  delay(50);
  digitalWrite(SP, LOW);//pull pin down
}

void StepForwardDefault()
{
  //Serial.println("input steps");
  
//  char input = Serial.read(); //Read user input
//  while(input == -1){ 
//    input = Serial.read();
//  }
  digitalWrite(dir, LOW); //Pull direction pin low to move "forward"
  for(int i= 0; i<20; i++)  //Loop the forward stepping enough times for motion to be visible
  { 
    digitalWrite(stp,HIGH); //Trigger one step forward
    delay(1);
    digitalWrite(stp,LOW); //Pull step pin low so it can be triggered again
    delay(1);
  }
  
  //Serial.println(count);
  //Serial.println();
}

void SmallStepMode()
{

  digitalWrite(dir, LOW); //Pull direction pin low to move "forward"
  digitalWrite(MS1, HIGH); //Pull MS1,MS2, and MS3 high to set logic to 1/16th microstep resolution
  digitalWrite(MS2, HIGH);
  digitalWrite(MS3, HIGH);
  for(int i= 0; i<30; i++)  //Loop the forward stepping enough times for motion to be visible
  {
    digitalWrite(stp,HIGH); //Trigger one step forward
    delay(1);
    digitalWrite(stp,LOW); //Pull step pin low so it can be triggered again
    delay(1);
  }

}
void resetBEDPins()//reset keeps everything clean
{
  digitalWrite(stp, LOW);
  digitalWrite(dir, LOW);
  digitalWrite(MS1, LOW);
  digitalWrite(MS2, LOW);
  digitalWrite(EN, HIGH);
}
