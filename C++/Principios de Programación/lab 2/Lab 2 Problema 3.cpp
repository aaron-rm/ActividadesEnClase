#include<stdio.h>

main(){

	float a; 
	printf("Ingrese un angulo en grados centesimales: "); 
	scanf("%f", &a); 
	if(a<90){ 
		if(a>0){
			printf("Su angulo es agudo.");
		}
	} 

	else{
		if (a==90){ 
		printf("Su angulo es recto."); 
		}
		else{
			if (a<180){ 
			printf("Su angulo es obtuso."); 
			}
		} 
	}
}
