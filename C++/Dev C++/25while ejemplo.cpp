#include "stdio.h"

main(){
	int saldo=0, deposito=0, retiro=0, opcion=0;
	printf("Introduzca saldo inicial: ");
	scanf("%d", &saldo);
	while(opcion != 5){
    	printf("===Bienvenido al banco===\n");
    	printf("\nElija una opcion");
    	printf("\n1. Depositar");
    	printf("\n2. Retirar");
    	printf("\n3. Ver saldo");
    	printf("\n4. Abonar intereses");
    	printf("\n5. Salir");
    	printf("Su opcion: ");
    	scanf("%d", &opcion);
    if (opcion == 1){
    	printf("Monto a depositar: ");
        scanf("%d", &deposito);
        saldo = saldo + deposito;
    }
    if (opcion == 3){
    	printf("\nSu saldo es: %d", saldo);
    }
    if (opcion == 5){
        printf("\nGracias por usar este programa");
    }
  }
}
