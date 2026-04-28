//Que lea una cadena y diga cuantas vocales hay.

#include<stdio.h>

main()
{
	int i,cont=0,x;
	char frase[50];
	printf("Inserte una frase: ");
	gets(frase);
	
    for(x=0;x<50;x++)
    {
    	if (frase[x]==0)
    	{
       		break;
    	}
    }
    
    while(frase[i]!=0)
    {
    	if(frase[i]=='a'||frase[i]=='e'||frase[i]=='i'||frase[i]=='o'||frase[i]=='u'||
		frase[i]=='A'||frase[i]=='E'||frase[i]=='I'||frase[i]=='O'||frase[i]=='U')
    	{
    		cont++;
		}
    	i++;
	}
	printf("Cantidad de vocales: %d",cont);
}
