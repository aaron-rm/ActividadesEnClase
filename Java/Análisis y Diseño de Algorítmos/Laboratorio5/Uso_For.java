
import java.util.Scanner;

public class Uso_For {
    public static void main(String[] args) {
        int cantNum = 5;
        int num[] = new int[cantNum];
        int suma=0,promedio=0;
        Scanner sc = new Scanner(System.in);

        for (int i=0;i<cantNum;i++){
            System.out.printf("Inserte el número %d: ",i+1);
            num[i] = sc.nextInt();
            suma += num[i];
        }

        promedio = suma/cantNum;

        for (int i=0;i<cantNum;i++){
            System.out.printf("Número %d: %d\n",i+1,num[i]);
        }
        System.out.println("Suma de los números: " + suma);
        System.out.println("Promedio de los números: " + promedio);

    }
}
