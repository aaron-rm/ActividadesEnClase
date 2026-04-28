//Que lea 10 números por teclado, los almacene en un array y los ordene de forma ascendente.

#include<stdio.h>
#include<locale.h>

main()
{
	setlocale(LC_ALL,"");
	int i,x,z,num[10];
	
	for(i=0;i<10;i++)
	{
		printf("Inserte el numero %d: ",i+1);
		scanf("%d",&num[i]);
	}
	
	for(i=0;i<10;i++)
	{
		for(x=0;x<10;x++)
		{
			if(num[x]>num[i])
			{
				z=num[x];
				num[x]=num[i];
				num[i]=z;
			}
		}
	}
	
	printf("\nNúmeros ordenados:");
	for(i=0;i<10;i++)
	{
		printf("\n%d",num[i]);
	}
}
