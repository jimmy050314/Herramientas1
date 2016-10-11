#include<stdio.h>

void main(void){

float a[5];
float sum=0;
float prom=0;

printf("Bienvenido, ingrese los 5 datos para obtener su promedio y la sumatoria. \n");
printf("Escriba el primer número: ");
scanf("%f",&a[0]);
printf("Escriba el segundo número: ");
scanf("%f",&a[1]);
printf("Escriba el tercero número: ");
scanf("%f",&a[2]);
printf("Escriba el cuarto número: ");
scanf("%f",&a[3]);
printf("Escriba el último número: ");
scanf("%f",&a[4]);

sum=a[0]+a[1]+a[2]+a[3]+a[4];
prom=sum/5;

printf("Sumatoria=%f. \n",sum);
printf("Promedio=%f. \n",prom);

}
