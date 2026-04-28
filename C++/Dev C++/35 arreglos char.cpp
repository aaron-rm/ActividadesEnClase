
#include<stdio.h>
#include<conio.h>

main(){
	char cadena[20];
	int i;
	for (i=0;i<19 && cadena[i-1]!=13;i++)
		cadena[i]=getche( ); 
		//al utilizar getche, el indice solo puede contener un caracter
	if (i==19) cadena[i]='\0';
	else cadena[i-1]='\0';
	printf("\n%s",cadena);
}
