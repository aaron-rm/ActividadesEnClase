#include <stdio.h>
#include <locale.h>

//leer las temperaturas horarias de cada uno de los dias del año
main()
{
	setlocale(LC_ALL,"");
	int dia=1,hora=1;
	float temperatura;


	for(dia=1;dia<=365;dia++)
	{
		printf("\nDía %d\n", dia);
		for(hora=1;hora<=24;hora++)
		{
			do{
				printf("Temperatura de la hora %d: ", hora);
				scanf("%f", &temperatura);	
			}while(temperatura<0 || temperatura>100);
		}
	}

	
	/*      utilizando do-while
	do{
		hora=1;
		printf("\nDía %d\n", dia);
		do{
			printf("Temperatura de la hora %d: ", hora);
			scanf("%f", &temperatura);	
			hora++;
		}while(hora<=24);
	dia++;
	}while(dia<=365);
	*/
	
	/*    utilizando while
	while(dia<=365){
		printf("\nDía %d\n",dia)
		while(hora<=24){
			printf("Temperatura de la hora %d: ", hora);
			scanf("%f", &temperatura);	
			hora++;
		}
	}
	
	*/
}
