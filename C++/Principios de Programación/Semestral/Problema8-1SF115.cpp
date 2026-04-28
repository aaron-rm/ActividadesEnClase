/*
1SF115
Joseph Alvarez
Helen Bolanos
Jaziel Gonzalez
Dilam Jimenez
Aaron Remarchuk
*/


/*En un país hubo elecciones para elegir al presidente. 
El país consta de 10 provincias o regiones, 
de las cuales se han levantado actas que contiene el total de votos obtenidos por los 5 partidos políticos en dicha región. 
Diseñe un programa en c, que lea las actas de las 10 provincias, muestre que partido ganó las elecciones y en caso de empate, lo especifique con un mensaje. */

#include<stdio.h>
#include<locale.h>

int i=0, x=0, max_indice, provincias_votos[10][5], suma[5];

void votos()
{
	for(x=0;x<10;x++)
	{
		printf("Provincia %d:\n",x+1);
		for(i=0;i<5;i++)
		{
			
			do
			{
				printf("Inserte los votos del partido %d: ",i+1);
				scanf("%d",&provincias_votos[x][i]);
			} while(provincias_votos[x][i]<0);
		}
		printf("\n");
	}

}

void sumar_votos()
{
	for(i=0;i<5;i++)
	{
		for(x=0;x<10;x++)
		{
			suma[i]+=provincias_votos[x][i];
		}
	}
}

void encontrar_maximo()
{
    int max_votos = suma[0];
    
    for(i=1;i<5; i++)
	{
		if(suma[i]>max_votos)
		{
            max_votos = suma[i];
            max_indice = i;
        }
    }
}

bool empate()
{
	for(i=0;i<5;i++)
	{
		if(i==max_indice)
		{
			break;
		}
		if(suma[i]<suma[max_indice])
		{
			return true;
		}
	}
	return false;
}

main()
{
	setlocale(LC_ALL,"");
	votos();	
	sumar_votos();
	encontrar_maximo();
	if(empate())
	{
		printf("El ganador es el partido %d",max_indice+1
		);
	} else printf("Hay un empate");
}
