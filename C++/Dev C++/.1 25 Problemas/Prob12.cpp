//Que lea 10 números por teclado, los almacene en un array y muestre la media.

#include<stdio.h>
#include<locale.h>
main()
{
	setlocale(LC_ALL,"");
	int i,num[10],sum;
	for(i=0;i<10;i++)
	{
		printf("Inserte el %d número: ",i+1);
		scanf("%d",&num[i]);
	}
	
	sum=0;
	for(i=0;i<10;i++)
	{
		sum+=num[i];
	}
	
	printf("La media es: %d",sum/10);
}
