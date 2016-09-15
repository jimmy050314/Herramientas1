#include<stdio.h>
#include<string.h>

char main(){
char letras [26]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char a;
char b;
int c;
int d;
int f;
char g;
printf("Ingrese una letra: \n");
scanf("%c%*c",&a);

if(a=='a'){
c=0;
}
if(a=='b'){
c=1;
}
if(a=='c'){
c=2;
}
if(a=='d'){
c=3;
}
if(a=='e'){
c=4;
}
if(a=='f'){
c=5;
}
if(a=='g'){
c=6;
}
if(a=='h'){
c=7;
}
if(a=='i'){
c=8;
}
if(a=='j'){
c=9;
}
if(a=='k'){
c=10;
}
if(a=='l'){
c=11;
}
if(a=='m'){
c=12;
}
if(a=='n'){
c=13;
}
if(a=='o'){
c=14;
}
if(a=='p'){
c=15;
}
if(a=='q'){
c=16;
}
if(a=='r'){
c=17;
}
if(a=='s'){
c=18;
}
if(a=='t'){
c=19;
}
if(a=='u'){
c=20;
}
if(a=='v'){
c=21;
}
if(a=='w'){
c=22;
}
if(a=='x'){
c=23;
}
if(a=='y'){
c=24;
}
if(a=='z'){
c=25;
}

printf("La letra ingresada fue %c\n",a);

printf("Ingrese otra letra: \n");
scanf("%c",&b);

if(b=='a'){
d=0;
}
if(b=='b'){
d=1;
}
if(b=='c'){
d=2;
}
if(b=='d'){
d=3;
}
if(b=='e'){
d=4;
}
if(b=='f'){
d=5;
}
if(b=='g'){
d=6;
}
if(b=='h'){
d=7;
}
if(b=='i'){
d=8;
}
if(b=='j'){
d=9;
}
if(b=='k'){
d=10;
}
if(b=='l'){
d=11;
}
if(b=='m'){
d=12;
}
if(b=='n'){
d=13;
}
if(b=='o'){
d=14;
}
if(b=='p'){
d=15;
}
if(b=='q'){
d=16;
}
if(b=='r'){
d=17;
}
if(b=='s'){
d=18;
}
if(b=='t'){
d=19;
}
if(b=='u'){
d=20;
}
if(b=='v'){
d=21;
}
if(b=='w'){
d=22;
}
if(b=='x'){
d=23;
}
if(b=='y'){
d=24;
}
if(b=='z'){
d=25;
}

printf("La letra ingresada fue %c\n",b);

if(a>b){
	int u=d;
	printf("Las letras entre %c y %c son %c",a,b,letras[u]);
	u=u+1;
	for(f=d;f<c;f++){
	printf("%c",letras[u]);
	u=u+1;
	}
//	printf("%c\n",f);
}
else{
        int u=c;
        printf("Las letras entre %c y %c son %c",a,b,letras[u]);
        u=u+1;
        for(f=c;f<d;f++){
        printf("%c",letras[u]);
        u=u+1;
        }
}
printf("\n");
}

