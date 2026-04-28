
#include<stdio.h>
#include <locale.h>

main(){
    setlocale(LC_ALL, "");
    float num1, num2;
	printf("Introduce el primer número: ");
	scanf("%f", &num1);
	printf("Introduce el segundo número: ");
	scanf("%f", &num2);
	if (num1>num2)
		printf("El primer número es el mayor");
	else
		if (num2>num1)
			printf ("El segundo número es el mayor");
		else
			printf("Los números son iguales");
}
