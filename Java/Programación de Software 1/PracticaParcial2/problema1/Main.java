package problema1;

//Diseñe un programa que valide una contraseña. Las características de la
//contraseña son:
//o  Mínimo 8 caracteres.
//o Contenga al menos un número.
//o Contenga al menos una letra mayúscula.
//Si la contraseña no cumple, informar el motivo. Repetir hasta que se ingrese una
//contraseña válida.

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String contrasenia;
        try {
            do {
                System.out.printf("\nIngrese una contraseña: ");
                contrasenia= reader.readLine();
            }while (validacion(contrasenia));
            System.out.println("Contraseña válida");
        }
        catch (RuntimeException e){
            System.err.println("Error: " + e.getMessage());
        }
        catch (IOException e){
            System.err.println("Error: " + e.getMessage());
        }
    }

    static boolean validacion(String c){
        if (c.length()>=8){
        }else {
            System.err.println("Contraseña inválida: debe contener al 8 caracteres");
            return true;
        }
        if (c.matches(".*\\d.*")){
        }else {
            System.err.println("Contraseña inválida: debe contener al menos un número");
            return true;
        }
        if (c.matches(".*[A-Z].*")){
        }else {
            System.err.println("Contraseña inválida: debe contener al menos una mayúscula");
            return true;
        }
        return false;
    }
}

