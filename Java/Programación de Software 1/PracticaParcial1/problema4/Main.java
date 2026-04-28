package problema4;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int i,numEstudiantes;
        String nombre,apellido,numMatricula,carrera;
        int calif1,calif2,calif3;
        System.out.println("Información del estudiante");
        System.out.print("Ingrese nombre: ");
        nombre=scanner.nextLine();
        System.out.print("Ingrese apellido: ");
        apellido=scanner.nextLine();
        System.out.print("Ingrese número de matricula: ");
        numMatricula=scanner.nextLine();
        System.out.print("Ingrese carrera: ");
        carrera=scanner.nextLine();

        do {
            System.out.print("Ingrese calificación 1: ");
            calif1 = scanner.nextInt();
        }while(calif1<0||calif1>10);
        do {
        System.out.print("Ingrese calificación 2: ");
        calif2=scanner.nextInt();
        }while(calif2<0||calif2>10);
        do {
        System.out.print("Ingrese calificación 3: ");
        calif3=scanner.nextInt();
        }while(calif3<0||calif3>10);

        Estudiantes estudiante1 = new Estudiantes(nombre,apellido,numMatricula,carrera,calif1,calif2,calif3);
        estudiante1.mostrarInformacion();
    }
}
