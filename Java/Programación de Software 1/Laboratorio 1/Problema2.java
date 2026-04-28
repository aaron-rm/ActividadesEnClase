
//2.	Calcule el área de un rombo en centímetros cuadrados.
//Utilice la siguiente fórmula A = D*d/ 2.
//D= diagonal mayor
//d= diagonal menor

import java.util.Scanner;

public class Problema2
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        double diagMayor, diagMenor, area;

        System.out.print("Inserte la diagonal mayor en cm: ");
        diagMayor = scanner.nextDouble();
        System.out.print("Inserte la diagonal menor en cm: ");
        diagMenor = scanner.nextDouble();

        area = (diagMayor*diagMenor)/2;
        System.out.println("El área es de " + area + "cm^2");

        scanner.close();
    }
}
