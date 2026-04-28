//Escribir un algoritmo que realice la conversion de pulgadas a centimetros utilizando una funcion.
// 1 pulgada = 2.54 cm

#include<stdio.h>
#include<locale.h>

float conversion(float); //declarar la funcion
//tipo del resultado  	tipo de las variables que se van a usar
float conversion(float x){
	//pulgadas a cm
	return(x*2.54);    //resultado de la funcion
}

main(){
	setlocale(LC_ALL,"");
	float a;
	printf("Ingrese las pulgadas: ");
	scanf("%f",&a);
	printf("Conversión: %f cm", conversion(a)); //realiza la funcion, en lugar de una operacion
}
