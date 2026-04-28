package problema3;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String nombre, direccion, autor, titulo;

        System.out.print("Nombre de la biblioteca:");
        nombre=scanner.nextLine();
        System.out.print("Dirección de la biblioteca:");
        direccion=scanner.nextLine();

        System.out.print("Titulo del libro 1:");
        titulo=scanner.nextLine();
        System.out.print("Autor del libro 1:");
        autor=scanner.nextLine();
        Libro libro1 = new Libro(titulo,autor);

        System.out.print("Titulo del libro 2:");
        titulo=scanner.nextLine();
        System.out.print("Autor del libro 2:");
        autor=scanner.nextLine();
        Libro libro2 = new Libro(titulo,autor);

        Biblioteca biblioteca = new Biblioteca(nombre,direccion, libro1, libro2);
        biblioteca.mostrarInformacion();
    }
}
