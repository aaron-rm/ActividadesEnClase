//Que mediante un array almacene números tanto positivos como negativos y los muestre ordenados.

#include<stdio.h>
#include<locale.h>

main()
{
	setlocale(LC_ALL,"");
	int a,b,i,c;
	printf("Inserte un número negativo: ");
	scanf("%d",&a);
	printf("Inserte un número positivo: ");
	scanf("%d",&b);
	c=(-a)*b;
	int num[c+1];
	
	for(i=0;i<c;i++)
	{
		for(a;a<=b;a++)
		{
			
		}
	}
	
	for(i=0;i<c;i++)
	{
		printf("%d\n",num[i]);
	}
}
