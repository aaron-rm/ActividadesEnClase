#include <stdio.h>

main()
{
	int dia;
	printf("Introduce el dia: ");
   	scanf("%d",&dia);
	switch(dia)  /* solo puede ser tipo entero o cadena*/
	{
	    case 1: printf("Lunes"); break; /* break, lleva el codigo al final */
	    case 2: printf("Martes"); break;
	    case 3: printf("Miercoles"); break;
	    case 4: printf("Jueves"); break;
	    case 5: printf("Viernes"); break;
	    case 6: printf("Sabado"); break;
		case 7: printf("Domingo"); break;
	}
}
