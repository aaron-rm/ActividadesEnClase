package problema4;
import java.io.BufferedReader;
import java.io.IOException;

//Declare 2 vectores. Uno contendrá el nombre de los estudiantes y el otro la calificación
//final obtenida en el curso.  Ordene los dos vectores. Permita al usuario escoger si ordena
//por orden de notas de menor a mayor ambos vectores o por orden alfabético

public class Problema4 {
    private String[] nombres;
    private double[] notas;

    public Problema4(int cantidad) {
        nombres = new String[cantidad];
        notas = new double[cantidad];
    }

    public void cargarDatos(BufferedReader reader) {
        for (int i = 0; i < nombres.length; i++) {
            try {
                System.out.print("Ingrese el nombre del estudiante #" + (i + 1) + ": ");
                nombres[i] = reader.readLine();

                while (true) {
                    try {
                        System.out.print("Ingrese la nota final de " + nombres[i] + " (0 a 100): ");
                        notas[i] = Double.parseDouble(reader.readLine());
                        if (notas[i] < 0 || notas[i] > 100) {
                            System.err.println("La nota debe estar entre 0 y 100.");
                            continue;
                        }
                        break;
                    } catch (NumberFormatException e) {
                        System.err.println("Ingrese un número válido para la nota.");
                    }
                }
            } catch (IOException e) {
                System.err.println("Error al leer el nombre del estudiante: " + e.getMessage());
                nombres[i] = "Desconocido";
                notas[i] = 0;
            }
        }
    }

    public void ordenarPorNotaAscendente() {
        ordenarNotas(true);
    }

    public void ordenarPorNotaDescendente() {
        ordenarNotas(false);
    }

    public void ordenarPorNombreAscendente() {
        ordenarNombres(true);
    }

    public void ordenarPorNombreDescendente() {
        ordenarNombres(false);
    }

    private void ordenarNotas(boolean ascendente) {
        for (int i = 0; i < notas.length - 1; i++) {
            for (int j = i + 1; j < notas.length; j++) {
                if ((ascendente && notas[i] > notas[j]) || (!ascendente && notas[i] < notas[j])) {
                    intercambiar(i, j);
                }
            }
        }
    }

    private void ordenarNombres(boolean ascendente) {
        for (int i = 0; i < nombres.length - 1; i++) {
            for (int j = i + 1; j < nombres.length; j++) {
                int cmp = nombres[i].compareToIgnoreCase(nombres[j]);
                if ((ascendente && cmp > 0) || (!ascendente && cmp < 0)) {
                    intercambiar(i, j);
                }
            }
        }
    }

    private void intercambiar(int i, int j) {
        String tempNombre = nombres[i];
        nombres[i] = nombres[j];
        nombres[j] = tempNombre;

        double tempNota = notas[i];
        notas[i] = notas[j];
        notas[j] = tempNota;
    }

    public void imprimir() {
        System.out.println("\nListado de estudiantes:");
        for (int i = 0; i < nombres.length; i++) {
            System.out.printf("%-20s Nota: %.2f\n", nombres[i], notas[i]);
        }
    }

    public void buscarPorNombre(String nombreBuscado) {
        boolean encontrado = false;
        for (int i = 0; i < nombres.length; i++) {
            if (nombres[i].equalsIgnoreCase(nombreBuscado)) {
                System.out.println("Estudiante encontrado: " + nombres[i] + " - Nota: " + notas[i]);
                encontrado = true;
                break;
            }
        }
        if (!encontrado) {
            System.out.println("No se encontró al estudiante con nombre: " + nombreBuscado);
        }
    }

    public void ejecutarMenu(BufferedReader reader) {
        try {
            cargarDatos(reader);

            while (true) {
                System.out.println("\nOpciones:");
                System.out.println("1 - Ordenar por nota ascendente");
                System.out.println("2 - Ordenar por nota descendente");
                System.out.println("3 - Ordenar por nombre ascendente (A-Z)");
                System.out.println("4 - Ordenar por nombre descendente (Z-A)");
                System.out.println("5 - Buscar estudiante por nombre");
                System.out.println("6 - Mostrar lista");
                System.out.println("0 - Volver al menú principal");
                System.out.print("Seleccione una opción: ");

                int opcionInterna = Integer.parseInt(reader.readLine());

                switch (opcionInterna) {
                    case 1 -> {
                        ordenarPorNotaAscendente();
                        System.out.println("Lista ordenada por nota (ascendente):");
                        imprimir();
                    }
                    case 2 -> {
                        ordenarPorNotaDescendente();
                        System.out.println("Lista ordenada por nota (descendente):");
                        imprimir();
                    }
                    case 3 -> {
                        ordenarPorNombreAscendente();
                        System.out.println("Lista ordenada por nombre (A-Z):");
                        imprimir();
                    }
                    case 4 -> {
                        ordenarPorNombreDescendente();
                        System.out.println("Lista ordenada por nombre (Z-A):");
                        imprimir();
                    }
                    case 5 -> {
                        System.out.print("Ingrese el nombre a buscar: ");
                        String nombre = reader.readLine();
                        buscarPorNombre(nombre);
                    }
                    case 6 -> imprimir();
                    case 0 -> {
                        return;
                    }
                    default -> System.out.println("Opción inválida.");
                }
            }

        } catch (IOException | NumberFormatException e) {
            System.err.println("Error durante la ejecución del menú: " + e.getMessage());
        }
    }
}
