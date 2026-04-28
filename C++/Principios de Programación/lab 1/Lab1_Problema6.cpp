#include <stdio.h>
#include <locale.h>
#include <math.h> //para usar la función potencia
#define CONST_GRAVEDAD 6.673e-8

main(){
	setlocale(LC_ALL,"");
	float masa1,masa2,distancia,fuerza;
	printf("Digite la primera masa (gramos): ");
	scanf("%f",&masa1);
	printf("Digite la segunda masa (gramos): ");
	scanf("%f",&masa2);
	printf("Digite la distancia (centímetros): ");
	scanf("%f",&distancia);
	fuerza =  (CONST_GRAVEDAD*masa1*masa2)/(distancia*distancia);
	printf("%f\n%f\n%f\n",masa1,masa2,distancia);
	printf("La fuerza gravitacional es: %.4e dinas",fuerza);
}
