#include <stdio.h>

int imprimir(int, int, int);
int main(){

    int dia, mes, anio, validar;

    //pedir año mayor a 1900 y menor a 2025
    do{
        validar = 0;
        printf("\n\nIngrese el anio ");
        scanf("%d", &anio);

        //El sistema valida que se ingrese un año dentro del rango establecido
        if(anio<1925 || anio>2024)
        {
            validar=1;
            printf("\nIngrese un anio entre 1900 y 2024");
        }
    }while(validar == 1);

    //pedir mes
    do{
        validar = 0;
        printf("\n\nIngrese el numero de mes ");
        scanf("%d", &mes);

        //El sistema valida que se ingrese un mes correcto
        if(mes<1|| mes>12)
        {
            validar=1;
            printf("\nIngrese un numero de mes correcto");
        }
    }while(validar == 1);

    //pedir dia
    do{
        validar = 0;
        printf("\n\nIngrese el numero de dia ");
        scanf("%d", &dia);

        //El sistema valida si el dia ingresado cumple con el limite de dias por mes
        if(mes == 4 || mes == 6 || mes == 9 || mes == 11)
        {
            if( dia > 31)
            {
                validar = 1;
                printf("Ingrese un numero de dia correcto");
            }
        }
        else if( mes == 2)
        {
            if(dia>30)
            {
                validar = 1;
                printf("Ingrese un numero de dia correcto");
            }
        }
        else
        {
            if(dia>32)
            {
                validar = 1;
                printf("Ingrese un numero de dia correcto");
            }
        }
    }while(validar == 1);

    imprimir(dia,mes,anio);


}

int imprimir (int x, int y, int z)
{
    printf("\nLa fecha ingresada es: %d/%d/%d", x,y,z);
    return 0;
}
