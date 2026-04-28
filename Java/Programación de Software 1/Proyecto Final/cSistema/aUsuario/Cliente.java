package cSistema.aUsuario;

public class Cliente {
    private String id;
    private String nombre;
    private int telefono;
    private String correoElectronico;

    public Cliente(String id, String nombre, int telefono, String correoElectronico) {
        this.id = id;
        this.nombre = nombre;
        this.telefono = telefono;
        this.correoElectronico = correoElectronico;
    }

    public String getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public int getTelefono() {
        return telefono;
    }

    public String getCorreoElectronico() {
        return correoElectronico;
    }

    public void mostrarInfoCliente() {
        System.out.println("Cliente ID: " + id);
        System.out.println("Nombre: " + nombre);
        System.out.println("Teléfono: " + telefono);
        System.out.println("Correo Electrónico: " + correoElectronico);
    }
    public String imprimirInfoCliente() {
        String infoCliente = String.format("\nCliente ID: "+ id+"\nNombre: " +nombre+"\nTeléfono: "+telefono+"\nCorreo Electónico: "+correoElectronico+"\n");
        return infoCliente;
    }
}
