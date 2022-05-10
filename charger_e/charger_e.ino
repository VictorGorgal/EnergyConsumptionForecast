#include "EmonLib.h"

EnergyMonitor SCT013;

#define pinSCT A7   //Pino analógico conectado ao SCT-013

float corrente;
float tensao = 127;
float potencia;

void setup(){
  SCT013.current(pinSCT, 2.9411);
  Serial.begin(115200);
}

void loop(){
  if(Serial.available() > 0){  // apenas faz a leitura quando for requisitado via serial
    Serial.readStringUntil('\n');  // limpa o buffer serial

    for(int i = 0; i < 10; i++){
      corrente = SCT013.calcIrms(1480);   // Calcula o valor da Corrente
      potencia += corrente * tensao;
    }

    potencia /= 10;
    Serial.println(potencia);
    potencia = 0;
  }
}
