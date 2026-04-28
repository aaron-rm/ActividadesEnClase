//Narración 4 – Uso de switch case
//En una aplicación de gestión de tareas, el usuario selecciona una opción de menú:
//1.	Registrar tarea
//2.	Listar tareas
//3.	Eliminar tarea
//4.	Salir
//Dependiendo de la opción seleccionada, el programa muestra un mensaje confirmando la acción elegida.

import java.util.Scanner;

public class Problema4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //entrada
        int opcion;
        System.out.println("----Eliga una Opción----");
        System.out.println("1. Registrar tarea");
        System.out.println("2. Listar tareas");
        System.out.println("3. Eliminar tarea");
        System.out.println("4. Salir");
        System.out.print("Opción a Elegir: ");
        opcion = sc.nextInt();

        //proceso
        switch (opcion){
            case 1: {
                System.out.println("Acción Registrar Tarea");
                break;
            }
            case 2:{
                System.out.println("Acción Listar Tareas");
                break;
            }
            case 3:{
                System.out.println("Acción Eliminar Tarea");
                break;
            }
            case 4:{
                System.out.println("Acción Salir");
                break;
            }
            default: System.err.println("Error, eliga una opción correcta");
        }
    }
}
