#include <stdio.h>
#define pi 3.1416
#define escribe printf
//#define se utiliza para declarar constantes

main()
{
	int r;
	escribe("Introduce el radio: ");
	scanf("%d",&r);
	//se utiliza & para leer un numero en la consola
	escribe("El perímetro es: %f",2*pi*r);
	//se utiliza %f para escribir un valor flotante o real
}
