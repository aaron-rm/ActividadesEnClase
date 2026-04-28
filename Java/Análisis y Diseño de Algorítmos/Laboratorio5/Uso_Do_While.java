
import java.util.Scanner;

public class Uso_Do_While {
    public static void main(String[] args) {
        int cantNum = 5;
        int contador = 0;
        int num[] = new int[cantNum];
        int suma=0,promedio=0;
        Scanner sc = new Scanner(System.in);

        do {
            System.out.printf("Inserte el número %d: ", contador+1);
            num[contador] = sc.nextInt();
            suma += num[contador];
            contador++;
        }while (contador < cantNum);

        contador = 0;
        promedio = suma/cantNum;

        do {
            System.out.printf("Número %d: %d\n", contador+1, num[contador]);
            contador++;
        }while (contador < cantNum);
        System.out.println("Suma de los números: " + suma);
        System.out.println("Promedio de los números: " + promedio);
    }
}
