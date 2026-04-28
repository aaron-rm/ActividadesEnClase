//Integrantes:
//Aaron Remarchuk       8-1042-134
//Luis King             8-1017-548
//Edwin Rodriguez       8-975-208
//Victor Villareal      8-1016-1917


import java.util.Scanner;

public class Proyecto1ERD {
    //se define final, porque es el limite de nuestro arreglo
    static final int MAX_LIBROS = 50;

    // se crea nuestro arreglo(catalogo) de tipo registros(Libro)
    static Libro[] catalogo = new Libro[MAX_LIBROS];

    //define la cantidad de libros en el arreglo
    static int totalLibros = 0;

    static Scanner sc = new Scanner(System.in);


    public static void main(String[] args) {
        int opcion;

        //menú de opciones, se repite hasta que se eliga '0' (salir)
        do {
            System.out.println("\n====== CATÁLOGO BIBLIOTECA ======");
            System.out.println("1. Agregar libro");
            System.out.println("2. Buscar libro por título o autor");
            System.out.println("3. Listar todos los libros");
            System.out.println("4. Filtrar libros por año o categoría");
            System.out.println("5. Editar libro existente");
            System.out.println("0. Salir");
            System.out.print("Seleccione una opción: ");
            opcion = leerEntero();

            switch (opcion) {
                case 1: agregarLibro();
                case 2: buscarLibro();
                case 3: listarLibros();
                case 4: filtrarLibros();
                case 5: editarLibro();
                case 0: System.out.println("¡Hasta luego!");
                default: System.out.println("Opción inválida.");
            }
        } while (opcion != 0);
    }


    static void agregarLibro() {
        //si nuetro catalogo esta lleno, no se crea un libro nuevo
        if (totalLibros >= MAX_LIBROS) {
            System.out.println("¡Catálogo lleno!");
            return;
        }

        System.out.println("--- Agregar nuevo libro ---");
        String titulo = leerTexto("Título: ");
        String autor = leerTexto("Autor: ");
        int anio = leerEnteroRango("Año de publicación: ", 1450, 2100);
        String categoria = leerTexto("Categoría: ");

        String isbn;
        //ciclo para validar que no exista otro libro con el mismo isbn
        do {
            isbn = leerTexto("ISBN (hasta 13 dígitos numéricos): ");
            if (!isbn.matches("\\d{1,13}")) {
                System.out.println("ISBN inválido. Debe tener hasta 13 dígitos.");
                continue;
            }
            if (buscarPorISBN(isbn) != -1) {
                System.out.println("Ya existe un libro con ese ISBN.");
                isbn = "";
            }
        } while (isbn.isEmpty());

        //se crea el nuevo libro en el catalogo
        catalogo[totalLibros++] = new Libro(titulo, autor, anio, categoria,
                isbn);
        System.out.println("✓ Libro agregado con éxito.");
    }

    static void buscarLibro() {
        //verifica que nuestro catalogo no este vacio
        if (totalLibros == 0) {
            System.out.println("El catálogo está vacío.");
            return;
        }

        //lee el titulo o autor a buscar
        String termino = leerTexto("Ingrese título o autor a buscar: ").toLowerCase();
        boolean encontrado = false;

        //verifica si existe un libro con este titulo o autor
        for (int i = 0; i < totalLibros; i++) {
            if (catalogo[i].titulo.toLowerCase().contains(termino) ||
                    catalogo[i].autor.toLowerCase().contains(termino)) {
                System.out.println("\nLibro #" + (i + 1));
                catalogo[i].mostrar();
                encontrado = true;
            }
        }

        if (!encontrado) System.out.println("No se encontraron coincidencias.");
    }

    static void listarLibros() {
        if (totalLibros == 0) {
            System.out.println("El catálogo está vacío.");
            return;
        }

        //imprime todos los libros existentes
        System.out.println("\n--- Lista de libros ---");
        for (int i = 0; i < totalLibros; i++) {
            System.out.println("\nLibro #" + (i + 1));
            catalogo[i].mostrar();
        }
    }

