//crear matriz a:3x3, b:3x3 y c:suma de a y b

#include<stdio.h>

int i,x, C[3][3];
void cargar(int A[3][3])
{
	for(i=0;i<3;i++)
	{
		for(x=0;x<3;x++)
		{
			printf("Inserte el valor [%d][%d]: ",i,x);
			scanf("%d",&A[i][x]);
		}
	}
}

void imprimir(int A[3][3])
{
	for(i=0;i<3;i++)
	{
		for(x=0;x<3;x++)
		{
			printf("%d\t",A[i][x]);
		}
		printf("\n");
	}
}

int suma(int A[3][3], int B[3][3])
{
	for(i=0;i<3;i++)
	{
		for(x=0;x<3;x++)
		{
			C[i][x]=A[i][x]+B[i][x];
		}
	}
	return C[3][3];
}

int main()
{
	int A[3][3], B[3][3];
	printf("Inserte valores de la matriz A: \n");
	cargar(A);
	printf("\nInserte valores de la matriz B: \n");
	cargar(B);
	printf("\nMatriz A: \n");
	imprimir(A);
	printf("\nMatriz B: \n");
	imprimir(B);
	printf("\nLa matriz C o la suma de matrices es: \n");
	suma(A,B);
	imprimir(C);
}
