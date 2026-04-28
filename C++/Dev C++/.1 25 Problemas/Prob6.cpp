//lea 10 números por teclado, los almacene en un array y muestre la suma, resta, multiplicación y división de todos.

#include<stdio.h>
#include<locale.h>

main()
{
	setlocale(LC_ALL,"");
	int suma,resta,mult,div,i,num[10];
	for(i=0;i<10;i++)
	{
		printf("Inserte el %d número: ",i+1);
		scanf("%d",&num[i]);
	}
	
	suma=num[0];
	resta=num[0];
	mult=num[0];
	div=num[0];
	
	for(i=1;i<10;i++)
	{
		suma+=num[i];
		resta-=num[i];
		mult*=num[i];
		div/=num[i];
	}
	
	printf("La suma total es: %d\n",suma);
	printf("La resta total es: %d\n",resta);	
	printf("La multiplicación total es: %d\n",mult);
	printf("La división entera es: %d\n",div);
}
