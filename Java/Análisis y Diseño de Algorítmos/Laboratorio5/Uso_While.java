
import java.util.Scanner;

public class Uso_While {
    public static void main(String[] args) {
        int cantNum = 5;
        int contador = 0;
        int num[] = new int[cantNum];
        int suma=0,promedio=0;
        Scanner sc = new Scanner(System.in);

        while (contador < cantNum){
            System.out.printf("Inserte el número %d: ", contador+1);
            num[contador] = sc.nextInt();
            suma += num[contador];
            contador++;
        }
        contador = 0;
        promedio = suma/cantNum;

        while (contador < cantNum){
            System.out.printf("Número %d: %d\n", contador+1, num[contador]);
            contador++;
        }
        System.out.println("Suma de los números: " + suma);
        System.out.println("Promedio de los números: " + promedio);

    }
}
