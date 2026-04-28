#include <stdio.h>

void funcion(void);
int num=5;
main(){
	int num=10;
	printf("%d\n",num);
	funcion();
}

void funcion(void){
	printf("%d\n",num);
}
