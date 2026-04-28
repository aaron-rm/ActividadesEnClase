/* 	&& 	AND
	|| 	OR
	! 	NOT */

#include <stdio.h>

main()
{
	int numero;
	printf("Introduce un numero: ");
	scanf("%d",&numero);
	if(!(numero>=0)) /* cambia el valor de num>=o, es lo mismo que num<0*/
		printf("El número es negativo");
	else 
		if((numero<=100)&&(numero>=25)) /* Ambos deben ser verdaderos */
	    	printf("El numero esta entre 25 y 100");
	   	else 
			if((numero<25)||(numero>100)) /* Uno de los dos es verdadero*/
	      		printf("El numero no esta entre 25 y 100");
}
