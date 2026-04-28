//Crear una matriz de 3 filas por 5 columnas con elementos de tipo int, cargar sus componentes y luego imprimirlas.

#include<stdio.h>

int i,x;
void cargar(int mat[3][5])
{
	for(i=0;i<3;i++)
	{
		for(x=0;x<5;x++)
		{
			printf("Ingrese el valor [%d][%d]: ",i,x);
			scanf("%d",&mat[i][x]);
		}
	}
}

void imprimir(int mat[3][5])
{
	for(i=0;i<3;i++)
	{
		for(x=0;x<5;x++)
		{
			printf("%d\t",mat[i][x]);
		}
		printf("\n");
	}
}

int main()
{
	int mat[3][5];
	cargar(mat);
	imprimir(mat);
}
