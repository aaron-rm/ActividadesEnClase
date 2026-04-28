//Que lea una cadena y diga cuantas mayúsculas hay.

#include<stdio.h>
#include<locale.h>

main()
{
	setlocale(LC_ALL,"");
	int i,cont=0,x;
	char frase[50];
	printf("Inserte una frase: ");
	gets(frase);
	
    for(x=0;x<50;x++)
    {
    	if(frase[x]>=65 && frase[x]<=90) //codigo ASCII para mayusculas
		{
    		cont++;
		}
    	if (frase[x]==0)
    	{
       		break;
    	}
    }
    
	printf("Cantidad de mayúsculas: %d",cont);
}
