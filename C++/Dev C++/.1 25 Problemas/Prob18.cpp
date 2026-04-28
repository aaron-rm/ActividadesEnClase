//Que rellene un array de dos dimensiones con números pares, lo pinte y después que pida una posición X,Y y mostrar el número correspondiente.

#include<stdio.h>

int x,y;
void rellenar(int num[10][10])
{
	int a=1;
	for(x=0;x<10;x++)
	{
		for(y=0;y<10;y++)
		{
			while(a%2!=0)
			{
				a++;
			}
			num[x][y]=a;
			a++;
		}
	}
}

void print(int num[10][10])
{
	for(x=0;x<10;x++)
	{
		for(y=0;y<10;y++)
		{
			printf("%d\t",num[x][y]);
		}
		printf("\n");
	}
}

main()
{
	int num[10][10];
	rellenar(num);
	print(num);
	printf("Inserte una posicion [x][y], separadas por un espacio: ");
	scanf("%d %d",&x,&y);
	printf("Su numero es: %d", num[x][y]);
}
