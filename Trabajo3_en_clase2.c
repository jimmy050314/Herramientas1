#include<stdio.h>

float suma(float b,float c);
float resta(float b,float c);
float multiplicacion(float b,float c);
int potencia(int e,int f);
long factorial(int e);

void main(void){
int a=0;
float b=0;
float c=0;
float d=0;
int e=0;
int f=0;
int g=0;
int h=0;
int k=0;

while(1){
printf("\nBienvenido, pulse el número de la operación que desea realizar: \n1.Suma. \n2.Resta. \n3.Multiplicación. \n4.Potencia. \n5.Factorial. \n6.Salir. \n");
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
	printf("Para esta operación solo se reciben valores enteros \n");
	printf("Escriba un número: \n");
	scanf("%d",&e);
	printf("Escriba la potencia a la que desea elevar el número: \n");
        scanf("%d",&f);
	g=potencia(e,f);
	printf("El resultado de la potencia es %d.\n",g);
	break;

	case 5:
        printf("Para esta operación solo se reciben valores enteros \n");
	printf("Escriba el número que desea obtener su factorial: \n");
        scanf("%d",&e);
        k=factorial(e);
	printf("El resultado de %d! es %d",e,k);
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
int potencia(int e,int f){
	int g=e;
	int h=0;
	for(int j=0;j<f;j++){
		g=g+h;
		h=0;
		for(int i=1;i<e;i++){
			h=h+g;
		}
	}
	return g;
}
long factorial(int e){
	int f=0;
	long h=0;
	long k=0;
	if(e>0){
	f=e-1;
	k=e;
	for(int i=1;i<e;i++){
		h=0;
		for(int j=1;j<f;j++){
			h=h+k;
		}
	k=k+h;
	f=f-1;
	}
	return k;
	}
}
