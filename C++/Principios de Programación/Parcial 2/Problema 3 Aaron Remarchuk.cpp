/* Un profesor tiene un salario inicial de $1,500, y recibe un incremento de 10 % anual durante 6 años.
¿Cuál sera su salario al cabo de 6 años? ¿Qué salario ha recibido en cada uno de los 6 años?. 
Prepare un informe donde se muestre el nombre del profesor y el detalle de los salarios cada año, 
partiendo del año 0 que seria el salario inicial. 
Utilize funciones en el programa.
*/

// Aaron Remarchuk 8-1042-134

#include<stdio.h>
#include<locale.h>

float salario[6];
int i;
char nombre[20];

void aumento()
{
	for(i=1;i<6;i++)
	{
		salario[i]=(salario[i-1]+(salario[i-1]*0.1));
	}
}

float total()
{
	float sum=0;
	for(i=0;i<6;i++)
	{
		sum+=salario[i];
	}
	return sum;
}

void informe()
{
	printf("\n\nNombre del profesor: %s",nombre);
	printf("\nAño 1 \tSalario Inicial \t%.2f\n",salario[0]);
	for(i=1;i<6;i++)
	{
		printf("Año %d \tNuevo Salario \t	%.2f\n",i,salario[i]);
	}
	printf("Total \t\t\t\t%.2f",total());
}

main()
{
	setlocale(LC_ALL,"");
	printf("Nombre del Profesor: ");
	scanf("%s",nombre);
	salario[0]=1500;
	aumento();
	informe();
}
