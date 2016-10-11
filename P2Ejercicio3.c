#include<stdio.h>

void main(void){

int a[3];
int b=0;
int c=0;
int res=0;

printf("Bienvenido,ingrese 3 números, el módulo y la operación que desea realizar. \n");
printf("Ingrese la operación que desea realizar: \n1.Suma. \n2.Resta. \n3.Multiplicación. \n");
scanf("%d",&c);

printf("Escriba el primer número: ");
scanf("%d",&a[0]);
printf("Escriba el segundo número: ");
scanf("%d",&a[1]);
printf("Escriba el tercer número: ");
scanf("%d",&a[2]);
printf("Escriba el módulo: ");
scanf("%d",&b);

if(c<4 && c>0){
	switch(c){
		case 1:
		res=(a[0]%b)+(a[1]%b)+(a[2]%b);
		printf("Resultado=%d \n",res);
		break;

                case 2:
                res=(a[0]%b)-(a[1]%b)-(a[2]%b);
                printf("Resultado=%d \n",res);
                break;

                case 3:
                res=(a[0]%b)*(a[1]%b)*(a[2]%b);
                printf("Resultado=%d \n",res);
                break;

	}
}
else{
printf("El número ingresado no es válido");
}
}
