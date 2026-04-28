#include<stdio.h>
#include<locale.h>

void visualizar(int []);	
void visualizar(int array[]) 
{
	int i;
	for (i=0;i<25;i)
	{
		printf("%d\t",array[i]);
		i+=1;
		if(i%3==0) printf("\n");	
	}  
	//al no utilizar getcha, un indice del arreglo, puede tener mas de un numero
}

main()
{
	setlocale(LC_ALL,"");
	int array[25],i;
	for (i=0;i<25;i++)
	{
		printf("Elemento nº %d: ",i+1);
		scanf("%d",&array[i]);
	}
	visualizar(&array[0]);
}
