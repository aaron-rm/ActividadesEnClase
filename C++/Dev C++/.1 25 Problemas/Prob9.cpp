//Que lea 5 números por teclado, los copie a otro array multiplicados por 2 y muestre el segundo array.

#include<stdio.h>
#include<locale.h>

main()
{
	setlocale(LC_ALL,"");
	int i,num[5],num2[5];
	for(i=0;i<5;i++)
	{
		printf("Inserte el %d número: ",i+1);
		scanf("%d",&num[i]);
	}
	
	for(i=0;i<5;i++)
	{
		num2[i]=2*num[i];
	}
	
	printf("Números por 2:");
	for(i=0;i<5;i++)
	{
		printf("\n%d",num2[i]);
	}
}
