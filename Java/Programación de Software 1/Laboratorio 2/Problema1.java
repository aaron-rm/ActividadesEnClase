package problema1;

//La liga de beisbol de Panamá le ha contratado para que usted realice un software que apoye el cálculo de las estadísticas de los jugadores
//Diseñe, según la POO, un programa que calcule las siguientes estadísticas de los lanzadores y bateadores.
//Bateadores
//•	Promedio de bateo= (número de hits/número de turnos al bate)
//•	Slugging = total de bases conseguidas / número de turnos al bate
//Lanzadores
//•	Efectividad = (carreras limpias / episodios lanzados) * 9
//•	WHIP (Walks más Hit por episodios lanzados) = (Base por bolas + hits)/episodios lanzados.
//•	Ponches por episodios = (número de ponches/episodios lanzados) x 9
//
//Indicaciones
//1.	Crear una clase para los bateadores y otra para los lanzadores.
//2.	Crear un objeto para cada clase.
//3.	El usuario suministrará la información que luego usará el objeto.
//4.	Crear variables, objetos y funciones según las normas de identificadores vistas en clase.

import java.util.Scanner;


public class Problema1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int hits, turnosBate, basesConseguidas, carrerasLimpias, basePorBolas, ponches, hitsLanzador;
        double episodiosLanzados;

        System.out.println("Ingrese Datos del Bateador");
        System.out.print("Número de hits: ");
        hits = scanner.nextInt();
        System.out.print("Número de turnos al bate: ");
        turnosBate = scanner.nextInt();
        System.out.print("Total de bases conseguidas: ");
        basesConseguidas = scanner.nextInt();

        Bateadores bateador1 = new Bateadores(hits,turnosBate,basesConseguidas);

        System.out.println("\nEstadísticas del Bateador");
        System.out.printf("El promedio de bateo del bateador es de: %.2f\n", bateador1.promedioDeBateo());
        System.out.printf("El promedio de slugging del bateador es de: %.2f\n\n", bateador1.slugging());


        System.out.println("\nIngrese Datos del Lanzador");
        System.out.print("Carreras limpias: ");
        carrerasLimpias = scanner.nextInt();
        System.out.print("Hits recibidos: ");
        hitsLanzador = scanner.nextInt();
        System.out.print("Episodios lanzados: ");
        episodiosLanzados = scanner.nextDouble();
        System.out.print("Bases por bolas provocadas: ");
        basePorBolas = scanner.nextInt();
        System.out.print("Bateadores ponchados: ");
        ponches = scanner.nextInt();

        Lanzadores lanzador1 = new Lanzadores(carrerasLimpias, episodiosLanzados, basePorBolas, ponches, hitsLanzador);

        System.out.println("\nEstadísticas del Lanzador");
        System.out.printf("La efectividad del lanzador es de: %.2f\n", lanzador1.efectividad());
        System.out.printf("El WHIP del lanzador es de: %.2f\n", lanzador1.calcularWHIP());
        System.out.printf("El promedio de ponches por episodio del lanzador es: %.2f\n", lanzador1.ponchesEpisodios());

        
    }
}
