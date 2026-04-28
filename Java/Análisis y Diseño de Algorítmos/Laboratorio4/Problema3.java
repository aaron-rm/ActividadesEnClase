//Narración 3 – Uso de if…else anidado
//Una aplicación de registro académico asigna calificaciones según la nota final (0–100):
//•	91–100 → “A”
//•	81–90 → “B”
//•	71–80 → “C”
//•	61–70 → “D”
//•	0–60 → “F”

import java.util.Scanner;

public class Problema3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //entrada
        int nota;
        System.out.print("Ingrese su nota final: ");
        nota = sc.nextInt();
        //proceso
        if (nota<=100){
            if (nota<91){
                if (nota<81){
                    if (nota<71){
                        if (nota<61){
                            if (nota<=60){
                                //salidas
                                System.out.println("F");
                            }
                        }else{
                            System.out.println("D");
                        }
                    }else{
                        System.out.println("C");
                    }
                }else{
                    System.out.println("B");
                }
            }else{
                System.out.println("A");
            }
        }
        sc.close();
    }
}
