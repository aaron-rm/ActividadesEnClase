// rellene un array con los 100 primeros números enteros y los muestre en pantalla en orden ascendente.

#include<stdio.h>

main()
{
	int i,num[100];
	for(i=1;i<=100;i++)
	{
		num[i]=i;
	}
	printf("Valores en orden ascendente:\n");
	for(i=1;i<=100;i++)
	{
		printf("%d\n",num[i]);
	}
}
