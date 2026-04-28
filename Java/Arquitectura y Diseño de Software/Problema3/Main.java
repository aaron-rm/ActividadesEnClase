package Problema3;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
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
