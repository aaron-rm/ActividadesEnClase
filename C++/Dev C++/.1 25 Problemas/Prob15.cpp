//Que pinte un tablero de ajedrez, los peones con la letra P, las torres con T, los caballos con C, los alfiles con A, el rey con R y la reina con M.

#include<stdio.h>

int x,y;
void vaciar(char tablero[10][10])
{
	for(x=0;x<10;x++)
	{
		for(y=0;y<10;y++)
		{
			tablero[x][y]=0;
		}
	}
}

void llenar(char tablero[10][10])
{
	for(y=1;y<=8;y++)//peones
	{
		tablero[2][y]='P';
		tablero[7][y]='P';
	}
	tablero[1][1]='T';
	tablero[8][8]='T';
	tablero[8][1]='T';
	tablero[1][8]='T';
	tablero[1][2]='C';	
	tablero[1][7]='C';
	tablero[8][2]='C';
	tablero[8][7]='C';
	tablero[1][3]='A';
	tablero[1][6]='A';
	tablero[8][3]='A';
	tablero[8][6]='A';
	tablero[1][4]='M';
	tablero[1][5]='R';
	tablero[8][4]='M';
	tablero[8][5]='R';
}

void print(char tablero[10][10])
{
	for(x=0;x<10;x++)
	{
		for(y=0;y<10;y++)
		{
			printf("%c\t",tablero[x][y]);
		}
		printf("\n");
	}
}

main()
{
	char tablero[10][10];
	vaciar(tablero);
	llenar(tablero);
	printf("Tablero de ajedrez:\n");
	print(tablero);
}
