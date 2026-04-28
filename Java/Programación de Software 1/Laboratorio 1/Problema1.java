
//1.	Realice un programa que transforme de grados Centígrados a grados Fahrenheit.
//La fórmula es:  F = 32 + (9* C/5)

import java.util.Scanner;

public class Problema1
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        double centigrados, fahrenheit;

        System.out.print("Ingrese los grados Centígrados: ");
        centigrados = scanner.nextDouble();
        fahrenheit = 32 + (9* centigrados/5);

        System.out.println("En grados Fahrenheit serían: " + fahrenheit);

        scanner.close();
    }
}
