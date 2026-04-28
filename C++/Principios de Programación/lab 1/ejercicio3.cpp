#include <stdio.h>

int main() {
    float base, altura, superficie;

    // Solicitar la base y la altura al usuario
    printf("Ingrese la base del triángulo: ");
    scanf("%f", &base);
    
    printf("Ingrese la altura del triángulo: ");
    scanf("%f", &altura);

    // Calcular la superficie
    superficie = (base * altura) / 2;

    // Mostrar la superficie
    printf("La superficie del triángulo es: %.2f\n", superficie);

    return 0;
}

