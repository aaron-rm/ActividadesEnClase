#include <stdio.h>

main() 
{
	char cad[]="El valor de";
	//char declara caracter y []
	int a=-15;
	unsigned int b=3; 
	//unsigned elimina los signos del valor
	float c=932.5;
	printf("%s a es %d\n",cad,a);
	//%s se utiliza para string
	printf("%s b es %u\n",cad,b);
	//%u es un entero sin signo
	printf("%s c es %e o %f",cad,c,c);
	//%e es para numero exponenciales
}
