//Que rellene una matriz de 3x3 y muestre su traspuesta (la traspuesta se consigue intercambiando filas por columnas y viceversa).

#include<stdio.h>

int x,y;
void ask(int mat[3][3])
{
	for(x=0;x<3;x++)
	{
		for(y=0;y<3;y++)
		{
			printf("Inserte el valor[%d][%d]: ",x,y);
			scanf("%d",&mat[x][y]);
		}
	}
}

void print(int mat[3][3])
{
	for(x=0;x<3;x++)
	{
		for(y=0;y<3;y++)
		{
			printf("%d\t",mat[x][y]);
		}
		printf("\n");
	}
}

int clon(int mat[3][3], int mat2[3][3])
{
	for(x=0;x<3;x++)
	{
		for(y=0;y<3;y++)
		{
			mat2[x][y]=mat[x][y];
		}
	}
	return mat2[3][3];
}

int traspuesta(int mat[3][3], int mat2[3][3])
{
	for(x=0;x<3;x++)
	{
		for(y=0;y<3;y++)
		{
			mat[y][x]=mat2[x][y];
		}
	}
	return mat[3][3];
}

main()
{
	int mat[3][3],mat2[3][3];
	ask(mat);
	clon(mat,mat2);
	printf("La matriz es: \n");
	print(mat);
	printf("\nLa matriz traspuesta es: \n");
	traspuesta(mat,mat2);
	print(mat);
}
