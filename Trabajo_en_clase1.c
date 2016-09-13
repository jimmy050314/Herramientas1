#include<stdio.h>

void main(void){
int a,b;
printf("Ingrese un número: \n");
scanf("%d",&a);
printf("Ingrese otro número: \n");
scanf("%d",&b);

	if(a>b){
	printf("El número mayor es:%d\n" ,a);
	}
	else{
	printf("El número mayor es:%d\n" ,b);
	}
}
