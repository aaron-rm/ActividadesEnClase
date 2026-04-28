#include<stdio.h>
#include<locale>

main(){
	setlocale(LC_ALL, "");
	float sueldo;
	printf("Ingrese su sueldo: ");
	scanf("%f", &sueldo);
	if(sueldo<1000){
		sueldo=sueldo+(sueldo*0.45); 
	}
	else{
		sueldo=sueldo-(sueldo*0.10);
	}
	printf("Su sueldo final es de: %f", sueldo);
}
