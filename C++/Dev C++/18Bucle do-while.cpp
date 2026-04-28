
/* a diferencia de while, do-while realiza las acciones y luego evalua la condicion*/

#include <stdio.h>
#include <locale.h>

main(){
    setlocale(LC_ALL, "");
    char seleccion;
    do{
		printf("1.- Comenzar \n");	
		printf("2.- Abrir \n");
		printf("3.- Grabar \n");
		printf("4.- Salir \n");
		printf("Escoge una opción: \n");
		seleccion=getchar();
		switch(seleccion){
			case '1': printf("Opción 1 \n");
				break;
			case '2':printf("Opción 2 \n");
				break;
			case '3':printf("Opción 3 \n");
				break;
		}
	}while(seleccion!='4');
}
