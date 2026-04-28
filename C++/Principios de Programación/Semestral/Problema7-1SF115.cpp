/*
1SF115
Joseph Alvarez
Helen Bolanos
Jaziel Gonzalez
Dilam Jimenez
Aaron Remarchuk
*/

#include<stdio.h>

void pedirDatos(int num, int rep, float peso[], float altura[], char sexo[]){
	rep=1;
	while(rep==1){
		for(int i=0; i<num; i++){
			printf("\nEstudiante #%d", i+1);
			printf("\n	Sexo (M o F): ");
			scanf(" %c", &sexo[i]);
			if(sexo[i]!='M' && sexo[i]!='F'){
				printf("		Error: Ingrese un caracter valido.");
				break;
			} else {
				printf("	Altura (metros): ");
				scanf("%f", &altura[i]);
				printf("	Peso (libras): ", i+1);
				scanf("%f", &peso[i]);
				rep+=1;	
			}
		}
	}
}

int calcularDosis(int num, float dosis[], float peso[], float altura[], char sexo[]){
		for(int i=0; i<num; i++){
			if (sexo[i]=='M'){
				if(altura[i]>1.6 && peso[i]>=150){
					dosis[i]=(altura[i]*0.20)+(peso[i]*0.80);
				} else{
					dosis[i]=(altura[i]*0.30)+(peso[i]*0.70);
				} 
			} else if (sexo[i]=='F'){
				if(altura[i]>1.6 && peso[i]>=150){
						dosis[i]=(altura[i]*0.25)+(peso[i]*0.75);
					} else{
						dosis[i]=(altura[i]*0.35)+(peso[i]*0.65);
					}
			}
		}
	return dosis[num];
}

main(){
	int num, rep;
	printf("Bienvenido. A continuacion ingrese el numero de estudiantes que desea evaluar: ");
	scanf("%d", &num);
	float peso[num], altura[num], dosis[num];
	char sexo[num];
	pedirDatos(num, rep, peso, altura, sexo);
	printf("\n\n");
	calcularDosis(num, dosis, peso, altura, sexo);
	for(int i=0; i<num; i++){
		printf("La cantidad de vitaminas que debe consumir el estudiante #%d es de: %.2f gramos\n", i+1, dosis[i]);
	}
	return 0;
}