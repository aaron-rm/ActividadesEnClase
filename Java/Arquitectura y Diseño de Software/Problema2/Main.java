package Problema2;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            System.out.print("Cantidad de cursos: ");
            int n = Integer.parseInt(br.readLine());
            Curso[] curso = new Curso[n];
            for (int i=0; i<n; i++) {
                System.out.print("Nombre: ");
                String name = br.readLine();
                System.out.print("Precio: ");
                double price = Double.parseDouble(br.readLine());
                curso[i] = new Curso(price, name);
            }
            Matricula matricula = new Matricula(curso);
            matricula.mostrarResumen();

        }catch(Exception e){
            System.err.println(e.getMessage());
        }
    }
}
