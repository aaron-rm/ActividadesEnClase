#include <stdio.h>

int validarDato() {
    int n;
    //scanf devuelve 1 cuando el formato es aceptado, si el formato es incorrecto devuelve 0
    if (scanf("%d", &n) != 1) {
        printf("Error: inserte un dato valido (formato numerico)\n");
        //se devuelve n=-1, para volver a pedir el dato
        n=-1;
        //limpiamos los datos de entrada, para evitar caer en un bucle
        while (getchar() != '\n');
    }else {
        if (n<=0) {
            printf("Las horas no pueden ser negativas, inserte un dato valido \n");
        }
    }
    return n;
}

int main() {
    int horas1, horas2, horas3;
    int total;
    float promedio;

    // Entrada

    //ciclo para validar entradas
    do {
        printf("Ingrese las horas estimadas para la tarea 1: ");
        horas1=validarDato();
    }while (horas1<=0);

    do{
        printf("Ingrese las horas estimadas para la tarea 2: ");
        horas2=validarDato();
    }while (horas2<0);

    do{
        printf("Ingrese las horas estimadas para la tarea 3: ");
        horas3=validarDato();
    }while (horas3<0);

    // Procesamiento
    total = horas1 + horas2 + horas3;
    promedio = total / 3.0;

    // Salida
    printf("\nResumen de las tareas:\n");
    printf("Tarea 1: %d horas\n", horas1);
    printf("Tarea 2: %d horas\n", horas2);
    printf("Tarea 3: %d horas\n", horas3);
    printf("Total de horas: %d\n", total);
    printf("Promedio de horas: %.2f\n", promedio);

    return 0;
}
