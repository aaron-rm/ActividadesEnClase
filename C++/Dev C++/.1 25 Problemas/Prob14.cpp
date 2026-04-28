//14. Que rellene un array con 20 números y luego busque un número concreto.

#include<stdio.h>
int i,x;

void pedir(int mat[20])
{
	for(i=0;i<20;i++)
	{
		printf("Inserte valor [%d]: ",i);
		scanf("%d",&mat[i]);
	}
}

main()
{
	int a,mat[20];
	pedir(mat);
	printf("Inserte el numero que desea buscar: ");
	scanf("%d",&a);
	x=0;
	while(mat[x]!=a)
	{	
		x++;
	}
	printf("Su numero esta en la posicion %d",x);
}
