package problema3;

import java.io.BufferedReader;
import java.io.IOException;

public class Matriz {
    private int[][] elementoMatriz;
    private int tamañoMatriz;

    public Matriz(int tamañoMatriz) {
        this.tamañoMatriz = tamañoMatriz;
        this.elementoMatriz = new int[tamañoMatriz][tamañoMatriz];
    }

    public void leerElem(BufferedReader scan) throws IOException {
        System.out.println();
        System.out.println("Ingrese los elementos de la matriz (solo numeros enteros):");
        for (int i = 0; i < tamañoMatriz; i++) {
            for (int j = 0; j < tamañoMatriz; j++) {
                System.out.print("Elemento [" + i + "][" + j + "]: ");
                elementoMatriz[i][j] = Integer.parseInt(scan.readLine());
            }
        }
    }

    public void imprimirMatriz() {
        System.out.println();
        System.out.println("Matriz ingresada:");
        for (int i = 0; i < tamañoMatriz; i++) {
            for (int j = 0; j < tamañoMatriz; j++) {
                System.out.printf("%d\t",elementoMatriz[i][j]);
            }
            System.out.println();
        }
        System.out.println();
    }

    public int[] obtenerDiagonalSecundaria() {
        int[] diagonal = new int[tamañoMatriz];
        for (int i = 0; i < tamañoMatriz; i++) {
            diagonal[i] = elementoMatriz[i][tamañoMatriz - 1 - i];
        }
        return diagonal;

    }
}
