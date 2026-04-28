//un array con los números primos comprendidos entre 1 y 100 y los muestre en pantalla en orden ascendente.

#include<stdio.h>
#include<locale.h>

main()
{
	setlocale(LC_ALL,"");
	int i=0,x,z,cont,num[100];
    for (x=1;x<=100;x++)
    {
    	cont=0;
        for (z=1;z<=x;z++)
		{
    		if (x%z==0) //si x, se puede dividir enteramente entre z, el contador aumenta
            {
            	cont++;
            }
        }
       
        if (cont==2) //si el contador es 2, x se dividio entre 1 y entre si mismo
        {
         num[i]=x; //i se inicializa en 0, los valores de x se almacenaran
         i++;   //aumenta la cantidad de numeros primos, para su impresion
        }
       
    }
        for (x=0;x<i;x++) 
        {
        	printf("%d\n",num[x]);
    	}
}




