#include <stdio.h>
#include<locale.h>

main()
{
	setlocale(LC_ALL,"");
  	int i,j;
  	float suma1=0,suma2=0,calif,promedio1, promedio2;
  	for (i=1;i<=5;i++)
	{
		suma1=0;
    	printf("\nCalificaciones alumno N°%d\n", i);
    	for (j=1;j<=3;j++)
		{
        	do
			{
   			printf("\tInserte la calificación N° %d: ",j);
        	scanf("%f",&calif);
        	}	while(calif<0 || calif>10);
        	suma1=suma1+calif;
    	}
    	promedio1 = suma1/3;
    	printf("\tEl promedio es %f", promedio1);
    	suma2=suma2+promedio1;
  	}
  	promedio2 = suma2 / 5;
  	printf("\n\nEl promedio general es: %f",promedio2);
}
