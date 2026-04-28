//un array con los números impares comprendidos entre 1 y 100 y los muestre en pantalla en orden ascendente.

#include<stdio.h>
#include<locale.h>

main()
{
	setlocale(LC_ALL,"");
	int x,z,i=0,cont,num[100];
	for(x=1;x<=100;x++)
	{
		if(x%2==1)
		{
			cont++;
			num[i]=x;
			i++;
		}
	}
	printf("Números impares de 1 a 100");
	for(z=0;z<i;z++)
	{
		printf("\n%d",num[z]);
	}
}
