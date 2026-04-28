package problema4;

//Escriba un programa que valide fechas de nacimiento. El usuario las escribirá
//en el formarto dd/mm/AAAA. Determine si la fecha es válida o no. PD: No utilice
//librerías.

//Para determinar si un año es bisiesto, debes seguir estas reglas:
//Divisible por 4: Si un año es divisible por 4, generalmente es bisiesto.
//Divisible por 100: Sin embargo, si un año es divisible por 100, NO es bisiesto a menos que también sea divisible por 400.
//Divisible por 400: Si un año es divisible por 400, sí es bisiesto.

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String fecha;
        int dia,mes,anio;
        boolean continuar=true, bisiesto=false;


        while (true){
            try {
                do {
                    continuar=true;
                    System.out.printf("\nIngrese una la fecha en formato (dd/mm/AAAA): ");
                    fecha= reader.readLine();
                    if (fecha.length()!=10){
                        System.err.println("Error: ingrese el formato adecuado (dd/mm/AAAA), puede incluir '/' o '-'");
                        System.err.println("De ser necesario, poner 0 antes del dia o mes");
                        continuar = false;
                        continue;
                    }

                    anio=Integer.parseInt(fecha.substring(6,10));
                    if (anio<1 || anio>2100){
                        System.err.println("Error: ingrese un año correcto");
                        continuar = false;
                        continue;
                    }
                    if ((anio % 4 == 0) && ((anio % 100 != 0) || (anio % 400 == 0))){
                        bisiesto=true;
                    }

                    mes=Integer.parseInt(fecha.substring(3,5));
                    if (mes<1 || mes>12){
                        System.err.println("Error: ingrese un año correcto");
                        continuar = false;
                        continue;
                    }

                    dia=Integer.parseInt(fecha.substring(0,2));
                    if (dia<1){
                        System.err.println("Error: ingrese un día correcto");
                        continuar = false;
                        continue;
                    }

                    if (mes == 2){
                        if (bisiesto){
                            if (dia>29){
                                System.err.println("Error: ingrese un día correcto");
                                continuar = false;
                                continue;
                            }
                        }else if (dia>28){
                            System.err.println("Error: ingrese un día correcto");
                            continuar = false;
                            continue;
                        }
                    }

                    if (mes%2 == 0){
                        if (dia>31){
                            System.err.println("Error: ingrese un día correcto");
                            continuar = false;
                            continue;
                        }
                    }else {
                        if (dia>30){
                            System.err.println("Error: ingrese un día correcto");
                            continuar = false;
                            continue;
                        }
                    }
                }while (!continuar);
            }
            catch (NumberFormatException e){
                System.err.println("Error: ingrese una fecha válida ,error " + e.getMessage());
                continue;
            }
            catch (IOException e){
                System.err.println("Error: " + e.getMessage());
                continue;
            }
            catch (RuntimeException e){
                System.err.println("Error: " + e.getMessage());
                continue;
            }
            break;
        }
        System.out.println("Fecha exitosa");
    }

}

