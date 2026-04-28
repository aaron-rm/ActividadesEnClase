#include <stdio.h>

int main() {
    // Declaración de variables para almacenar los tres números y el promedio
    float num1, num2, num3, promedio;

    // Solicitar al usuario que ingrese tres números decimales
    printf("Ingresa el primer nUmero: ");
    scanf("%f", &num1);

    printf("Ingresa el segundo nUmero: ");
    scanf("%f", &num2);

    printf("Ingresa el tercer nUmero: ");
    scanf("%f", &num3);

    // Calcular el promedio
    promedio = (num1 + num2 + num3) / 3;

    // Mostrar el promedio
    printf("El promedio es: %.2f\n", promedio);

    // Verificar si el promedio es mayor o igual a 2
    if (promedio >= 2) {
        printf("Nota aprobatoria\n");
    }

    return 0;
}
