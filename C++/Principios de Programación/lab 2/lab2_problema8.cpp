// 8. Solicitar un número entero por teclado y verificar si es par o impar.  
#include <stdio.h>
#include <locale.h>

main()
{
	setlocale(LC_ALL,"");
	int num;
	printf("Digite un número: ");
	scanf("%d",&num);
	if(num%2==0)
		printf("El número %d es par",num);
	else
		printf("El número %d es impar",num);
}
