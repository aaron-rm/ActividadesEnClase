// 1. Realizar un algoritmo para operar la suma de dos números enteros

#include <stdio.h>
#include <locale.h>

main(){
	setlocale(LC_ALL,"");
	int num1, num2, suma;
	printf("Digite un número: ");
	scanf("%d",&num1);
	printf("Digite un segundo número: ");
	scanf("%d",&num2);
	suma = num1 + num2;
	printf("La suma es: %d",suma);
}
