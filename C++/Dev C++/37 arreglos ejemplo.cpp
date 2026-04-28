#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<locale.h>

main()
{
	setlocale(LC_ALL,"");
	//Crear un arreglo
	float grupo[10];
	int i;

	//Asignar valores directamente a cada indice
	grupo[0] = 0;
	grupo[1] = 0;
	grupo[2] = 0;


	// Poner el mismo numero a todos los indices
	for(i=0; i<10; i++)
	{
		grupo[i] = 0;
	}
	


	// Mostrar el contenido de cada indice
	for(i=0; i<10; i++)
	{
		printf("En posicion %d el valor es %f\n", i, grupo[i]);
	}

	grupo[0] = 70;
	grupo[1] = 90;
	grupo[2] = 100;

	for(i=0; i<10; i++)
	{
	  printf("En posicion %d el valor es %f\n", i, grupo[i]);
	}


	//Leer datos y guardarlos en el arreglo
	for(i=0; i<10; i++)
	{
		printf("\nEscriba el valor %d: ", i);
		scanf("%f", &grupo[i]);

	}

	for (i=0; i<10; i++){
	  printf("En posicion %d el valor es %f\n", i, grupo[i]);
	}

	// Sumar todos los datos de un arreglo
	float suma =0;
	for(i=0; i<10; i++)
	{
		suma+=grupo[i];
	}
	float media = suma / 10;
	printf("La media es %.2f", media);
					//.2f, muestra 2 decimales
					
	//Obtener el valor máximo y mínimo de un arreglo	
	float max=grupo[0];
	for(i=0; i<10; i++)
	{
		if(grupo[i] > max)
		{
			max=grupo[i];
		}
	}
	printf("\nEl valor máximo es %.2f", max);

	float min=grupo[0];
	for(i=0; i<10; i++)
	{
		if(grupo[i] < min)
		{
			min=grupo[i];
		}
	}
	printf("\nEl valor minimo es %.2f", min);


	/* A cada numero se le resta la media, el resultado se eleva al cuadrado, 
	se suman todos los cuadrados, se dividen entre n y se saca la raiz cuadrada */

	// Ejemplo: obtener la desviación estándar
	float diferencia, cuadrado, total, varianza, devest;

	for(i=0; i<10; i++)
	{
		diferencia = grupo[i]-media;
		cuadrado = diferencia * diferencia;
		total+=cuadrado;
	}
	varianza = total/10;
	devest = sqrt(varianza);
	printf("\nLa desviacion estándar es: %.4f", devest);


}
