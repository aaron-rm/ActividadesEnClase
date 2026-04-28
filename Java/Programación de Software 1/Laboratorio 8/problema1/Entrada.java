package Lab8.problema1;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Entrada {
    public static String leerPalabra() {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String palabra = "";

        try {
            System.out.print("Ingrese una palabra (solo letras): ");
            palabra = br.readLine();
            if (!palabra.matches("[a-zA-Z]+")) {
                throw new IllegalArgumentException("La palabra debe contener solo letras.");
            }
        } catch (IOException e) {
            System.out.println("Error al leer la entrada: " + e.getMessage());
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }

        return palabra;
    }
}
