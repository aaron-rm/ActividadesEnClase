package problema1;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String nombre;
        double precio, itbms;

        System.out.print("Nombre del objeto: ");
        nombre = scanner.nextLine();

        System.out.print("Precio del objeto: ");
        precio = scanner.nextDouble();

        Producto producto1 = new Producto(nombre,precio);

        System.out.println(producto1.getNombre()+" vale: "+producto1.calcularPrecioFinal()+"$");

    }
}
