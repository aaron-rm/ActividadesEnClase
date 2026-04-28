#include <stdio.h>

main(){
	int numero=1;
	while (numero<=100){
		if (numero==25){ 
			numero=numero+5;
			/*Cuando el numero llega a 25, suma 5 en vez de 1*/
			continue;
			/*Luego de realizar el if, continua en el while*/
		}	
		printf("%d\n", numero);
		numero++;
	}
}
