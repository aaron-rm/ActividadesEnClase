
import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.DateTimeException;
import java.time.LocalDate;
import java.util.Random;


public class Productos {
    private String id;
    private String nombre,marca;
    private double precio,garantia;
    private LocalDate fechaDeVenta;
    private LocalDate fechaActual = LocalDate.now();
    private LocalDate fechaVencimiento;
    private Random aleatorio = new Random(System.currentTimeMillis());

    public Productos(){
        while (true){
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        try {
            System.out.print("Nombre del producto: ");
            this.nombre = reader.readLine().trim();
            if (nombre.equals("")){
                throw new NullPointerException();
            }
            System.out.print("Marca del producto: ");
            this.marca = reader.readLine().trim();
            if (marca.equals("")){
                throw new NullPointerException();
            }
            System.out.print("Precio del producto: ");
            String a = reader.readLine().trim();
            if (a.equals("")){
                throw new NullPointerException();
            }else this.precio = Double.parseDouble(a);
            System.out.print("Fecha de venta (AAAA-MM-DD): ");
            fechaDeVenta = LocalDate.parse(reader.readLine());
            fechaVencimiento = fechaDeVenta.plusDays(365);

            this.id = (nombre.substring(0, 1)+marca.substring(0, 1)+aleatorio.nextInt(10)+aleatorio.nextInt(10)+aleatorio.nextInt(10));

            System.out.println("Id del producto: " + id);


        }
        catch (NullPointerException e){
            System.out.println();
            System.err.println("Rellene toda la información");
            continue;
        }
        catch (NumberFormatException e){
            System.out.println();
            System.err.println("Ingrese datos válidos");
            continue;
        }
        catch (DateTimeException e){
            System.out.println();
            System.err.println("Ingrese la fecha con el formato (AAAA-MM-DD)");
            continue;
        }
        catch (RuntimeException e) {
            System.out.println();
            System.err.println(e.getMessage());
            continue;
        }
        catch (Exception e){
            System.out.println();
            System.err.println(e.getMessage());
            continue;
        }
        break;
        }
    }
    public Productos(Productos productos){
        this.id = productos.id;
        this.nombre = productos.nombre;
        this.marca = productos.marca;
        this.fechaDeVenta = productos.fechaDeVenta;
        this.precio = productos.precio;
        this.garantia = productos.garantia;
    }

    public double getGarantia() {
        if (fechaActual.isBefore(fechaDeVenta)) {
            garantia=0.0;
        }else {
            garantia = fechaVencimiento.toEpochDay()-fechaDeVenta.toEpochDay();
        }
        return garantia;
    }

    public void imprimirInformacion(){
        System.out.println("Nombre: " + nombre);
        System.out.println("Marca: " + marca);
        System.out.println("Precio: " + precio);
        System.out.println("Fecha de Venta: " + fechaDeVenta);
        System.out.printf("Garantia: %.2f meses\n", getGarantia()/30);
        System.out.println("Id: " + id);
    }

    public void verificarGarantia(){
        while(true){
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        try {
            System.out.print("Ingrese la fecha actual (AAAA-MM-DD): ");
            fechaActual = LocalDate.parse(reader.readLine());
            if (fechaActual.isBefore(fechaDeVenta)) {
                System.out.println("Aún no aplica la garantía");
            }else{
                System.out.println("Aún quedan: "+ (fechaVencimiento.toEpochDay()-fechaActual.toEpochDay()) +" días de garantia");
            }
        }
        catch (DateTimeException e){
            System.out.println();
            System.err.println("Ingrese la fecha con el formato (AAAA-MM-DD)");
            continue;
        }
        catch (RuntimeException e){
            System.out.println();
            System.err.println(e.getMessage());
            continue;
        }
        catch (Exception e){
            System.out.println();
            System.err.println(e.getMessage());
            continue;
        }
        break;
        }
    }

}
