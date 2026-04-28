#include<stdio.h>
#include<locale.h>

//mostrar el numero mayor de una serie de numeros ingresados por teclado, salir del bucle al intgresar un numero negativo
main(){
	setlocale(LC_ALL,"");
	int num,a=0,mayor;
	printf("Para salir del bucle, inserte un número negativo\n");
	while(num>=0){
		printf("Ingrese un número: ");
		scanf("%d",&num);
		if(num>a){
			mayor=num;
		}
		a=num;
	}
	printf("El número mayor es: %d",mayor);
}
