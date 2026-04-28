package Problema1;

public class DetalleFactura{
    private Factura f;

    public DetalleFactura(Factura f) {
        this.f = f;
    }

    public double getITBMS() {
        return (f.getPrecio() * 0.07);
    }

    public double getPrecio() {
        return f.getPrecio();
    }

    public void generarResumen() {
        System.out.println("Valor bruto: " + getPrecio());
        System.out.println("ITBMS: " + getITBMS());
        f.generarResumen();
    }
}
