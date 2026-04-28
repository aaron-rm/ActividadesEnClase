//Que lea una cadena y la encripte sumando 3 al código ASCII de cada carácter. Mostrar por pantalla.

#include<stdio.h>

main()
{
	int i=0,x;
	char frase[50];
	printf("Inserte una frase: ");
	gets(frase);
    printf("\nLa frase es: %s",frase);
    
    for(x=0;x<50;x++)
    {
    	if (frase[x]!=0)
    	{
   			frase[x]=frase[x]+3;
    	}
    }
    
    printf("\n\nLa nueva frase es: %s",frase);
}
