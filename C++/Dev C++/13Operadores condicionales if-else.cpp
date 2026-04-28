#include <stdio.h>

main() 
{
	int usuario,clave=1234;
	printf("Introduce tu clave: ");
	scanf("%d",&usuario);
	if(usuario==clave) /* Si no se usa doble igual, usuario tomaria el valor de clave*/
	    printf("Acceso permitido");
	else
	    printf("Acceso denegado");
} 
