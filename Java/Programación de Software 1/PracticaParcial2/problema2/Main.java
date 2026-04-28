package problema2;

//Solicite al usuario registrar las temperaturas diarias durante N días. Solicite al
//inicio la cantidad de días.
    //o Por cada día, pedir la temperatura.
    //o Validar que la temperatura sea entre -50°C y 60°C (si no, solicitar
    //nuevamente).
//Al finalizar, mostrar:
    //o Temperatura máxima
    //o Temperatura mínima
    //o Temperatura promedio

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {


    public static void main(String[] args) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int dias=0;
        double temperatura=0, tempMax=-51,tempMin=60,tempProm=0;

        while (true){
            try {
                do {
                    System.out.print("Ingrese la cantidad de días: ");
                    dias = Integer.parseInt(reader.readLine());
                }while (validarDias(dias));

                for (int i=1;i<=dias;i++){
                    do {
                        System.out.printf("\nIngrese la temperatura del día %d: ",i);
                        temperatura = Double.parseDouble(reader.readLine());
                    }while (validarTemperatura(temperatura));

                    if (temperatura>tempMax){
                        tempMax=temperatura;
                    }
                    if (temperatura<tempMin){
                        tempMin=temperatura;
                    }
                    tempProm+=temperatura/dias;
                }

                break;
            }
            catch (NumberFormatException e){
                System.err.println("Error: " + e.getMessage());
                System.out.println();
                continue;
            }
            catch (RuntimeException e){
                System.err.println("Error: " + e.getMessage());
                System.out.println();
                continue;
            }
            catch (IOException e){
                System.err.println("Error: " + e.getMessage());
                System.out.println();
                continue;
            }
        }
        System.out.println("Temperatura máxima = " + tempMax + "°C");
        System.out.println("Temperatura mínima = " + tempMin + "°C");
        System.out.println("Temperatura promedio = " + tempProm + "°C");




    }

    static boolean validarDias(int n){
        //verdadero para repetir, falso para seguir
        if (n<=0){
            System.out.println();
            System.err.println("Error: ingrese un día válido");
            return true;
        }else return false;
    }

    static boolean validarTemperatura(double t){
        if (t<-50 || t>60){
            System.err.println("Error: ingrese una temperatura válida");
            return true;
        }else return false;
    }

}
