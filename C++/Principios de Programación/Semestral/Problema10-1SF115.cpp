/*
1SF115
Joseph Alvarez
Helen Bolanos
Jaziel Gonzalez
Dilam Jimenez
Aaron Remarchuk
*/

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <locale.h>
#include <ctype.h>


void Bienvenida(void);

float Calcular_imc(float,float);
const char* Analizar_imc(float);

const char* Analizar_tensionArterial(int);

const char* Analizar_colesterol_total(int,int,int);
const char* Analizar_colesterol_HDL(int,int,int);
const char* Analizar_colesterol_LDL(int,int,int);

float Calcular_imc(float estatura, float peso)
{
	float imc;
	imc = peso / (pow(estatura,2));
	return imc;
}

const char* Analizar_imc(float imc)
{
	if(imc>32) //Se hace el rango para un adulto mayor.
	{
		return "Obesidad";
	} else if(imc>=28){
		return "Sobrepeso";
	} else if(imc>=23){
		return "Normal";
	} else{
		return "Bajo peso";
	}
}

const char* Analizar_tensionArterial(int sistolica, int diastolica)
{
	if(sistolica>180&&diastolica>120)
	{
		return "Crítico: Demasiado alta.\nSu presión arterial está extremadamente alta. Requiere atención médica de inmediato.";
	} else if(sistolica>=140&&diastolica>=90){
		return "Muy alta.\nPresenta hipertensión etapa 2.\nSu presión arterial está alta y podría afectar su salud si no se controla. Esto necesita tratamiento activo y seguimiento cercano.";
	} else if(sistolica>=130&&diastolica>80){
		return "Alta.\nPresenta hipertensión etapa 1.\nSu presión está en un nivel que podría aumentar el riesgo de problemas cardíacos a largo plazo. Este es un buen momento para tomar medidas como mejorar su dieta, hacer más ejercicio y, si es necesario, considerar tratamiento médico.";
	} else if(sistolica>=120 && diastolica<=80){
		return "Elevada.\nSu presión está un poco más alta de lo ideal. Esto no es alarmante, pero podría ser una señal de que necesita ajustar hábitos como el consumo de sal, ejercicio o manejo del estrés.";
	} else if (sistolica>=90 && diastolica >=60){
		return "Normal.\nExcelente! Su presión arterial está en un rango saludable. Mantenga este equilibrio con un estilo de vida activo, una dieta equilibrada y chequeos regulares para cuidar de su bienestar.";
	} else if(sistolica>=70 && diastolica>=40){
		return "Baja (hipotensión).\nSu presión está por debajo de lo normal. Aunque no siempre es un problema grave, puede causar síntomas como mareos o debilidad. Le recomendamos un chequeo para identificar la causa y asegurarnos de que esté bien cuidado.";
	} else if (sistolica < 70 && diastolica < 40){
		return "Muy baja (crítica).\nSu presión arterial está peligrosamente baja. Requiere atención médica de inmediato.";
	}
}

const char* Analizar_colesterol_total(int colesterol)
{
	//Colesterol
	if(colesterol>=240)
	{
		return "Muy alto.\nSu colesterol total está demasiado alto, lo que puede aumentar el riesgo de problemas cardíacos. Le sugerimos hacer un plan conjunto para reducirlo, que podría incluir cambios en su dieta, actividad física y, si es necesario, medicamentos.";
	}else if(colesterol>=200){
		return "Alto.\nSu colesterol total está un poco elevado. Esto podría ser una señal para ajustar algunos hábitos, como reducir grasas saturadas y aumentar la actividad física. Un pequeño esfuerzo ahora puede hacer una gran diferencia en su salud.";
	}else if(colesterol>=125){
		return "Normal.\nExcelente! Su colesterol total está en un rango saludable. Mantenga este nivel con una dieta balanceada, ejercicio regular y chequeos periódicos.";
	}else{
		return "Bajo.\nSu colesterol total está bajo. Se recomienda buscar la opinión de un médico.";
	}
	
}

const char* Analizar_colesterol_HDL(int HDL, char sexo)
{
	//HDL
	if(sexo=='M')
	{
		if(HDL>=40)
		{
			return "Normal.\nBuen trabajo! Su colesterol HDL está en un nivel protector para su corazón. Manténgalo así con actividad física y buena alimentación.";
		}else "Bajo.\nSu colesterol bueno (HDL) está bajo. Esto puede aumentar el riesgo cardiovascular. Incorporar ejercicio aeróbico y grasas saludables en su dieta puede ayudar a subirlo.";
	}else if(sexo=='F')
	{
		if(HDL>=50)
		{
			return"Normal.\nBuen trabajo! Su colesterol HDL está en un nivel protector para su corazón. Manténgalo así con actividad física y buena alimentación.";
		}else{
			return "Bajo\nSu colesterol bueno (HDL) está bajo. Esto puede aumentar el riesgo cardiovascular. Incorporar ejercicio aeróbico y grasas saludables en su dieta puede ayudar a subirlo.";
		}
	}
}

const char* Analizar_colesterol_LDL(int LDL)
{
	//LDL
	if(LDL>=160)
	{
		return "Muy elevado.\nSu colesterol LDL está demasiado alto. Esto requiere atención para evitar complicaciones futuras. Trabajemos juntos en un plan personalizado que podría incluir cambios en su dieta, ejercicio y medicamentos";
	}else if(LDL>=130){
		return "Elevado.\nSu colesterol LDL está algo elevado, lo que podría aumentar el riesgo de problemas a largo plazo. Reducir alimentos procesados y aumentar fibra puede ser un gran primer paso.";
	}else if(LDL>=100){
		return "Casi ideal.\nSu colesterol LDL está dentro de un rango aceptable, pero podría mejorar un poco más. Considere algunos ajustes simples, como reducir las grasas saturadas y trans en su dieta.";
	}else{
		return "Normal.\nFelicidades! Su colesterol LDL está en un rango ideal, lo que ayuda a proteger sus arterias. Mantenga su estilo de vida saludable para conservar este nivel.";
	}
}


