//softare created with the help of arduion.cc/en/Reference

#include <SoftwareSerial.h>

const int rxPin = 0;
const int txPin = 1;
SoftwareSerial tr(rxPin, txPin);


//Microphone Pin Assignments
const int micRF = A4;
const int micRB = A3;
const int micLF = A2;
const int micLB = A1;

//Receiving Bits from RPI and TR
boolean primingBitRPI = false;
boolean primingBitTR = false;

const int sampleWindowWidth = 1000;//length of each window check in milliseconds

void setup(){
  pinMode(micRF, INPUT);
  pinMode(micRB, INPUT);
  pinMode(micLF, INPUT);
  pinMode(micLB, INPUT);

  Serial.begin(9600);//serial connected to Raspberry Pi
  tr.begin(9600);//serial connected to Testing Rig
}

void loop(){
  //Look for primer bits from TR and RPI
  char RPIbit = Serial.read();
  char TRbit = tr.read();
  if(RPIbit != ' '){
    primingBitRPI = true;
  }
  if(TRbit != ' '){
    primingBitTR = true;
  }
  
  //record audio if both other devices are ready
  if(primingBitRPI && primingBitTR){
    long startPt = millis();//starting time
    long currentPt = millis();
    long progress = currentPt - startPt;
    while(progress < sampleWindowWidth){//artificially create sample window
      recordBits(progress);//record bits
    }

    //reset the device after the window was sampled
    primingBitRPI = false;
    primingBitTR = false;
  }
  
}

void recordBits(long progress){
    //read data from mic array
    float audRF = analogRead(micRF);
    float audRB = analogRead(micRB);
    float audLF = analogRead(micLF);
    float audLB = analogRead(micLB);

    //send data to raspberry pi
    Serial.println("Time ");
    Serial.println(progress);
    Serial.println("audRF");
    Serial.println(audRF);
    Serial.println("audRB");
    Serial.println(audRB);
    Serial.println("audLF");
    Serial.println(audLF);
    Serial.println("audLB");
    Serial.println(audLB);
}


