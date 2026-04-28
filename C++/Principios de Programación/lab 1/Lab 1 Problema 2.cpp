#include<stdio.h>

main(){
	float r;
	printf("Coloque el radio para calcular la longitud de la circunferencia y el area del circulo: ");
	scanf("%f", &r);
	float C=2*3.1416*r;
	float A=3.1416*2*r*r;
	printf("La longitud de la circunferencia es de: %f\n", C);
	printf("El area del circulo es de: %f\n", A);
	
}
