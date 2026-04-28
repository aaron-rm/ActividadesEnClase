#include <stdio.h>
//variables globales, se declara fuera de main
//en este caso 'a' es una variable global

int a;
main()
{
	int b=4;
	//las variables locales se declaran dentro de main
	//b solo tiene valor dentro de b
	printf("b es local y vale %d",b);
	a=5;
	printf("\na es global y vale %d",a);
} 
