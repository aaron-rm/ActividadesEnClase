package problema2;

public class Libro {
    private String titulo,autor;
    private int anioPublicacion;

    Libro(String titulo, int anioPublicacion, String autor){
        this.anioPublicacion=anioPublicacion;
        this.autor=autor;
        this.titulo=titulo;
    }

    public int getAnioPublicacion() {
        return anioPublicacion;
    }

    public String getAutor() {
        return autor;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setAnioPublicacion(int anioPublicacion) {
        this.anioPublicacion = anioPublicacion;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void mostrarInformacionLibro() {
        System.out.println("Titulo del libro: "+getTitulo());
        System.out.println("Año de publicacion: "+getAnioPublicacion());
        System.out.println("Autor del libro: "+getAutor());
    }
}
