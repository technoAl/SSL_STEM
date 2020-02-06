//softare created with the help of arduion.cc/en/Reference

//Microphone Pin Assignments
const int micRF = A4;
const int micRB = A3;
const int micLF = A2;
const int micLB = A1;

//Receiving Bits from RPI and TR
boolean primingBitRPI = false;

const int samples = 1500;
const double freq = 1.0/2500.0 ;//check this
const int wait = 1000;
void setup(){
  pinMode(micRF, INPUT);
  pinMode(micRB, INPUT);
  pinMode(micLF, INPUT);
  pinMode(micLB, INPUT);
  Serial.begin(1000000);//serial connected to Raspberry Pi
}

void loop(){
  //Look for primer bits from TR and RPI
  char RPIbit = Serial.read();
  if(RPIbit == 'r'){
    primingBitRPI = true;
    Serial.write("c");
  }
  
  //record audio if both other devices are ready
  if(primingBitRPI){
      delay(wait);//delay a few seconds for the audio rig to be ready
      int currentSample = 0;
      while(currentSample < samples){//artificially create sample window
        recordBits(currentSample);//record bits
        currentSample++;
      }
      //reset the device after the window was sampled
      primingBitRPI = false;
  }
  
}

void recordBits(long progress){
    //read data from mic array
    unsigned int audRF = analogRead(micRF);
    unsigned int audRB = analogRead(micRB);
    unsigned int audLF = analogRead(micLF);
    unsigned int audLB = analogRead(micLB);
    
    //send data to raspberry pi
    Serial.println(progress);
    Serial.println(audRF);
    Serial.println(audRB);
    Serial.println(audLF);
    Serial.println(audLB);
}
