#include <stdio.h>
#include<locale.h>

//leer 10 calificaciones y definir si son erroneas o no
main()
{
	setlocale(LC_ALL,"");
  	int i,erronea=0;
	float calif=0;
  	for (i = 1; i<=10; i++)
	{
   	do{
    	printf("\nEscriba una calificación correcta: ");
    	scanf("%f", &calif);
    	if (calif <0 || calif > 10){
      		erronea=1;
      		printf("\nLa calificación es erronea, introduzca de nuevo: ");
    	}
    	else{
        	erronea = 0;
    	}
    } while (erronea != 0);
    printf("\nGracias!!");
  	}
}
