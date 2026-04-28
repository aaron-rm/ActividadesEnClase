/*
1SF115
Joseph Alvarez
Helen Bolanos
Jaziel Gonzalez
Dilam Jimenez
Aaron Remarchuk
*/


#include <stdio.h>
#include <stdlib.h> // Para usar system()

// Declaración de funciones
float prom(int[]);
void mostrarPromedios(int[], int[], int[], int[], int[], int[]);
void mostrarExtremos(int[], int[], int[], int[], int[], int[], const char *[]);

int main()
{
    int menu, x, temp;
    // Inicialización de las variables
    int norte[12] = {0}, centro[12] = {0}, sur[12] = {0}, golfo[12] = {0}, pacifico[12] = {0}, caribe[12] = {0};
    char salir = 'n'; // Inicializamos con 'n' para entrar al bucle
    int seleccionadas[6] = {0, 0, 0, 0, 0, 0}; // Bandera para controlar regiones seleccionadas
    const char *meses[] = {
        "Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"};
    const char *regiones[] = {"Norte", "Centro", "Sur", "Golfo", "Pacifico", "Caribe"};

    do
    {
        // Limpia la pantalla al inicio de cada iteración
        system("cls");

        printf("\nBienvenido al centro meteorologico de Baja California\n\n");
        printf("Seleccione la region que desea trabajar:\n\n");
        printf("1. Norte\n2. Centro\n3. Sur\n4. Golfo\n5. Pacifico\n6. Caribe\n7. Salir del programa\n");

        // Validación para evitar que el usuario ingrese caracteres no válidos
        if (scanf("%d", &menu) != 1 || menu < 1 || menu > 7)
        {
            system("cls");
            printf("ERROR! Por favor, seleccione un numero entre 1 y 7 para el menu: \n");
            while (getchar() != '\n'); // Limpiar el buffer de entrada
            system("pause");
            continue;
        }

        if (menu == 7)
        {
            salir = 'x';
            continue; // Salir del bucle
        }

        if (seleccionadas[menu - 1] == 1)
        {
            printf("Esta region ya ha sido seleccionada! Elija otra region.\n");
            system("pause"); // Pausa para que el usuario lea el mensaje antes de limpiar
            continue; // Volvemos al inicio del bucle
        }

        seleccionadas[menu - 1] = 1; // Marcamos la región como seleccionada

        system("cls");
        printf("Ingrese la temperatura por mes para la region seleccionada:\n");
        for (x = 0; x < 12; x++)
        {
            printf("%d. %s: ", x + 1, meses[x]);

            // Validación de entrada para la temperatura:
            while (scanf("%d", &temp) != 1)
            {
                printf("Entrada invalida. Por favor, ingrese un numero entero para %s: ", meses[x]);
                while (getchar() != '\n'); // Limpia el buffer de entrada
            }

            // Guarda la temperatura en la región correspondiente
            switch (menu)
            {
            case 1:
                norte[x] = temp;
                break;
            case 2:
                centro[x] = temp;
                break;
            case 3:
                sur[x] = temp;
                break;
            case 4:
                golfo[x] = temp;
                break;
            case 5:
                pacifico[x] = temp;
                break;
            case 6:
                caribe[x] = temp;
                break;
            }
        }

        printf("\nDatos ingresados correctamente!\n");

        // Verifica si todas las regiones han sido completadas
        if (seleccionadas[0] == 1 && seleccionadas[1] == 1 && seleccionadas[2] == 1 &&
            seleccionadas[3] == 1 && seleccionadas[4] == 1 && seleccionadas[5] == 1)
        {
            system("cls");
            printf("Ver datos finales\n");
            system("pause");
            system("cls");
            mostrarPromedios(norte, centro, sur, golfo, pacifico, caribe);
            mostrarExtremos(norte, centro, sur, golfo, pacifico, caribe, meses);
            salir = 'x';
        }

        system("pause"); // Pausa antes de limpiar la pantalla

    } while (salir != 'x');

    return 0;
}

// Función para calcular el promedio
float prom(int a[])
{
    int x;
    float media = 0; // Inicializar media en 0
    for (x = 0; x < 12; x++)
    {
        media += a[x];
    }
    return media / 12; // Dividir por la cantidad de meses
}

// Función para mostrar los promedios de todas las regiones
void mostrarPromedios(int norte[], int centro[], int sur[], int golfo[], int pacifico[], int caribe[])
{
    

    printf("\n=== Promedios Anuales por Region ===\n");
    printf("Norte: %.2f\n", prom(norte));
    printf("Centro: %.2f\n", prom(centro));
    printf("Sur: %.2f\n", prom(sur));
    printf("Golfo: %.2f\n", prom(golfo));
    printf("Pacifico: %.2f\n", prom(pacifico));
    printf("Caribe: %.2f\n", prom(caribe));
    printf("====================================\n");
    system("pause");
    system("cls");

    printf("\n=== Promedio mas alto entre las regiones Sur-Pacifico-Caribe ===\n");
    if(prom(sur)>prom(pacifico) && prom(sur)>prom(caribe))
    {
        printf("Sur tiene el promedio mas alto: %2.f\n", prom(sur));
        printf("====================================\n");
        system("pause");
        system("cls");
    }

    else if(prom(pacifico)>prom(sur) && prom(pacifico)>prom(caribe))
    {
        printf("Pacifico tiene el promedio mas alto: %2.f\n", prom(pacifico));
        printf("====================================\n");
        system("pause");
        system("cls");
    }

    else
    {
        printf("Caribe tiene el promedio mas alto: %2.f\n", prom(caribe));
        printf("====================================\n");
        system("pause");
        system("cls");
    }
}

// Función para mostrar la temperatura más alta, más baja y las regiones correspondientes
void mostrarExtremos(int norte[], int centro[], int sur[], int golfo[], int pacifico[], int caribe[], const char *meses[])
{
    int *regiones[] = {norte, centro, sur, golfo, pacifico, caribe};
    const char *nombresRegiones[] = {"Norte", "Centro", "Sur", "Golfo", "Pacifico", "Caribe"};
    int maxTemp = -9999, minTemp = 9999, mesMax = 0, mesMin = 0;
    const char *regionMax = NULL, *regionMin = NULL;

    // Buscar la temperatura máxima y mínima
    for (int r = 0; r < 6; r++)
    {
        for (int m = 0; m < 12; m++)
        {
            if (regiones[r][m] > maxTemp)
            {
                maxTemp = regiones[r][m];
                mesMax = m;
                regionMax = nombresRegiones[r];
            }
            if (regiones[r][m] < minTemp)
            {
                minTemp = regiones[r][m];
                mesMin = m;
                regionMin = nombresRegiones[r];
            }
        }
    }

    printf("\n=== Extremos de Temperatura ===\n");
    printf("Temperatura maxima: %d en %s (%s)\n", maxTemp, meses[mesMax], regionMax);
    printf("Temperatura minima: %d en %s (%s)\n", minTemp, meses[mesMin], regionMin);
    printf("================================\n");
}
