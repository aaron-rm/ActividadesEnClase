//Que muestre los primeros 100 números de izquierda a derecha usando un array de dos dimensiones.

#include<stdio.h>

main()
{
	int i,x,a=1,num[10][10];
	for(i=0;i<10;i++)
	{
		for(x=0;x<10;x++)
		{
			num[i][x]=a;
			a++;
			printf("%d ",num[i][x]);
		}
		printf("\n");
	}
}
