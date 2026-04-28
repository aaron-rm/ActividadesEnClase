//Que lea 10 números por teclado, 5 para un array y 5 para otro array distinto. Mostrar los 10 números en pantalla mediante un solo array.

#include<stdio.h>
#include<locale.h>

main()
{
	setlocale(LC_ALL,"");
	int i,num[10],num2[5],num3[5];
	
	for(i=0;i<5;i++)
	{
		printf("Inserte el %d número: ",i+1);
		scanf("%d",&num2[i]);
	}
	for(i=6;i<=10;i++)
	{
		printf("Inserte el %d número: ",i);
		scanf("%d",&num3[i-5]);
	}
	
	
	for(i=0;i<5;i++)
	{
		num[i]=num2[i];

	}
	for(i=6;i<=10;i++)
	{
		num[i-1]=num3[i-5];
	}
	
	
	for(i=0;i<10;i++)
	{
		printf("%d\n",num[i]);
	}
}
