package problema1;

public class Producto {
    private String nombre;
    private double precio, itbms;

    Producto(String nombre, double precio) {
        this.nombre = nombre;
        this.precio = precio;
    }

    public double getPrecio() {
        return precio;
    }

    public double getItbms() {
        return (getPrecio()*0.07);
    }

    public String getNombre() {
        return nombre;
    }

    public void setItbms(double itbms) {
        this.itbms = itbms;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public double calcularPrecioFinal(){
        return(getPrecio()+getItbms());
    }


}
