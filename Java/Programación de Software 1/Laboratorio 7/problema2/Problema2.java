package problema2;
// Dada una matriz entera de tamaño m x n, solicita al usuario que ingrese los elementos.
//Luego, encuentra el elemento más grande en cada fila, guárdelo en un vector y muestra
//dichos elementos.


import java.io.BufferedReader;
import java.io.IOException;

public class Problema2 {
    private int[][] matriz;
    private int[] mayor;
    private int filas,columnas;

    public Problema2(int n, int m){
        this.filas=n;
        this.columnas=m;
        this.matriz = new int[n][m];
        this.mayor = new int[n];
    }

    public void datosMatriz(BufferedReader reader){
        while (true){
            try {
                for (int i=0;i<filas;i++){
                    for (int j=0;j<columnas;j++){
                        System.out.printf("Ingrese el número en la posicion [%d][%d]: ",i,j);
                        matriz[i][j] = Integer.parseInt(reader.readLine());
                    }
                }
                break;
            }
            catch (NullPointerException e){
                System.err.println("Error: " + e.getMessage());
                continue;
            }
            catch (NumberFormatException e){
                System.err.println("Error: ingrese un dígito " + e.getMessage());
                continue;
            }
            catch (RuntimeException e){
                System.err.println("Error: " + e.getMessage());
                continue;
            }
            catch (IOException e){
                System.err.println("Error: " + e.getMessage());
                continue;
            }
        }
    }


    public void imprimirMatriz(){
        System.out.println("Matriz");
        for (int i=0;i<filas;i++){
            for (int j=0;j<columnas;j++){
                System.out.printf("%d\t", matriz[i][j]);
                if (matriz[i][j]>mayor[i]){
                    mayor[i]=matriz[i][j];
                }
            }
            System.out.printf("\tElemento más grande: %d", mayor[i]);
            System.out.println();
        }
    }
}
