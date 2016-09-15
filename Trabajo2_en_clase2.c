#include<stdio.h>

void main(void){
int a=0;
float b=0;
float c=0;
float d=0;
float f=0;
float e=0;
float g=0;

while(1){
printf("\nBienvenido, pulse el número de la operación que desea realizar: \n1.Suma. \n2.Resta. \n3.Multiplicación. \n4.División. \n5.Potencia. \n6.Salir. \n");
scanf("%d",&a);

if(a>0 && a<7){
	while(a==0){
	printf("Fin del programa. \n");
	}
switch(a){
	case 1:
	printf("Escriba un número: \n");
	scanf("%f",&b);
	printf("Escriba el número con el que desea sumarlo: \n");
	scanf("%f",&c);
	d=b+c;
	printf("El resultado de la suma entre %f y %f es %f.\n",b,c,d);
        break;

        case 2:
        printf("Escriba un número: \n");
        scanf("%f",&b);
        printf("Escriba el número con el que desea restarlo: \n");
        scanf("%f",&c);
        d=b-c;
        printf("El resultado de la resta entre %f y %f es %f.\n",b,c,d);
        break;

        case 3:
        printf("Escriba un número: \n");
        scanf("%f",&b);
        printf("Escriba el número con el que desea multiplicarlo: \n");
        scanf("%f",&c);
        d=b*c;
        printf("El resultado de la multiplicación entre %f y %f es %f.\n",b,c,d);
        break;

        case 4:
        printf("Escriba un número: \n");
        scanf("%f",&b);
        printf("Escriba el número con el que desea dividirlo: \n");
        scanf("%f",&c);
        d=b/c;
        printf("El resultado de la división entre %f y %f es %f.\n",b,c,d);
        break;

        case 5:
        printf("Escriba un número: \n");
        scanf("%f",&b);
        printf("Escriba el número con el que desea hacer la potencia: \n");
        scanf("%f",&c);
	d=1;
	g=b;
	e=1;
	for(f=d;f<=c;f++){
	e=g*e;
}
        printf("El resultado de %f a la %f es %f.\n",b,c,e);
        break;

	case 6:
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