    static void filtrarLibros() {
        if (totalLibros == 0) {
            System.out.println("El catálogo está vacío.");
            return;
        }

        System.out.println("Filtrar por:");
        System.out.println("1. Año");
        System.out.println("2. Categoría");
        int opcion = leerEntero();

        boolean encontrado = false;


        //busca el libro por año
        if (opcion == 1) {
            int anio = leerEnteroRango("Ingrese año: ", 1450, 2100);
            for (int i = 0; i < totalLibros; i++) {
                if (catalogo[i].anio == anio) {
                    System.out.println("\nLibro #" + (i + 1));
                    catalogo[i].mostrar();
                    encontrado = true;
                }
            }
        } else if (opcion == 2) {
            //busca el libro por categoria
            String categoria = leerTexto("Ingrese categoría: ").toLowerCase();
            for (int i = 0; i < totalLibros; i++) {
                if (catalogo[i].categoria.toLowerCase().contains(categoria)) {
                    System.out.println("\nLibro #" + (i + 1));
                    catalogo[i].mostrar();
                    encontrado = true;
                }
            }
        } else {
            System.out.println("Opción inválida.");
            return;
        }

        if (!encontrado) System.out.println("No se encontraron libros con ese criterio.");
    }

    static void editarLibro() {
        if (totalLibros == 0) {
            System.out.println("El catálogo está vacío.");
            return;
        }

        //busca el libro a editar por isbn
        String isbn = leerTexto("Ingrese el ISBN del libro a editar: ");
        int idx = buscarPorISBN(isbn);
        if (idx == -1) {
            System.out.println("Libro no encontrado.");
            return;
        }

        Libro libro = catalogo[idx];
        System.out.println("Dejar en blanco para mantener el valor actual.");


        String nuevoTitulo = leerTextoOpcional("Nuevo título (" + libro.titulo
                + "): ");
        if (!nuevoTitulo.isEmpty()) libro.titulo = nuevoTitulo;

        String nuevoAutor = leerTextoOpcional("Nuevo autor (" + libro.autor +
                "): ");
        if (!nuevoAutor.isEmpty()) libro.autor = nuevoAutor;

        String nuevoAnioStr = leerTextoOpcional("Nuevo año (" + libro.anio +
                "): ");
        if (!nuevoAnioStr.isEmpty()) {
            try {
                int nuevoAnio = Integer.parseInt(nuevoAnioStr);
                if (nuevoAnio >= 1450 && nuevoAnio <= 2100)
                    libro.anio = nuevoAnio;
                else
                    System.out.println("Año fuera de rango. Se mantiene el anterior.");
            } catch (NumberFormatException e) {
                System.out.println("Formato inválido. Se mantiene el año anterior.");
            }
        }

        String nuevaCategoria = leerTextoOpcional("Nueva categoría (" +
                libro.categoria + "): ");
        if (!nuevaCategoria.isEmpty()) libro.categoria = nuevaCategoria;

        System.out.println("✓ Libro actualizado.");
    }


    static int buscarPorISBN(String isbn) {
        for (int i = 0; i < totalLibros; i++) {
            if (catalogo[i].isbn.equals(isbn)) return i;
        }
        return -1;
    }


    static String leerTexto(String mensaje) {
        String texto;
        do {
            System.out.print(mensaje);
            texto = sc.nextLine().trim();
            if (texto.isEmpty()) System.out.println("Este campo no puede estar vacío.");
        } while (texto.isEmpty());
        return texto;
    }

    //funcion para leer una entrada que puede ser vacia
    static String leerTextoOpcional(String mensaje) {
        System.out.print(mensaje);
        return sc.nextLine().trim();
    }

    //válida que se ingrese un entero
    static int leerEntero() {
        while (true) {
            try {
                return Integer.parseInt(sc.nextLine().trim());
            } catch (NumberFormatException e) {
                System.out.print("Ingrese un número válido: ");
            }
        }
    }

    //válida que se ingrese un entero dentro del rango
    static int leerEnteroRango(String mensaje, int min, int max) {
        int valor;
        do {
            System.out.print(mensaje);
            try {
                valor = Integer.parseInt(sc.nextLine().trim());
                if (valor >= min && valor <= max) return valor;
                else System.out.println("Número fuera de rango.");
            } catch (NumberFormatException e) {
                System.out.println("Ingrese un número válido.");
            }
        } while (true);
    }
}


// registro Libro
class Libro {
    String titulo;
    String autor;
    int anio;
    String categoria;
    String isbn;

    public Libro(String titulo, String autor, int anio, String categoria,
                 String isbn) {
        this.titulo = titulo;
        this.autor = autor;
        this.anio = anio;
        this.categoria = categoria;
        this.isbn = isbn;
    }

    //imprime toda la información del libro
    void mostrar() {
        System.out.println("Título   : " + titulo);
        System.out.println("Autor    : " + autor);
        System.out.println("Año      : " + anio);
        System.out.println("Categoría: " + categoria);
        System.out.println("ISBN     : " + isbn);
    }
}

