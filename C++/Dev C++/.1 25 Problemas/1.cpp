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

int i;

void RellenarInfo()
{
	
}

void ModificarNotas()
{
	
}

main()
{
	setlocale(LC_ALL,"");
	while(i!=7)
	{
	printf(" Menú \n 1- Rellenar Información \n 2- Modificar Notas \n 7- Salir \n Seleccione una Opción: ");
	scanf("%d",&i);	
	switch(i)
	{
		case 1: RellenarInfo(); i=0; break;
		case 2: ModificarNotas(); i=0; break;
	}
	}
	
}

