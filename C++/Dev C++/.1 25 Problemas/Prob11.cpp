//Que rellene un array con los 100 primeros números pares y muestre su suma.

#include<stdio.h>
main()
{
	int i,cont=0,num[100],x=0,suma;
	for(i=1;i<=100;i++)
	{
		if(i%2==0)
		{
			cont++;
			num[x]=i;
			x++;
		}
	}
	
	suma=num[0];
	for(i=1;i<cont;i++)
	{
		suma+=num[i];
		printf("%d\n",num[i]);
	}
	printf("La suma es: %d",suma);
}
