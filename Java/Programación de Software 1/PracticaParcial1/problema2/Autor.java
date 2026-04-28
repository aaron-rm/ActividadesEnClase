package problema2;

public class Autor {
    private String nombre, nacionalidad;

    Autor(String nombre, String nacionalidad){
        this.nombre=nombre;
        this.nacionalidad=nacionalidad;
    }

    public String getNombre() {
        return nombre;
    }

    public String getNacionalidad() {
        return nacionalidad;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setNacionalidad(String nacionalidad) {
        this.nacionalidad = nacionalidad;
    }

    public void mostrarInformacionAutor(){
        System.out.println("Nombre del autor: "+getNombre());
        System.out.println("Nacionalidad del autor: "+getNacionalidad());
    }
}
