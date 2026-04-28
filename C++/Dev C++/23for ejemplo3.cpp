
#include<stdio.h>

main(){
	int x,mes,dias=0;
	int aa=2024;
	printf("Que mes desea: ");
	scanf("%d",&mes);
	if(mes==1||mes==3||mes==5||mes==7||mes==8||mes==10||mes==12){
		dias=31;
	}
	if(mes==4||mes==6||mes==9||mes==11){
		dias=30;
	}
	if(mes==2){
		dias=29;
	}
	for(x=1;x<=dias;x++){
		printf("%d\t",x);
		if(x%7==0){
			printf("\n");
		}
	}
}
