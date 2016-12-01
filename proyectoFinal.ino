 
#define Pecho 6
#define Ptrig 7
long duracion, distancia;
int LM35 = A2;
int dato =0;
boolean prendido = false;

void setup() {                
  Serial.begin (9600);       
  pinMode(Pecho, INPUT);     // define el pin 6 como entrada (ECHO)
  pinMode(Ptrig, OUTPUT);    // define el pin 7 como salida  (TRIGER)
  pinMode(13, 1);    
   pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);        
  }
  
void loop() {
  {
  digitalWrite(Ptrig, LOW);
  delayMicroseconds(2);
  digitalWrite(Ptrig, HIGH);   // genera el pulso de triger por 10ms
  delayMicroseconds(10);
  digitalWrite(Ptrig, LOW);
  
  duracion = pulseIn(Pecho, HIGH);
  distancia = (duracion/2) / 29;            // calcula la distancia en centimetros
  
  if (distancia >= 500 || distancia <= 0){  // si la distancia es mayor a 500cm o menor a 0cm 
    Serial.println("---");                  // no mide
  }
  else {
    Serial.print(distancia);           
    Serial.println("cm");              
    digitalWrite(13, 1);               
  }
  
   if (distancia <= 10 && distancia >= 1){
    digitalWrite(13, 0);                    
    //Serial.println("Alarma.......");        
  }
  delay(400);                               
}
{
  int input = analogRead(LM35);    
  float mv  = (5000 / 1024.0) * input; // Conversio a mV
  float cel = mv / 10;                 // Conversion a grados C
   
  Serial.print(cel);
  Serial.println("°C");
  delay(1000); 
}
{
  if(Serial.available() >0){
    dato = Serial.read();
    
    
    //Serial.write(dato);

    if(dato == 'a' ){
      digitalWrite(13,HIGH);
     
    }

    else if(dato =='a' ){
      digitalWrite(13,LOW);
      
    }
    
    if(dato=='b' && prendido == false){
      digitalWrite(12,HIGH);
      prendido = true;
      
      }

     else if(dato=='b' && prendido == true){
      digitalWrite(12,LOW);
      prendido = false;
      }
  }
  
}
}
