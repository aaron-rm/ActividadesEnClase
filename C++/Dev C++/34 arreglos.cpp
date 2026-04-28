#include<stdio.h>

//vector o arreglo
//cada valor del vector, se le llama indice
//vector es un arreglo unidimensional, matriz es un arreglo bidimensional

main(){
	int vector[10],i;
	for (i=0;i<10;i++) vector[i]=i;
	for (i=0;i<10;i++) printf(" %d",vector[i]);
}
