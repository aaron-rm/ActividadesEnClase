#include <stdio.h>

main()
{		
	int x,y,numeros[3][4];	//esto genera una matriz 3 x 4
	for (x=0;x<3;x++)
	{
		for (y=0;y<4;y++)
		{
			printf("Introduzca el valor %d, %d: ",x,y);
			scanf("%d",&numeros[x][y]);
		}
	}		
	printf("\n\nLa matriz es: \n");
	for (x=0;x<3;x++)
	{
			for (y=0;y<4;y++)
			{
				if(y%4==0)
				{
					printf("\n");
				}
				printf("%d\t",numeros[x][y]);
			}
	}
	
	
	
	int a,b,num[3][4]={1,2,3,4,5,6,7,8,9,10,11,12};
	for(a=0;a<3;a++)
	{
		for(b=0;b<4;b++)
		{
			if(b%4==0)
			{
				printf("\n");
			}
			printf("indice[%d][%d] = %d\t",a,b,num[a][b]);
		}
	}
	
	

	char dias[7][10]={"lunes","martes","miércoles","jueves","viernes","sábado","domingo"};
	int i,z;
	for(i=0;i<7;i++)
	{
			printf("%s\t",dias[i]);
	}
	
	
}
