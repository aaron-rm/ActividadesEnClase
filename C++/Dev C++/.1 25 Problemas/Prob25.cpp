/*  Que gestiona las notas de una clase de 20 alumnos de los cuales sabemos el nombre y la nota. 
	El programa debe ser capaz de:
		
		Buscar un alumno.
		Modificar su nota.
		Realizar la media de todas las notas.
		Realizar la media de las notas menores de 5.
		Mostrar el alumno que mejores notas ha sacado.
		Mostrar el alumno que peores notas ha sacado. */
		
#include<stdio.h>
#include<locale.h>

float nota[20];
char alumno[20][30];

void lista()
{
	int i;
	printf("\n\nLista de Alumnos:");
	for(i=0;i<20;i++)
	{
		printf("\nAlumno %d:\n",i);
		printf("Nombre: %s\n",alumno[i]);
		printf("Calificaci�n: %f\n",nota[i]);
	}
}

void verifnota(int i)
{
	printf("Nota (0-10): ");
	scanf("%f",&nota[i]);
	while(nota[i]<0 || nota[i]>10)
	{
		printf("Nota (0-10): ");
		scanf("%f",&nota[i]);
	}
}

void cambiarnombre(int i)
{
	printf("Nuevo nombre: ");
	scanf("%s",alumno[i]);
}

bool igual(char a[0][30], int i)
{
	int y,x,cont;
	while(a[0][x]!=0)
	{
		x++;
	}
	for(i=0;i<20;i++)
	{
		for(y=0;y<x;y++)
		{
			if(a[0][y]==alumno[i][y]) cont++;
		}
	}

	if(cont==x) return true;
	else return false;
}

void fillinfo()
{
	int i=0;
	printf("\n\nRellene la informaci�n de los alumnos:");
	for(i=0;i<20;i++)
	{
		printf("\nAlumno %d:\n",i);
		printf("Nombre: ");
		scanf("%s",alumno[i]);
		verifnota(i);
	}
	int a=0,b=0;
	printf("�Desea editar alguna informaci�n?\n");
	do
	{
		printf("1- Si\n2- No\n");
		scanf("%d",&a);	
	}	while(a!=1 && a!=2);
	if(a==1)
	{
		printf("�Qu� n�mero de estudiante desea editar?\n");
		scanf("%d",&i);
		printf("\nAlumno %d:\n",i);
		printf("Nombre: %s",alumno[i]);
		printf("\n�Desea cambiar el nombre?\n");
		do
		{
			printf("1- Si\n2- No\n");
			scanf("%d",&a);	
		}	while(a!=1 && a!=2);
		if(a==1)
		{
			cambiarnombre(i);
		}
		printf("Calificaci�n: %f\n",nota[i]);
		printf("�Desea cambiar la calificaci�n?\n");
		do
		{
			printf("1- Si\n2- No\n");
			scanf("%d",&a);	
		}	while(a!=1 && a!=2);
		if(a==1)
		{
			verifnota(i);
		}
	}
	
}

void buscar()
{
	lista();
	printf("\n\nBuscar a un alumno:\n");
	int z=0,b=0,i=0;
	char a[0][30];
	while(z!=3)
	{
		do
		{
			printf("Buscar por: \n");
			printf("1- Nombre \n2- N�mero\n");
			scanf("%d",&z);
		}	while(z!=1 && z!=2);
		if(z==1)
		{
			printf("Nombre del alumno que desea buscar: ");
			scanf("%s",a);
			
			if(igual(a,i))
			{
				printf("Alumno encontrado\n");				
				printf("\nAlumno %d:\n",i);
				printf("Nombre: %s",alumno[i]);
				printf("\n�Desea cambiar el nombre?\n");
				do
				{
					printf("1- Si\n2- No\n");
					scanf("%d",&b);	
				}	while(b!=1 && b!=2);
				if(b==1)
				{
					cambiarnombre(i);
				}
				printf("�Desea cambiar la calificaci�n?\n");
				do
				{
					printf("1- Si\n2- No\n");
					scanf("%d",&b);	
				}	while(b!=1 &&b!=2);
				if(b==1)
				{
					verifnota(i);
				}
			}	else printf("No se ha encontrado al alumno\n");
		}
		if(z==2)
		{
			do
			{
				printf("N�mero del alumno que desea buscar: ");
				scanf("%d",&i);
			}	while(i<0||i>20);
			printf("Alumno encontrado\n");				
			printf("Alumno %d:\n",i);
			printf("Nombre: %s",alumno[i]);
			printf("\n�Desea cambiar el nombre?\n");
			do
			{
				printf("1- Si\n2- No\n");
				scanf("%d",&b);	
			}	while(b!=1 && b!=2);
			if(b==1)
			{
				cambiarnombre(i);
			}
			printf("�Desea cambiar la calificaci�n?\n");
			do
			{
				printf("1- Si\n2- No\n");
				scanf("%d",&b);	
			}	while(b!=1 && b!=2);
			if(b==1)
			{
				verifnota(i);
			}
		}
		printf("\n�Intentar nuevamente?\n");
		do
		{
			printf("1- Si\n2- No\n");
			scanf("%d",&b);
		}	while(b!=1 && b!=2);
		if(b==2) z=3;
	}
}

void media()
{
	int i;
	float sum=0;
	for(i=0;i<20;i++)
	{
		sum+=nota[i];
	}
	printf("La media de las notas es: %.2f", sum/20);
}

void media5()
{
	int i,c=0;
	float sum=0;
	for(i=0;i<20;i++)
	{
		if(nota[i]<5)
		{
			sum+=nota[i];
			c++;
		}
	}
	printf("La media de las notas menores a 5 es: %.2f", sum/c);
}

void mejor()
{
	int i,a,b,c;
	for(i=0;i<20;i++)
	{
		nota;
	}
	printf("Alumno con las mejores notas: %s", alumno[i]);
}

void peor()
{
	int i;
	
	printf("Alumno con las peores notas: %s", alumno[i]);
}

main()
{
	setlocale(LC_ALL,"");
	int opcion=0;
	while(opcion!=7)
	{
		printf("\n\n------------------------------------------------------------------\n");
		printf("\nMenu\n");
		printf("1- Rellenar informaci�n de alumnos\n");
		printf("2- Buscar un alumno\n");
		printf("3- Realizar media de todas las notas\n");
		printf("4- Realizar media de las notas menores de 5\n");
		printf("5- Mostrar el alumno que mejores notas ha sacado\n");
		printf("6- Mostrar el alumno que peores notas ha sacado\n");
		printf("7- Salir\n");
		printf("\nSeleccione una opci�n: ");
		scanf("%d",&opcion);
		switch(opcion)
		{
			case 1: fillinfo(); opcion=0; break;
			case 2: buscar(); opcion=0; break;
			case 3: media(); opcion=0; break;
			case 4: media5(); opcion=0; break;
			case 5: mejor(); opcion=0; break;
			case 6: peor(); opcion=0; break;
		}		
	}
	printf("------------------------------------------------------------------\n");
}
