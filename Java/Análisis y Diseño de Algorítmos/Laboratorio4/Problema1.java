//En una aplicación de control de proyectos, se ingresa el porcentaje de avance de una tarea (0–100).
// Si el avance es igual a 100, se debe mostrar el mensaje:
//“Tarea completada.” De lo contrario, no se muestra nada adicional.

import java.util.Scanner;

public class Problema1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //entrada
        int avance;
        System.out.print("Ingrese el porcentaje de avance de la tarea: ");
        avance = sc.nextInt();
        //proceso
        if (avance == 100){
            //salida
            System.out.println("Tarea Completada");
        }
    }
}
