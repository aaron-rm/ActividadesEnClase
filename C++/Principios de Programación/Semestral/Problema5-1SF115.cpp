/*
1SF115
Joseph Alvarez
Helen Bolanos
Jaziel Gonzalez
Dilam Jimenez
Aaron Remarchuk
*/


#include <stdio.h>

// Prototipo de la función
float saldo_actual(float saldo_anterior, float monto_compras, float pago_realizado, float *pago_minimo, float *pago_sin_intereses, float *intereses_generados, float *multa_aplicada);

int main()
{
    int n = 0;

    // Solicitar el número de clientes
    printf("Ingrese el numero de clientes que desea calcular: \n");
    scanf("%d", &n);

    // Crear un array para almacenar los saldos actuales de los clientes
    float clientes[n];

    // Variables para almacenar los datos de entrada por cliente
    float saldo_anterior, monto_compras, pago_realizado;
    float pago_minimo, pago_sin_intereses, intereses_generados, multa_aplicada;
    float total_ganado = 0; // Acumulador para intereses + multas de todos los clientes

    // Bucle para cada cliente
    for (int x = 0; x < n; x++)
    {
        printf("\nCliente %d:\n", x + 1);

        // Solicitar los datos del cliente
        printf("Ingrese el saldo anterior: ");
        scanf("%f", &saldo_anterior);

        printf("Ingrese el monto de las compras: ");
        scanf("%f", &monto_compras);

        printf("Ingrese el pago realizado: ");
        scanf("%f", &pago_realizado);

        // Calcular el saldo actual y los pagos relacionados
        clientes[x] = saldo_actual(saldo_anterior, monto_compras, pago_realizado, &pago_minimo, &pago_sin_intereses, &intereses_generados, &multa_aplicada);

        // Acumular los intereses + multas generados por el cliente
        total_ganado += intereses_generados + multa_aplicada;

        // Mostrar los resultados para este cliente
        printf("Saldo actual del cliente %d: %.2f\n", x + 1, clientes[x]);
        printf("Pago mínimo: %.2f\n", pago_minimo);
        printf("Pago para no generar intereses: %.2f\n", pago_sin_intereses);
        if (intereses_generados > 0)
        {
            printf("Intereses generados: %.2f\n", intereses_generados);
            printf("Multa aplicada: %.2f\n", multa_aplicada);
            printf("Total ganado por este cliente: %.2f\n", intereses_generados + multa_aplicada);
        }
    }

    // Mostrar el total ganado por concepto de intereses y multas
    printf("\nTotal ganado por concepto de intereses y multas de los morosos: %.2f\n", total_ganado);

    return 0;
}

// Función para calcular el saldo actual
float saldo_actual(float saldo_anterior, float monto_compras, float pago_realizado, float *pago_minimo, float *pago_sin_intereses, float *intereses_generados, float *multa_aplicada)
{
    // Calcular el saldo actual inicial
    float saldo_actual = saldo_anterior + monto_compras - pago_realizado;

    // Calcular el pago mínimo (15% del saldo actual)
    *pago_minimo = 0.15 * saldo_actual;

    // Calcular el pago para no generar intereses (85% del saldo actual)
    *pago_sin_intereses = 0.85 * saldo_actual;

    // Inicializar intereses y multa en 0
    *intereses_generados = 0;
    *multa_aplicada = 0;

    // Si el cliente no pagó al menos el mínimo, aplicar intereses y multa
    if (pago_realizado < *pago_minimo)
    {
        *intereses_generados = 0.12 * saldo_actual; // Intereses del 12%
        *multa_aplicada = 200;                     // Multa fija
        saldo_actual += *intereses_generados + *multa_aplicada; // Ajustar saldo con intereses y multa
    }

    return saldo_actual;
}
