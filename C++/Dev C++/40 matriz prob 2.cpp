// Crear una matriz de 4 x 4 que imprima la diagonal principal

#include<stdio.h>

main()
{

	int x,y,num[4][4]={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
	printf("\nLa matriz es:");
	for(x=0;x<4;x++)
	{
		for(y=0;y<4;y++)
		{
			if(y%4==0)
			{
				printf("\n");
			}
			printf("%d\t",num[x][y]);
		}
	}
	
	printf("\n\nLa diagonal principal es:");
	for(x=0;x<4;x++)
	{
		for(y=0;y<4;y++)
		{
			if(y%4==0)
			{
				printf("\n");
			}
			if(x==y)
			{
				printf("%d\t",num[x][y]);	
			}
			printf("\t");
		}
	}
	
	printf("\n\nLa diagonal principal es:");
	for(x=0;x<4;x++)
	{
		for(y=0;y<4;y++)
		{
			if(y%4==0)
			{
				printf("\n");
			}
			if(x!=y)
			{
				num[x][y]=0;	
			}
			printf("%d\t",num[x][y]);
		}
	}
}
