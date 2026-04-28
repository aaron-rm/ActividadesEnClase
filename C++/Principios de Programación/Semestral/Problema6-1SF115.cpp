/*
1SF115
Joseph Alvarez
Helen Bolanos
Jaziel Gonzalez
Dilam Jimenez
Aaron Remarchuk
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>
char names[5][20];
int hrs[30], horasSemanales[5];
float sueldoHora[5], sueldoSemanal[5], dineroTotal = 0.0f;
void pedirDatosTrabajador(int i) {
    while (1) {
        printf("	* Nombre del trabajador #%d (al menos 3 letras): ", i + 1);
        if (scanf("%s", names[i]) != 1) {
            printf("		Error: Entrada invalida.\n");
            while (getchar() != '\n');
            continue;
        }
        int valido = 1;
        if (strlen(names[i]) < 3) {
            printf("		Error: El nombre debe tener al menos 3 letras.\n");
            valido = 0;
        } else {
            for (int j = 0; j < strlen(names[i]); j++) {
                if (!isalpha(names[i][j])) {
                    printf("		Error: El nombre solo puede contener letras.\n");
                    valido = 0;
                    break;
                }
            }
        }
        if (valido) {
            break;
        }
	}
    horasSemanales[i] = 0;
    printf("\n	* Horas trabajadas:\n");
    for (int j = 0; j < 6; j++) {
        while (1) {
            printf("		Horas trabajadas de %s en el dia #%d de la semana: ", names[i], j + 1);
            if (scanf("%d", &hrs[i * 6 + j]) != 1) {
                printf("			Error: Entrada invalida.\n");
                while (getchar() != '\n');
                continue;
            }
            if (hrs[i * 6 + j] < 0) {
                printf("			Error: Las horas no pueden ser negativas.\n");
            } else {
                break;
            }
        }
        horasSemanales[i] += hrs[i * 6 + j];
    }
    while (1) {
        printf("\n	* Sueldo en dolares por hora de %s: ", names[i]);
        if (scanf("%f", &sueldoHora[i]) != 1) {
            printf("		Error: Entrada invalida.");
            while (getchar() != '\n');
            continue;
        }
        if (sueldoHora[i] < 0) {
            printf("		Error: El sueldo no puede ser negativo.");
        } else {
            break;
        }
    }
    sueldoSemanal[i] = sueldoHora[i] * horasSemanales[i];
    printf("\n");
}
int trabajadorMasHorasLunes() {
    int maxHoras = hrs[0], indiceMax = 0;
    for (int i = 1; i < 5; i++) {
        if (hrs[i * 6] > maxHoras) {
            maxHoras = hrs[i * 6];
            indiceMax = i;
        }
    }
    return indiceMax;
}
float calcularDineroTotal() {
    float total = 0.0f;
    for (int i = 0; i < 5; i++) {
        total += sueldoSemanal[i];
    }
    return total;
}
int main() {
    printf("Bienvenido al sistema de la compania de transporte.\n\n-------------------------------------------------\n\nA continuacion ingrese la informacion solicitada para evaluar a cinco trabajadores:\n\n");
    for (int i = 0; i < 5; i++) {
    	printf("- Trabajador #%d:\n", i+1);
        pedirDatosTrabajador(i);
    }
    int indiceMaxHoras = trabajadorMasHorasLunes();
    printf("\n\n-------------------------------\n\n");
    printf("\nInforme\n");
    for (int i = 0; i < 5; i++) {
        printf("\nNombre: %s\n	Horas trabajadas: %d\n	Sueldo semanal: %.2f\n", names[i], horasSemanales[i], sueldoSemanal[i]);
    }
    dineroTotal = calcularDineroTotal();
    printf("\nTotal a pagar: $%.2f\n", dineroTotal);
    printf("El trabajador que hizo mas horas el lunes fue: %s con %d horas.\n", names[indiceMaxHoras], hrs[indiceMaxHoras * 6]);
    return 0;
}