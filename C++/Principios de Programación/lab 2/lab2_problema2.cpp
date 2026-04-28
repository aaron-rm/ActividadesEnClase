// 2. Leer un número entero mostrar un mensaje si es que este es impar. 
#include <stdio.h>
#include <locale.h>

main()
{
	setlocale(LC_ALL,"");
	int num;
	printf("Digite un número: ");
	scanf("%d",&num);
	if(num%2!=0)
		printf("El número %d es impar.",num);
}
