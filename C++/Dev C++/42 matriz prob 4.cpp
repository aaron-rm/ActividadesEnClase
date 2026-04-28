//Crear y cargar una matriz de 4 filas por 4 columnas. Imprimir la diagonal principal.

#include<stdio.h>

int i,x;
void cargar(int mat[4][4])
{
	for(i=0;i<4;i++)
	{
		for(x=0;x<4;x++)
		{
			printf("Ingrese el valor [%d][%d]: ",i,x);
			scanf("%d",&mat[i][x]);
		}
	}
}

void imprimir(int mat[4][4])
{
		for(i=0;i<4;i++)
	{
		for(x=0;x<4;x++)
		{
			printf("%d\t",mat[i][x]);
		}
		printf("\n");
	}
}

void diag(int mat[4][4])
{
		for(i=0;i<4;i++)
	{
		for(x=0;x<4;x++)
		{
			if(i==x)
			{
				printf("%d\t",mat[i][x]);
			}else printf("\t");
		}
		printf("\n");
	}
}

int main()
{
	int mat[4][4];
	cargar(mat);
	printf("\nLa matriz es:\n");
	imprimir(mat);
	printf("\nLa diagonal principal de la matriz es:\n");
	diag(mat);
}
