package problema3;
// Haga un programa que lea una matriz cuadrada de K elementos enteros y construya una
//función genere un vector con los elementos de la diagonal secundaria ordenados de
//mayor a menor.

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Problema3 {
    public static void ejecutar() {
        try {
            BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("Ingrese el tamaño de la matriz cuadrada (K): ");
            int tamañoMatriz = Integer.parseInt(scan.readLine());

            if (tamañoMatriz <= 0) {
                System.out.println("El tamaño debe ser mayor a cero.");
                return;
            }

            Matriz matrizIngresada = new Matriz(tamañoMatriz);
            matrizIngresada.leerElem(scan);
            matrizIngresada.imprimirMatriz();
            int[] diagonalSecundaria = matrizIngresada.obtenerDiagonalSecundaria();

            OrdenMatriz.ordenarDescendente(diagonalSecundaria);

            System.out.println("Diagonal secundaria ordenada de mayor a menor:");
            for (int elemento : diagonalSecundaria) {
                System.out.print(elemento + " ");
            }
            System.out.println();

        } catch (NumberFormatException e) {
            System.out.println("Error: Debe ingresar un número entero válido.");
        } catch (IOException e) {
            System.out.println("Error al leer los datos.");
        } catch (Exception e) {
            System.out.println("Ocurrió un error inesperado: " + e.getMessage());
        }
    }
}
