//Realizar un programa que obtenga la división entera y el resto de la misma utilizando únicamente los operadores suma y resta.

#include<stdio.h>
#include<locale.h>

//Función para calcular la división entera
int div(int divisor, int dividendo, int cociente){
	cociente=0;
	
	if(divisor<0 && dividendo<0){ //en caso el divisor y el dividendo sean <0
		dividendo=-(dividendo);
		divisor=-(divisor);
		while(dividendo>=divisor){
			cociente++;
			dividendo-=divisor;
		}
	return(cociente);
	}
	
	if(dividendo<0){ //en caso el dividendo sea <0
		dividendo=-(dividendo);
		while(dividendo>=divisor){
			cociente++;
			dividendo-=divisor;
		}
	return(-cociente);
	
	}else if(divisor<0){ //en caso el divisor sea <0
		divisor=-(divisor);
		while(dividendo>=divisor){
			cociente++;
			dividendo-=divisor;
		}
		return(-cociente);
	}
	
	while(dividendo>=divisor){ //en caso el divisor y el dividendo sean >0
		cociente++;
		dividendo-=divisor;
	}
	return(cociente);
}

//Función para calcular el residuo
int res(int divisor, int dividendo, int residuo){
	residuo=dividendo;
	
	if(dividendo<=divisor){
		if(divisor<0 && dividendo<0){ //en caso el divisor y el dividendo sean <0
			dividendo=-(dividendo);
			divisor=-(divisor);
			while(dividendo>=divisor){
				dividendo-=divisor;
				residuo=dividendo;
			}
			return(-residuo);
		}
		else if(dividendo<0){ //en caso el dividendo sea <0
			dividendo=-(dividendo);
			if(dividendo<divisor){
				residuo=dividendo;
				return(-residuo);
			}
			while(dividendo>=divisor){
				dividendo-=divisor;
				residuo=dividendo;
			}				
			return(-residuo);
		}
		return(residuo);
	}

	if(divisor<0){ //en caso el dividendo sea <0
		divisor=-(divisor);
		while(dividendo>=divisor){
			dividendo-=divisor;
			residuo=dividendo;
		}
		return(residuo);
		}
		while(dividendo>=divisor){
			dividendo-=divisor;
			residuo=dividendo;
		}
		return(residuo);
}

main(){
	int dividendo, divisor, cociente, residuo;
	setlocale(LC_ALL,"");
	printf("Introduzca el dividendo: ");
	scanf("%d", &dividendo);
	do{
		printf("Introduzca el divisor: ");
		scanf("%d", &divisor);
	}while(divisor==0); //Para evitar que el divisor sea 0
	printf("%d entre %d = %d\n", dividendo, divisor, div(divisor,dividendo,cociente));
	printf("Y el residuo es = %d", res(divisor,dividendo,residuo));
}
