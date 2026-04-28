
import java.time.LocalDateTime;

public class Sesion {
    private String usuario;
    private LocalDateTime horaInicio;
    private Programa programa;

    public Sesion(String usuario, Programa programa) {
        this.usuario = usuario;
        this.programa = programa;
        this.horaInicio = LocalDateTime.now();
    }

    public void iniciarSesion() {
        programa.iniciar();
        System.out.println("Sesión iniciada por " + usuario + " en: ");
        programa.getInfoPrograma();
        System.out.println("Hora Inicio: " + horaInicio);
    }

    public void cerrarSesion() {
        programa.detener();
        System.out.println("Sesión finalizada");
    }
}
