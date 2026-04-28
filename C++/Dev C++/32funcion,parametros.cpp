#include <stdio.h>

int suma(int,int); 

int suma(int a,int b){
	return (a+b);
}

main(){
	int a=10,b=25,t;
	t=suma(a,b);
	printf("%d=%d",suma(a,b),t);
	suma(a,b);
}



