import problema1.*;
import problema2.*;
import problema3.Problema3;
import problema4.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//Grupo:
//Aaron Remarchuk   8-1042-134
//Luis King         8-1017-548
//Edwin Rodriguez   8-975-208
//Kevin Kakiyama    8-1025-1743

public class Main {
    public static void main(String[] args) {
        int opcion = 0;
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            try {
                System.out.printf("\n\tMenú\n");
                System.out.println("1- Problema 1");
                System.out.println("2- Problema 2");
                System.out.println("3- Problema 3");
                System.out.println("4- Problema 4");
                System.out.println("Cualquier otro número para salir");
                System.out.print("Ingrese una opción: ");
                opcion = Integer.parseInt(reader.readLine());

                switch (opcion) {
                    case 1: {
                        System.out.print("Ingrese número de filas: ");
                        int n = Integer.parseInt(reader.readLine());
                        System.out.print("Ingrese número de columnas: ");
                        int m = Integer.parseInt(reader.readLine());
                        Problema1 matriz = new Problema1(n, m);

                        matriz.datosMatriz(reader);
                        System.out.println();
                        matriz.imprimirMatriz();

                        continue;
                    }
                    case 2: {
                        System.out.print("Ingrese número de filas: ");
                        int n = Integer.parseInt(reader.readLine());
                        System.out.print("Ingrese número de columnas: ");
                        int m = Integer.parseInt(reader.readLine());
                        Problema2 matriz = new Problema2(n, m);

                        matriz.datosMatriz(reader);
                        System.out.println();
                        matriz.imprimirMatriz();
                        continue;
                    }
                    case 3: {
                        System.out.println();
                        System.out.println("\tProblema 3");
                        Problema3.ejecutar();
                        continue;
                    }
                    case 4: {
                        try {
                            System.out.print("Ingrese la cantidad de estudiantes: ");
                            int cantidad = Integer.parseInt(reader.readLine());
                            Problema4 problema = new Problema4(cantidad);
                            problema.ejecutarMenu(reader);
                        } catch (NumberFormatException | IOException e) {
                            System.err.println("Entrada inválida. " + e.getMessage());
                        }
                        continue;
                    }
                    default: {
                        break;
                    }
                }
                break;
            } catch (NumberFormatException e) {
                System.err.println("Error, ingrese un digito: " + e.getMessage());
            } catch (RuntimeException e) {
                System.err.println("Error: " + e.getMessage());
            } catch (IOException e) {
                System.err.println("Error: " + e.getMessage());
            } finally {
                System.out.println();
                System.out.println("...Volviendo al menú");
                System.out.println();
            }
        }
        System.out.println("...Cerrando el programa");
    }
}
