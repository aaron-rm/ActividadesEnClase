package Problema3;

public class Main {
    public static void main(String[] args) {
        try {
            Programa p1 = new Programa("Word", "15.4");
            Sesion s1 = new Sesion("Victor", p1);

            s1.iniciarSesion();
            s1.cerrarSesion();
        }catch(Exception e) {
            System.err.println(e.getMessage());
        }
    }
}
