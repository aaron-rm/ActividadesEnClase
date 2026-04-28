#include<stdio.h>
#include<locale.h>

//pedir N, calcular el factorial de 1 hasta N = N!
main(){
	setlocale(LC_ALL,"");
	int num,x,factorial;
	printf("Inserte un número entero, para calcular su factorial: ");
	scanf("%d", &num);
		for(x=1;x<=num;x++){
			factorial*=x;
			printf("%d! = %d\n",x,factorial); 
		}
}




