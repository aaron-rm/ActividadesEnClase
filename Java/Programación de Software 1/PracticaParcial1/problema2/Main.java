package problema2;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String titulo, autor,nacionalidad;
        int anioPublicacion;

        System.out.print("Nombre del libro: ");
        titulo= scanner.nextLine();

        System.out.print("Nombre del autor: ");
        autor= scanner.nextLine();

        System.out.print("Nacionalidad del autor: ");
        nacionalidad= scanner.nextLine();

        System.out.print("Año de publicación del libro: ");
        anioPublicacion= scanner.nextInt();

        Autor autor1 = new Autor(autor,nacionalidad);
        Libro libro1 = new Libro(titulo,anioPublicacion, autor1.getNombre());

        libro1.mostrarInformacionLibro();
        autor1.mostrarInformacionAutor();
        scanner.close();
    }
}