main()
{
	setlocale(LC_ALL,"");
	
	/*### Bienvenida ###*/
	Bienvenida();
	
	/*---- INICIO ----*/
	int opcion,iniciar;
	
	printf("Desea iniciar? \n1:si\n0:no\n");
	printf(">>>");
	scanf("%d",&iniciar);
	printf("--------------------------\n\n");
	while(iniciar)
	{
		printf("Escoga que examen analizaremos:\n\t1: IMC\n\t2: Tensión arterial\n\t3: Nivel de colesterol.\nDigite el número para ejecutar.\n");
		printf("Opción: ");
		scanf("%d",&opcion);
		switch(opcion)
		{
			case 1:
				/*### IMC ###*/
				float estatura,peso,imc;
				
				do{
					printf("Digite su estatura (en metros): ");
					scanf("%f",&estatura);
					if(estatura<0||estatura>3.00)
					{
						printf("ERROR: Valor Invalido. Digite de nuevo.\n\n");
					}
				} while(estatura<0||estatura>3.00);
				
				do{
					printf("Digite su peso (en Kg): ");
					scanf("%f",&peso);
					if(peso<0||peso>300)
					{
						printf("ERROR: Valor Invalido. Digite de nuevo.\n\n");
					}
				} while(peso<0||peso>300);
				
				imc = Calcular_imc(estatura,peso); //imc: indice masa corporal
				
				//Resultados IMC
				printf("\nPara los datos ingresados\n");
				printf("\tEstatura (m): %.2f metro(s)\n",estatura);
				printf("\tPeso (Kg): %.2f kilogramo(s)\n\n",peso);
				printf("\tSu IMC es %.1f, lo que indica que su peso está en la categoría de %s para adultos mayores de su estatura. ",imc,Analizar_imc(imc));
				break;
			case 2:
				//### Tension Arterial ###//
				int p_sistolica,p_diastolica;
				do{
					printf("Digite su presión sistólica: ");
					scanf("%d",&p_sistolica);
			
					printf("Digite su presión diastólica: ");
					scanf("%d",&p_diastolica);
					
					if(p_sistolica <=0 || p_diastolica<=0 || p_sistolica<p_diastolica || (p_sistolica-p_diastolica)>60 || (p_sistolica-p_diastolica)<0)
					{
						printf("Error: Sus valores son irreales. Corrija las mediciones y vuelva a digitarlas.\n\n");
					}	
				} while(p_sistolica <=0 || p_diastolica<=0 || p_sistolica<p_diastolica || (p_sistolica-p_diastolica)>60 || (p_sistolica-p_diastolica)<0);
				
				//Resumen
				printf("\nSu presión arterial es: %d/%d.\n",p_sistolica,p_diastolica);
				printf("Entra en la categoría de: %s",Analizar_tensionArterial(p_sistolica,p_diastolica));
				break;
			case 3:
				/*### COLESTEROL ###*/
				int colesterol, HDL, LDL; //HDL: colesterol bueno (alta densidad lopoproteína) y LDL: colesterol malo (baja densidad loporproteína)
				char sexo;
				
				do{
					printf("Sexo (M o F): ");
					scanf(" %c", &sexo);
				}while(sexo!='F'&&sexo!='M');
				
				do{
					printf("Digite el colesterol: ");
					scanf("%d",&colesterol);
					
					printf("Digite el HDL: ");
					scanf("%d",&HDL);
					
					printf("Digite el LDL: ");
					scanf("%d",&LDL);
					
				}while(colesterol<0 || HDL<0 || LDL<0);
				
				printf("Sus resultados arrojan:\n\tColesterol total: %d\n\tHDL: %d\n\tLDL:%d\n",colesterol,HDL,LDL);
				printf("Colesterol total:\nEntra en la categoría de: %s\n\n",Analizar_colesterol_total(colesterol));
				printf("Colesterol HDL:\nSe conoce como \"Colesterol bueno\".\n\nUsted entra en la categoría de: %s\n\n",Analizar_colesterol_HDL(HDL,sexo));
				printf("Colesterol LDL:\nSe conoce como \"Colesterol malo\".\nUsted entra en la categoría de: %s",Analizar_colesterol_LDL(LDL));
				break;
			default:
				printf("Error\n");
		}
		printf("\n-------Fin----------\n");
		printf("Desea iniciar? \n1:si\n0:no\n");
		printf(">>>");
		scanf("%d",&iniciar);
	}
	
	printf("\nGracias por preferirnos.");
} 

void Bienvenida(void)
{
	printf("Buen día.\n");
	printf("A continuación haremos un análisis de sus resultados en:\n\tIMC:Índice de Masa Corporal.\n\tTensión (o Presión) arterial.\n\tNivel de colesterol.\n");
	printf("AVISO: evitar digitar números negativos, de lo contrario deberá digitarlo nuevamente.\n");
	printf("AVISO: Esta calculadora evalúa los resultados en base a los rangos normales para un adulto mayor (mayor de 65 años según la OMS).\n");
	printf("-----------------------------------\n\n");
}
