#include <stdio.h>
#include <locale.h>


/* while, se usa cuando no ssabemos cuantas veces se repite el ciclo*/
main() 
{
    setlocale(LC_ALL, "");
	int numero=1;
	while(numero<=10) /*while se ejecutara, mientras se cumpla la condicion*/
						/* Evalua la condicion y luego ejecuta el programa */
	{
	    printf("%d\n",numero);
	    numero++;
	}
}
