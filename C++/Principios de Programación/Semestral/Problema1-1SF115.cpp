/*
1SF115
Joseph Alvarez
Helen Bolanos
Jaziel Gonzalez
Dilam Jimenez
Aaron Remarchuk
*/


#include <string.h> 
#include <stdio.h> 
#include <stdlib.h>
#include <locale.h> 
#include <ctype.h>

void mensaje(void);
char Pedir_dia(char*);

int main()
{ 
	setlocale(LC_ALL,"");
    int horas, minutos;
    float subtotal, valor_total;
    const float VALOR_MEDIO_MINUTO = 0.30, VALOR_HORA = 0.60, DESCUENTO = 0.1256;
    char dia[8];

    mensaje();
    
    Pedir_dia(dia);//lee el dia
    dia[strcspn(dia,"\n")] = '\0'; //elimina el '\n'

    //Pedir minuto y hora
	do{
    printf("Digite las horas transcurridas: ");
    scanf("%d",&horas);		
	} while(horas<0);

    do{
	printf("Digite los minutos transcurridos: ");
    scanf("%d",&minutos);	
	} while(minutos<0||minutos>=60);


    //Validar horas y minutos
    if(horas==0 && minutos<=10)
    {
        printf("Los primeros 10 minutos son gratis. %cBuen viaje!",173);
    }
    else if (horas>=0 && minutos>10)
    {
        //Calcular total a pagar
        subtotal += (horas*VALOR_HORA);
        subtotal += minutos*VALOR_MEDIO_MINUTO;
        if(strcmp(dia,"lunes")==0||strcmp(dia,"Lunes")==0||strcmp(dia,"LUNES")==0||strcmp(dia,"sabado")==0||strcmp(dia,"Sabado")==0||strcmp(dia,"SABADO")==0)
        {
            printf("\nComo el dia es %s aplica para descuento.\n",dia);
            valor_total = subtotal - (subtotal*DESCUENTO);
        }

        //Imprimir resumen
        printf("\nTiempo Transcurrido\nDia: %s\nHoras: %d, minutos: %d\n\n",dia,horas,minutos);
        printf("Subtotal: %.2f\n",subtotal);
        printf("\nDescuento: %.2f%\n",(DESCUENTO*100));
        printf("Monto descontado: %.2f\n",(valor_total*DESCUENTO));
        printf("Total a pagar: %.2f",valor_total);

        printf("\n%cBuen viaje!",173);
    }

    return 0;
}

void mensaje(void)
{
    printf("Bienvenido. Calcularemos su total a pagar de estacionamiento\n");
    printf("Nota: Digite cantidades positivas.\nEscriba el día de la semana sin tildes.\n\n");
}

char Pedir_dia(char dia[8])
{
	while(1)
	{
		int valido=1,i=0;
		
		printf("Escriba el nombre del día de la semana (ejemplo: martes, Martes o MARTES)\nDía: ");
		scanf(" %s", dia);
		for(i=0; i<=dia[i];i++)
		{
			if(!isalpha(dia[i]))
			{
				printf("      Solo debe haber letras.\n");
				while(getchar()!='\n');
				valido-=1;
			}
		}
		
		if(valido)
		{
			break;
		}
		
	}
}
