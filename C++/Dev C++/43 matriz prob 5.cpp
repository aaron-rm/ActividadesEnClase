//Crear y cargar una matriz de 3 filas por 4 columnas. Imprimir la primer fila. Imprimir la última fila e imprimir la primer columna.

#include<stdio.h>

int i,x;
void cargar(int mat[3][4])
{
	for(i=0;i<3;i++)
	{
		for(x=0;x<4;x++)
		{
			printf("Inserte el valor [%d][%d]: ",i,x);
			scanf("%d",&mat[i][x]);
		}
	}
}

void imprimir(int mat[3][4])
{
	for(i=0;i<3;i++)
	{
		for(x=0;x<4;x++)
		{
			printf("%d\t",mat[i][x]);
		}
		printf("\n");
	}
}

void imprimir1(int mat[3][4]) //primera fila
{
	for(i=0;i<4;i++)
	{
			printf("%d\t",mat[0][i]);
	}
	printf("\n");
}

void imprimir2(int mat[3][4]) //ultima fila y primer columna
{
	for(i=0;i<2;i++)
	{
		printf("%d\n",mat[i][0]);
	}
	for(i=0;i<4;i++)
	{
		printf("%d\t",mat[2][i]);
	}
}

int main()
{
	int mat[3][4];
	cargar(mat);
	printf("\nLa matriz es: \n");
	imprimir(mat);
	printf("\nLa primera fila es: \n");
	imprimir1(mat);
	printf("\nLa ultima fila y la primera columna son: \n");
	imprimir2(mat);
}
