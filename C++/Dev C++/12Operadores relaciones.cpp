#include <stdio.h>

main() 
{
	int a,b;
	printf("Introduce el valor de A: ");
	scanf("%d",&a);
   	printf("Introduce el valor de B: ");
   	scanf("%d",&b);
   	if(a>b)			
		printf("A es mayor que B");
	else 
	   	if(a<b)
	    	printf("B es mayor que A"); 
	   	else
	  		printf("A y B son iguales");
}
