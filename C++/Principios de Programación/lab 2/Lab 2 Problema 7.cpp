#include <stdio.h>
main(){
	float num1,num2,promedio;
	printf("Ingrese dos numeros: "); 
	scanf("%f", &num1); 
	scanf("%f", &num2);
	promedio=(num1+num2)/2; 
	if(promedio>=13){
	 	printf("Aprobado."); 
		}
	else{
		printf("Desaprobado.");
		} 
}
