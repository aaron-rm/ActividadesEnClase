package problema3;

public class Biblioteca {
    private String nombre, direccion;
    Libro libro1,libro2;

    Biblioteca(String nombre, String direccion, Libro libro1, Libro libro2){
        this.nombre=nombre;
        this.direccion=direccion;
        this.libro1=libro1;
        this.libro2=libro2;
    }

    public void mostrarInformacion() {
        System.out.println("");
        System.out.println("Información de la biblioteca");
        System.out.println("----------------------------");
        System.out.println("Biblioteca: " + nombre);
        System.out.println("Dirección: " + direccion);
        System.out.println("");
        System.out.println("Información del libro 1:");
        libro1.mostrarInformacion();
        System.out.println("");
        System.out.println("Información del libro 2:");
        libro2.mostrarInformacion();
    }
}
