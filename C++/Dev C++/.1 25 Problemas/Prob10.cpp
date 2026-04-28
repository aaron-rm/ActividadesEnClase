//Que lea 5 números por teclado, los copie a otro array multiplicados por 2 y los muestre todos ordenados usando un tercer array.

#include<stdio.h>
#include<locale.h>

main()
{
	setlocale(LC_ALL,"");
	int i,num[5],num2[5],num3[10];
	for(i=0;i<5;i++)
	{
		printf("Inserte el %d número: ",i+1);
		scanf("%d",&num[i]);
	}
	
	for(i=0;i<5;i++)
	{
		num2[i]=2*num[i];
	}
	
	for(i=0;i<5;i++)
	{
		num3[i]=num[i];
		num3[i+5]=num2[i];
	}
	
	for(i=0;i<10;i++)
	{
		printf("%d\n",num3[i]);
	}
}

