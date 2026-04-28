package Problema1;

public class Factura {
    private String fecha;
    private double precio;

    public Factura(String fecha, double precio) {
        this.fecha = fecha;
        this.precio = precio;
    }

    public String getFecha() {
        return fecha;
    }

    public double getPrecio() {
        return precio;
    }

    public void generarResumen(){
        System.out.println("Fecha: " + fecha);
        System.out.println("Precio final: " + (precio+(precio*0.07)));
    }
}
