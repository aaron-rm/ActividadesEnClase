//Que muestre los primeros 100 números de izquierda a derecha usando un array de dos dimensiones, 
//la última fila a mostrará la suma de sus respectivas columnas.

#include<stdio.h>
int i,x;
void rellenar(int num[10][10])
{
	int a=1;
	for(i=0;i<10;i++)
	{
		for(x=0;x<10;x++)
		{
			num[i][x]=a;
			a++;
			printf("%d\t",num[i][x]);
		}
		printf("\n");
	}
}

void sumatotal(int num[10][10])
{
	for(i=0;i<10;i++)
	{
		int a=0;
		for(x=0;x<10;x++)
		{
			a+=num[x][i];
		}
		printf("%d\t",a);
	}
}

main()
{
	int num[10][10];
	rellenar(num);
	printf("\nSuma de columnas: \n");
	sumatotal(num);
}
