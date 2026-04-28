//Diseñar un algoritmo que transforme un número introducido por teclado en notación decimal a notación romana. El número será entero positivo y no excederá de 3.000.
#include<stdio.h>
int i=1;
void error() {
    printf("Error: El numero debe ser un entero positivo y no debe exceder de 3000.\n");
}
void decimal_a_romano(int numero) {
    while (numero >= 1000) {
        printf("M");
        numero -= 1000;
    }
    if (numero >= 900) {
        printf("CM");
        numero -= 900;
    } else if (numero >= 500) {
        printf("D");
        numero -= 500;
    } else if (numero >= 400) {
        printf("CD");
        numero -= 400;
    }
    while (numero >= 100) {
        printf("C");
        numero -= 100;
    }
    if (numero >= 90) {
        printf("XC");
        numero -= 90;
    } else if (numero >= 50) {
        printf("L");
        numero -= 50;
    } else if (numero >= 40) {
        printf("XL");
        numero -= 40;
    }
    while (numero >= 10) {
        printf("X");
        numero -= 10;
    }
    if (numero == 9) {
        printf("IX");
        numero -= 9;
    } else if (numero >= 5) {
        printf("V");
        numero -= 5;
    } else if (numero == 4) {
        printf("IV");
        numero -= 4;
    }
    while (numero >= 1) {
        printf("I");
        numero -= 1;
    }
}
int main() {
    int numero;
    do{
    	printf("\nIntroduce un numero entero positivo (menor o igual a 3000): ");
		scanf("%d", &numero);
		if(numero<=0||numero>3000) {
        	error();
        } 
	}while(numero<=0||numero>3000);
		if(numero>=0||numero<3000) {
        	printf("El numero en notacion romana es: ");
        	decimal_a_romano(numero);
        	printf("\n");
    }
}