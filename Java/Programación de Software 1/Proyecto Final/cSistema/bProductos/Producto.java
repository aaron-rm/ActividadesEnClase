package cSistema.bProductos;

// Clase Producto
public class Producto {
    private int id;
    private String nombre;
    private String descripcion;
    private double precio;
    private String categoria;

    // Constructor
    public Producto(int id, String nombre, String descripcion, double precio, String categoria) {
        this.id = id;
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.precio = precio;
        this.categoria = categoria;
    }

    // Getters
    public int getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public double getPrecio() {
        return precio;
    }

    public String getCategoria() {
        return categoria;
    }

    // Setters
    public void setId(int id) {
        this.id = id;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }


    public String toString() {
        return String.format("ID: %d | %s\nDescripción: %s\nPrecio: $%.2f\nCategoría: %s\n%s",
                id, nombre, descripcion, precio, categoria, "-".repeat(50));
    }
}
