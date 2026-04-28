
#include<stdio.h>
#include<locale.h>

main(){
    setlocale(LC_ALL, "");
	int num;
	printf("Introduce un número: ");
	scanf("%d", &num);
	printf("El doble del número es: %d\n", 2*num);
	printf("El triple del número es: %d", 3*num);
}
