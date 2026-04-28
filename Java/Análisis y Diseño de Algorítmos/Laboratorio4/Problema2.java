//Un sistema de autenticación simple solicita al usuario una contraseña.
//•	Si la contraseña es "admin123", muestra el mensaje: “Acceso concedido.”
//•	De lo contrario, muestra: “Acceso denegado.”

import java.util.Scanner;

public class Problema2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //entradas
        String contrasenia;
        System.out.print("Ingrese la contraseña: ");
        contrasenia = sc.nextLine();
        //proceso
        if (contrasenia.matches("admin123")){
            //salida
            System.out.println("Acceso Concedido");
        }else {
            //salida
            System.err.println("Acceso Denegado");
        }
    }
}
