package Lab8.problema1;

public class ProcesadorVocales {
    public static char[] obtenerVocales(String palabra) {
        palabra = palabra.toLowerCase();
        int contador = 0;

        // Contar vocales
        for (int i = 0; i < palabra.length(); i++) {
            char c = palabra.charAt(i);
            if (esVocal(c)) {
                contador++;
            }
        }

        // Crear arreglo y llenar
        char[] vocales = new char[contador];
        int index = 0;

        for (int i = 0; i < palabra.length(); i++) {
            char c = palabra.charAt(i);
            if (esVocal(c)) {
                vocales[index++] = c;
            }
        }

        return vocales;
    }

    private static boolean esVocal(char c) {
        return "aeiou".indexOf(c) != -1;
    }
}
