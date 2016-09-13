#include<stdio.h>

void main(void){
int a=0;
int f=0;
int positivos=0;
int negativos=0;
int par=0;
int impar=0;

for (f=0;f<10;f++){
	printf("Ingrese un número: \n");
	scanf("%d",&a);
		if(a>=0){
		positivos=positivos+1;
			if(a%2==0){
			par=par+1;
			}
			else{
			impar=impar+1;
			}
		}
		else{
		negativos=negativos+1;
			if(a%2==0){
			par=par+1;
			}
			else{
			impar=impar+1;
			}
		}
}
printf("La cantidad de números positivos es:%d\n" ,positivos);
printf("La cantidad de números negativos es:%d\n" ,negativos);
printf("La cantidad de números pares es:%d\n" ,par);
printf("La cantidad de números impares es:%d\n" ,impar);
}
