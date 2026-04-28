/*Realice un programa para determinar cuánto pagará una persona que adquiere N cantidad de artículos,
los cuales están en promoción. Considere que si el precio es mayor o igual a $200 
se le aplica un descuento de 15%, si su precio es mayor a $100 pero menor a $200, 
el descuento es de 12%; de lo contrario, sólo se le aplica 10%. 
Se debe saber cuál es el costo de cada articulo, el descuento que tendrá cada uno de los artículos y 
el precio final de cada articulo. Se debe preparar un informe que muestre esta informacion y 
finalmente cuánto se pagará por todos los artículos obtenidos. 
Utilize funciones para segmentar los procesos que realize el programa.
*/

// Aaron Remarchuk 8-1042-134

#include<stdio.h>
#include<locale.h>

int x=0,i=0;

void inicio()
{
	printf("Cantidad de artículos a vender: ");
	scanf("%d",&x);
}

float rellenarinfo(float precios[])
{
	for(i=0;i<x;i++)
	{
		do
		{
			printf("Inserte el precio del artículo %d: ",i);
			scanf("%f",&precios[i]);
		}	while(precios[i]<0);
	}
	return precios[x];
}

float hacerdescuento(float precios[], float descuentos[])
{
	for(i=0;i<x;i++)
	{
		if(precios[i]>=200)
		{
			descuentos[i]=(precios[i]*.15);
		}
		if(precios[i]<200 && precios[i]>100)
		{
			descuentos[i]=(precios[i]*.12);
		}
		if(precios[i]<=100)
		{
			descuentos[i]=(precios[i]*.10);
		}
	}
	return descuentos[x];
}

float total(float precios[], float descuentos[])
{
	float sum=0;
	for(i=0;i<x;i++)
	{
		sum+=(precios[i]-descuentos[i]);
	}
	return sum;
}

void reporte(float precios[], float descuentos[],float sum)
{
	printf("\n\nCantidad de artículos: %d\n",x);
	printf("Artículo\tPrecio Inicial\t\tDescuento\tPrecio Final\n");
	for(i=0;i<x;i++)
	{
		printf("Artículo %d\t%.2f\t\t\t%.2f\t\t%.2f\n",i,precios[i],descuentos[i],(precios[i]-descuentos[i]));
	}
	printf("Total\t\t\t\t\t\t\t%.2f",total(precios,descuentos));
}

main()
{
	setlocale(LC_ALL,"");
	printf("Rellene la información sobre los productos:\n");
	inicio();
	float precios[x],descuentos[x],sum=0;
	rellenarinfo(precios);
	hacerdescuento(precios,descuentos);
	reporte(precios,descuentos,sum);
}
