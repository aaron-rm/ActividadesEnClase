/*Se requiere un algoritmo para determinar, de N cantidades, 
cuántas son cero, cuántas son menores a cero, y cuántas son mayores a cero. 
De igual forma se debe determinar cua es el numero mayor y cual es el menor de la lista de numeros.  
Realice el programa utilizando el ciclo apropiado y utilizando funciones.
*/

// Aaron Remarchuk	8-1042-134

#include<stdio.h>
#include<locale.h>

int x=0,i=0;

void cero(float num[], int x)
{
	int cont=0;
	for(i=0;i<x;i++)
	{
		if(num[i]==0)
		{
			cont++;
		}
	}
	printf("La cantidad de números que son cero: %d\n",cont);
}

void menorcero(float num[], int x)
{
	int cont=0;
	for(i=0;i<x;i++)
	{
		if(num[i]<0)
		{
			cont++;
		}
	}
	printf("La cantidad de números menores a cero: %d\n",cont);
}

void mayorcero(float num[], int x)
{
	int cont=0;
	for(i=0;i<x;i++)
	{
		if(num[i]>0)
		{
			cont++;
		}
	}
	printf("La cantidad de números mayores a cero: %d\n",cont);
}

void mayor(float num[], int x)
{
	int mayor=0;
	for(i=0;i<x;i++)
	{
		if(num[i]>mayor)
		{
			mayor=num[i];	
		}
	}
	printf("El número mayor es: %d\n",mayor);	
}

void menor(float num[], int x)
{
	int menor=0;
	for(i=0;i<x;i++)
	{
		if(num[i]<menor)
		{
			menor=num[i];	
		}
	}
	printf("El número mayor es: %d\n",menor);
}

main()
{
	setlocale(LC_ALL,"");
	do
	{
		printf("Inserte la cantidad de números a evaluar: ");
		scanf("%d",&x);
	} while(x<0);
	float num[x];
	for(i=0;i<x;i++)
	{
		printf("Inserte el número %d: ",i);
		scanf("%f",&num[i]);
	}
	printf("\n");
	
	cero(num,x);
	menorcero(num,x);
	mayorcero(num,x);
	mayor(num,x);
	menor(num,x);
}
