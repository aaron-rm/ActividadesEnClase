/*Que gestione los datos de stock de una tienda de comestibles, la información a recoger será: nombre del producto, precio, cantidad en stock. La tienda dispone de 10 productos distintos. 
	El programa debe ser capaz de:

		Dar de alta un producto nuevo.
		Buscar un producto por su nombre.
		Modificar el stock y precio de un producto dado.	*/

#include<stdio.h>
#include<locale.h>

int stock[10];
float precio[10];
char producto1[20], producto2[20], producto3[20], producto4[20], producto5[20], producto6[20], producto7[20], producto8[20], producto9[20], producto10[20];


void dardealta()
{
	printf("\n\nDar de alta un producto\n");
	printf("Nombre del producto 1: ");
	scanf("%s",producto1);
	printf("Nombre del producto 2: ");
	scanf("%s",producto2);
	printf("Nombre del producto 3: ");
	scanf("%s",producto3);
	printf("Nombre del producto 4: ");
	scanf("%s",producto4);
	printf("Nombre del producto 5: ");
	scanf("%s",producto5);
	printf("Nombre del producto 6: ");
	scanf("%s",producto6);
	printf("Nombre del producto 7: ");
	scanf("%s",producto7);
	printf("Nombre del producto 8: ");
	scanf("%s",producto8);
	printf("Nombre del producto 9: ");
	scanf("%s",producto9);
	printf("Nombre del producto 10: ");
	scanf("%s",producto10);
	int i;
	for(i=0;i<10;i++)
	{
		printf("\nProducto %d\n",i+1);
		printf("Inserte el precio del producto %d: ",i+1);
		scanf("%f",&precio[i]);
		printf("Inserte la cantidad en stock del producto %d: ",i+1);
		scanf("%d",&stock[i]);
	}
}

void productoactual(int i)
{
	i-=1;
	printf("\nPrecio del Producto actual: %f",precio[i]);
	printf("\nStock del Producto actual: %d",stock[i]);
}

void buscar()
{
	int i,opcion,restart;
	do
	{
		while(opcion!=11)
		{
			printf("\n\nBuscar un producto\n");
			printf("Lista de productos:\n");
			printf("Producto 1: %s\n",producto1);
			printf("Producto 2: %s\n",producto2);
			printf("Producto 3: %s\n",producto3);
			printf("Producto 4: %s\n",producto4);
			printf("Producto 5: %s\n",producto5);
			printf("Producto 6: %s\n",producto6);
			printf("Producto 7: %s\n",producto7);
			printf("Producto 8: %s\n",producto8);
			printf("Producto 9: %s\n",producto9);
			printf("Producto 10: %s\n",producto10);
			printf("11- Salir \n");
			printf("Número del producto que desea buscar: ");
			scanf("%d",&opcion);
			switch(opcion)
			{
				case 1: i=1; printf("\nProducto %d: %s",i,producto1); productoactual(i); opcion=11; break;
				case 2: i=2; printf("\nProducto %d: %s",i,producto2); productoactual(i); opcion=11; break;
				case 3: i=3; printf("\nProducto %d: %s",i,producto3); productoactual(i); opcion=11; break;
				case 4: i=4; printf("\nProducto %d: %s",i,producto4); productoactual(i); opcion=11; break;
				case 5: i=5; printf("\nProducto %d: %s",i,producto5); productoactual(i); opcion=11; break;
				case 6: i=6; printf("\nProducto %d: %s",i,producto6); productoactual(i); opcion=11; break;
				case 7: i=7; printf("\nProducto %d: %s",i,producto7); productoactual(i); opcion=11; break;
				case 8: i=8; printf("\nProducto %d: %s",i,producto8); productoactual(i); opcion=11; break;
				case 9: i=9; printf("\nProducto %d: %s",i,producto9); productoactual(i); opcion=11; break;
				case 10: i=10; printf("\nProducto %d: %s",i,producto10); productoactual(i); opcion=11; break;
			}	
			printf("\n\n¿Buscas algún otro producto?\n");
			printf("1- Si\n2- No\n:");
			scanf("%d",&restart);
		}
		opcion=0;
	}while(restart==1);
	
	
	
}

void modificar(int i)
{
	i-=1;
	printf("\n\nPrecio nuevo del Producto: ");
	scanf("%f",&precio[i]);
	printf("Stock nuevo del Producto: ");
	scanf("%d",&stock[i]);
}

void menumodificar()
{
	int i,opcion,restart;
	do
	{
		while(opcion!=11)
		{
			printf("\n\nModificar un producto\n");
			printf("Lista de productos:\n");
			printf("Producto 1: %s\n",producto1);
			printf("Producto 2: %s\n",producto2);
			printf("Producto 3: %s\n",producto3);
			printf("Producto 4: %s\n",producto4);
			printf("Producto 5: %s\n",producto5);
			printf("Producto 6: %s\n",producto6);
			printf("Producto 7: %s\n",producto7);
			printf("Producto 8: %s\n",producto8);
			printf("Producto 9: %s\n",producto9);
			printf("Producto 10: %s\n",producto10);
			printf("11- Salir \n");
			printf("Número del producto que desea modificar: ");
			scanf("%d",&opcion);
			switch(opcion)
			{
				case 1: i=1; printf("\nProducto %d: %s",i,producto1); productoactual(i); modificar(i); opcion=11; break;
				case 2: i=2; printf("\nProducto %d: %s",i,producto2); productoactual(i); modificar(i); opcion=11; break;
				case 3: i=3; printf("\nProducto %d: %s",i,producto3); productoactual(i); modificar(i); opcion=11; break;
				case 4: i=4; printf("\nProducto %d: %s",i,producto4); productoactual(i); modificar(i); opcion=11; break;
				case 5: i=5; printf("\nProducto %d: %s",i,producto5); productoactual(i); modificar(i); opcion=11; break;
				case 6: i=6; printf("\nProducto %d: %s",i,producto6); productoactual(i); modificar(i); opcion=11; break;
				case 7: i=7; printf("\nProducto %d: %s",i,producto7); productoactual(i); modificar(i); opcion=11; break;
				case 8: i=8; printf("\nProducto %d: %s",i,producto8); productoactual(i); modificar(i); opcion=11; break;
				case 9: i=9; printf("\nProducto %d: %s",i,producto9); productoactual(i); modificar(i); opcion=11; break;
				case 10: i=10; printf("\nProducto %d: %s",i,producto10); productoactual(i); modificar(i); opcion=11; break;
			}
			printf("\n\n¿Modificar algún otro producto?\n");
			printf("1- Si\n2- No\n:");
			scanf("%d",&restart);	
		}
		opcion=0;
	}while(restart==1);
}

main()
{
	setlocale(LC_ALL,"");
	int opcion;
	printf("\n-----------------------------------------------------------\n");
	while(opcion!=4)
	{
		printf("\n\nMenú\n");
		printf("1- Dar de alta un producto\n");
		printf("2- Buscar un producto\n");
		printf("3- Modificar el stock y precio del producto\n");
		printf("4- Salir\n");
		scanf("%d",&opcion);
		switch(opcion)
		{
		    case 1: dardealta(); opcion=0; break;
		    case 2: buscar(); opcion=0; break;
		    case 3: menumodificar(); opcion=0; break;
		}
	}
	printf("\n-----------------------------------------------------------\n");
}
