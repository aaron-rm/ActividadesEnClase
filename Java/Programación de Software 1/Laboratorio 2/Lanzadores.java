package problema1;

//•	Efectividad = (carreras limpias / episodios lanzados) * 9
//•	WHIP (Walks más Hit por episodios lanzados) = (Base por bolas + hits)/episodios lanzados.
//•	Ponches por episodios = (número de ponches/episodios lanzados) x 9



public class Lanzadores {
    int carrerasLimpias, basePorBolas, ponches, hitsLanzador;
    double episodiosLanzados;

    Lanzadores(int carrerasLimpias, double episodiosLanzados, int basePorBolas, int ponches, int hitsLanzador){
        this.carrerasLimpias = carrerasLimpias;
        this.episodiosLanzados = episodiosLanzados;
        this.basePorBolas = basePorBolas;
        this.ponches = ponches;
        this.hitsLanzador = hitsLanzador;
    }

    double efectividad(){
        return (carrerasLimpias/episodiosLanzados)*9;
    }

    double calcularWHIP(){
        return (basePorBolas+hitsLanzador)/episodiosLanzados;
    }

    double ponchesEpisodios(){
        return (ponches/episodiosLanzados)*9;
    }
}
