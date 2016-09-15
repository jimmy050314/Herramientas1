#include<stdio.h>

void main(void){
int a=0;

printf("Ingrese un número: \n");
scanf("%d",&a);

while(a<=0){
printf("Ingrese un número: \n");
scanf("%d",&a);
}

while(a>0){
printf("El número ingresado fue %d y es positivo \n",a);
return;
}

}
