//Que lea una cadena y la muestre al revés.

#include <stdio.h>

int main()
{

    int indice,x;
    char frase[50];
   
    printf("Introduzca una frase: ");
    gets(frase);
   
    for(x=0;x<50;x++)
    {
      	if (frase[x]==0)
      	{
       		indice=x;
       		break;
      	}
    }
   
    printf("\nLa frase al reves es:\n");
    
    for(x=indice-1;x>=0;x--)
	{
      	printf("%c",frase[x]);
    }
}
