package problema3;

//Diseñe un programa que haga un conteo de los dígitos pares e impares de un
//número entero positivo ingresado por el usuario. Imprima la cantidad de
//dígitos impares y la cantidad de dígitos pares.


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int num=0,temp=0,cantPar=0,cantImpar=0;

        while (true){
            try {
                do {
                    System.out.printf("\nIngrese un número entero positivo: ");
                    num = Integer.parseInt(reader.readLine());

                    if (num <= 0){
                        System.err.println("Error: el número debe ser positivo");
                    }

                }while (num <= 0);
            }

            catch (NumberFormatException e){
                System.err.println("Error: " + e.getMessage());
                continue;
            }

            catch (IOException e){
                System.err.println("Error: " + e.getMessage());
                continue;
            }

            temp=num;
            while (temp%10 != 0){
                if (temp%2 == 0){
                    cantPar++;
                }else cantImpar++;
                temp/=10;
            }

            System.out.println("Cantidad de dígitos pares: " + cantPar);
            System.out.println("Cantidad de dígitos impares: " + cantImpar);


            break;
        }
    }
}