#include<stdio.h>
#include<locale.h>

main(){
	setlocale(LC_ALL, "");
	int calif=0;
	do{
		printf("Inserte una calificación:\n");
		scanf("%d", &calif);
	}while(calif<0 || calif>10);
	printf("\nGracias");
}
