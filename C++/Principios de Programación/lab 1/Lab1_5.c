#include <stdio.h>

int main() {
    // Declaración de variables
    double masa, energia;
    const double c = 2.997925e10; // Velocidad de la luz en cm/seg

    // Leer la masa en gramos
    printf("Ingresa la masa en gramos: ");
    scanf("%lf", &masa);

    // Convertir la masa en gramos a energía en ergios
    // E = mc^2
    energia = masa * c * c;

    // Mostrar el resultado
    printf("La energia producida es: %.2e ergios\n", energia);

    return 0;
}
