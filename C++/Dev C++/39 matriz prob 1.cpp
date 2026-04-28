// Crear una matriz de 3 filas por 5 columnas con elementos de tipo int, cargar sus componentes y luego imprimirlas

#include<stdio.h>

main()
{
	int x,y,num[3][5];
	for(x=0;x<3;x++)
	{
		for(y=0;y<5;y++)
		{
			printf("Inserte el valor [%d][%d]: ",x,y);
			scanf("%d",&num[x][y]);
		}
	}
	printf("\nLa matriz es:");
	for(x=0;x<3;x++)
	{
		for(y=0;y<5;y++)
		{
			if(y%5==0)
			{
				printf("\n");
			}
			printf("%d\t",num[x][y]);
		}
	}
}
