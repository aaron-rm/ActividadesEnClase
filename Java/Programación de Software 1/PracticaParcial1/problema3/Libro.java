package problema3;

public class Libro {
    private String titulo, autor;

    Libro(String titulo, String autor){
        this.autor=autor;
        this.titulo=titulo;
    }

    public void mostrarInformacion() {
        System.out.println("---------------------");
        System.out.println("Título: " + titulo);
        System.out.println("Autor: " + autor);
    }
}
