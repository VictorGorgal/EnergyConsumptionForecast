#include "EmonLib.h"

EnergyMonitor SCT013;

#define pinSCT A7   // Analogic pin connected to the SCT-013

float corrente;
float tensao = 127;
float potencia;

void setup(){
  SCT013.current(pinSCT, 2.9411);
  Serial.begin(115200);
}

void loop(){
  if(Serial.available() > 0){  // Reads the sensor only when requested via Serial
    Serial.readStringUntil('\n');  // Clear the Serial buffer

    for(int i = 0; i < 10; i++){
      corrente = SCT013.calcIrms(1480);   // Calculate the current value
      potencia += corrente * tensao;  // Calculate the power
    }

    potencia /= 10;
    Serial.println(potencia);  // Send the power to the PC via Serial
    potencia = 0;
  }
}
