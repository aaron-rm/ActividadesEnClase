//Problema 2: Escribir una función booleana Digito que determine si un caracter es uno de los dígitos 0 al 9.

#include <stdio.h>
#include <locale.h>
#include <stdbool.h>

bool es_digito(char); /*Prototipo*/

main(){
	setlocale(LC_ALL,"");
	char digito;
	bool comprobar_digito;
	printf("Programa comprobador de digitos.\nNota:\n\t1: Verdadero\n\t0: Falso\n");
	printf("Ingrese un caracter: ");
	digito = getchar();
	comprobar_digito = es_digito(digito);
	printf("¿Es digito?\nRespuesta: %d",comprobar_digito);
}

bool es_digito(char digito)
{
	switch(digito)
	{
		case '0':
			return true;
			break;
		case '1':
			return true;
			break;
		case '2':
			return true;
			break;
		case '3':
			return true;
			break;
		case '4':
			return true;
			break;
		case '5':
			return true;
			break;
		case '6':
			return true;
			break;
		case '7':
			return true;
			break;
		case '8':
			return true;
			break;
		case '9':
			return true;
			break;
		default:
			return false;
			break;
	}
}
