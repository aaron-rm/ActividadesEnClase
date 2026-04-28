/*
1SF115
Joseph Alvarez
Helen Bolanos
Jaziel Gonzalez
Dilam Jimenez
Aaron Remarchuk
*/


//Construye programa que, al recibir como dato un número entero positivo, 
//escriba una figura como la que se muestra a continuación (ejemplo para N = 7): 
//	1
//	1	2	1
//	1	2	3	2	1
//	1	2	3	4	3	2	1
//	1	2	3	4	5	4	3	2	1	
//	1	2	3	4	5	6	5	4	3	2	1
//	1	2	3	4	5	6	7	6	5	4	3	2	1


#include<stdio.h>
#include<locale.h>

void imprimir(int n)
{
	int i,x;
	for (i=1;i<=n;i++) 
	{
		for (x=1;x<=i;x++)
		{
			printf("%d ",x);
		}
		for (x=i-1;x>=1;x--)
		{
			printf("%d ",x);
		}
		printf("\n");
	}
}

main()
{
	int n;
	setlocale(LC_ALL,"");
	do
	{
		printf("Inserte un número N: ");
		scanf("%d",&n);
	}	while(n<0);
	printf("\n\nFigura:\n");
	imprimir(n);
}
