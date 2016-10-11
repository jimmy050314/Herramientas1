#include<stdio.h>

void main(void){

float a=0;
float pi=3.141592;
float area=0;
float diam=0;
float circ=0;

printf("Bienvenido, ingrese el valor del radio del círculo para hallar su área, diametro y circunferencia. \n");
printf("Escriba el radio del círculo: ");
scanf("%f",&a);

area=pi*(a*a);
diam=a*2;
circ=pi*diam;

printf("Área=%f. \n",area);
printf("Diametro=%f. \n",diam);
printf("Circunferencia=%f. \n",circ);

}
