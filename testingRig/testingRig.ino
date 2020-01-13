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
  Serial.println("Begin motor control");
  Serial.println();
  //Print function list for user selection
  Serial.println("Enter number for control option:");
  Serial.println("1 for forward");
  Serial.println("2 for micro");
  Serial.println();
}
//Main loop
void loop() {
  while(Serial.available()){
      user_input = Serial.read(); //Read user input and trigger appropriate function
      digitalWrite(EN, LOW); //Pull enable pin low to set FETs active and allow motor control
      if (user_input =='1')
      {
         StepForwardDefault();
         Serial.print("entered");
      }
      else if(user_input =='2')
      {
        SmallStepMode();
        Serial.print("entered");
      }
      else
      {
        Serial.println("Bad Communication");
      }
      resetBEDPins();
      if(user_input == 'p'){
        playFrequency(440);
      }
  }
  }

void playFrequency(int tones){
  tone(SP, tones);
  delay(50);
  digitalWrite(SP, LOW);//pull pin down
}

void StepForwardDefault()
{
  Serial.println("input steps");
  char input = Serial.read(); //Read user input
  digitalWrite(dir, LOW); //Pull direction pin low to move "forward"
  for(int i= 0; x<input; i++)  //Loop the forward stepping enough times for motion to be visible
  {
    digitalWrite(stp,HIGH); //Trigger one step forward
    delay(1);
    digitalWrite(stp,LOW); //Pull step pin low so it can be triggered again
    delay(1);
  }
  Serial.println("done");
  Serial.println();
}

void SmallStepMode()
{
  Serial.println("Stepping at 1/16th microstep mode, input amount of steps");
  char input = Serial.read(); //Read user input
  digitalWrite(dir, LOW); //Pull direction pin low to move "forward"
  digitalWrite(MS1, HIGH); //Pull MS1,MS2, and MS3 high to set logic to 1/16th microstep resolution
  digitalWrite(MS2, HIGH);
  digitalWrite(MS3, HIGH);
  for(int i= 0; i<input; i++)  //Loop the forward stepping enough times for motion to be visible
  {
    digitalWrite(stp,HIGH); //Trigger one step forward
    delay(1);
    digitalWrite(stp,LOW); //Pull step pin low so it can be triggered again
    delay(1);
  }
  Serial.println("done");
  Serial.println();
}
void resetBEDPins()//reset keeps everything clean
{
  digitalWrite(stp, LOW);
  digitalWrite(dir, LOW);
  digitalWrite(MS1, LOW);
  digitalWrite(MS2, LOW);
  digitalWrite(EN, HIGH);
}
