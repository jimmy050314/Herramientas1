#include<stdio.h>

float suma(float b,float c);
float resta(float b,float c);
float multiplicacion(float b,float c);

void main(void){
int a=0;
float b=0;
float c=0;
float d=0;
float e=0;

while(1){
printf("\nBienvenido, pulse el número de la operación que desea realizar: \n1.Suma. \n2.Resta. \n3.Multiplicación. \n4.Salir. \n");
scanf("%d",&a);

if(a>0 && a<7){

switch(a){
	case 1:
	printf("Escriba un número: \n");
	scanf("%f",&b);
	printf("Escriba el número con el que desea sumarlo: \n");
	scanf("%f",&c);
	d=suma(b,c);
	printf("El resultado de la suma entre %f y %f es %f.\n",b,c,d);
        break;

        case 2:
        printf("Escriba un número: \n");
        scanf("%f",&b);
        printf("Escriba el número con el que desea restarlo: \n");
        scanf("%f",&c);
        d=resta(b,c);
        printf("El resultado de la resta entre %f y %f es %f.\n",b,c,d);
        break;

        case 3:
        printf("Escriba un número: \n");
        scanf("%f",&b);
        printf("Escriba el número con el que desea multiplicarlo: \n");
        scanf("%f",&c);
        d=multiplicacion(b,c);
        printf("El resultado de la multiplicación entre %f y %f es %f.\n",b,c,d);
        break;

        case 4:
	printf("Fin del programa.\n");
	return;
	break;

}
}
else{
	printf("El número ingresado no es valido\n");
}
}
}

float suma(float b,float c){
	return b+c;
}
float resta(float b,float c){
	return b-c;
}
float multiplicacion(float b,float c){
	float e=0;
	for(int f=0;f<c;f++){
		e=e+b;
		}
	return e;
}
