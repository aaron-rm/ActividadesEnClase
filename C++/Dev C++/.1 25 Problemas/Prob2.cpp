// rellene un array con los 100 primeros números enteros y los muestre en pantalla en orden descendente.

#include<stdio.h>

main()
{
	int i,num[100];
	for(i=1;i<=100;i++)
	{
		num[i]=i;
	}
	printf("Valores en orden descendente:\n");
	for(i=100;i>0;i--)
	{
		printf("%d\n",num[i]);
	}
}
