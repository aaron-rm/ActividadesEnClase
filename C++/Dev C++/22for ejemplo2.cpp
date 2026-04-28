/*imprimir del 1 al 30 y cada 7 numeros hacer un salto de linea*/

#include<stdio.h>

main(){
	int num;
	for (num=1;num<=30;num++){
		printf("%d\t",num);
		if(num%7==0){
			printf("\n");
		}
	}
}
