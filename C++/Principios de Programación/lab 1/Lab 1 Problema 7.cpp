#include<stdio.h>

main(){
	float ft; 
	printf("Coloque una longitud en pies: ");	 
	scanf("%f", &ft); 
	float ft_yd=ft/3; 
	float ft_pg=ft*12; 
	float ft_cm=ft*30.48; 
	float ft_m=ft*0.3048; 
	printf("Su longitud en yardas es de: %f\n", ft_yd); 
	printf("Su longitud en pulgadas es de: %f\n", ft_pg); 
	printf("Su longitud en centimetros es de: %f\n", ft_cm);
	printf("Su longitud en pies en metros es de: %f\n", ft_m);
}