#include <stdio.h>
//uso de operaciones aritmeticas basicas

main()
{
	int a=1,b=2,c=3,r;
	r=a+b;
	printf("%d + %d = %d\n",a,b,r);
	r=c-a;
	printf("%d - %d = %d\n",c,a,r);
	b++;
	//++ suma 1 unidad a la variable
	printf("b + 1 = %d",b);
}
