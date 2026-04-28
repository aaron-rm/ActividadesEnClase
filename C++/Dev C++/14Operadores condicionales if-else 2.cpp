#include <stdio.h>

main()
{
	int edad;
	printf("Introduce tu edad: ");
   	scanf("%d",&edad);
	if (edad<1)
		printf("Lo siento, te has equivocado.");
	else
		if (edad<3) 
			printf("Eres un bebe");
		else 
			if (edad<13) 
				printf("Eres un nino");
	   		else 
				printf("Eres adulto");
}
