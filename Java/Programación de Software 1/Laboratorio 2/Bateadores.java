package problema1;

//•	Promedio de bateo= (número de hits/número de turnos al bate)
//•	Slugging = total de bases conseguidas / número de turnos al bate


public class Bateadores {
    int hits, turnosBate, basesConseguidas;

    Bateadores(int hits, int turnosBate, int basesConseguidas){
        this.hits=hits;
        this.turnosBate=turnosBate;
        this.basesConseguidas=basesConseguidas;
    }

    double promedioDeBateo(){
        return (double) hits/turnosBate;
    }

    double slugging(){
        return (double) basesConseguidas/turnosBate;
    }

}



