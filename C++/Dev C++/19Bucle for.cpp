
#include <stdio.h>
#include <locale.h>

main(){
	setlocale(LC_ALL,"");
	int num,x,result;
	printf("Introduce un número: ");
	scanf("%d", &num);
	for (x=0;x<=10;x++){
/*primero se inicializa la variable, se define el rango o el tope, se define el incremento o decremento*/
		result=num*x;
		printf("\n%d por %d = %d\n", num,x,result);
			}
}
