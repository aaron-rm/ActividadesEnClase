
#include<stdio.h>
#include <locale.h>

main(){
    setlocale(LC_ALL, "");
    int num1, num2;
	printf("Introduce el primer número: ");
	scanf("%d", &num1);
	printf("Introduce el segundo número: ");
	scanf("%d", &num2);
	if (num1<num2)
		printf("El número menor es: %d", num1);
	else
		if (num2<num1)
			printf ("El número menor es: %d", num2);
		else
			printf("Los números son iguales");
    
}
