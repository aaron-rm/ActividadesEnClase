package problema1;

public class Multa {
    private String nombre,id;
    private int tipoVia,velocidad;

    public Multa(String nombre, String id, int tipoVia, int velocidad){
        this.nombre=nombre;
        this.id=id;
        this.tipoVia=tipoVia;
        this.velocidad=velocidad;
    }

    public int obtenerMulta() {
        if(tipoVia==1){
            if (velocidad > 40) {
                return ((velocidad - 40) * 5);
            } else return 0;
        }
        else if (tipoVia==2) {
            if (velocidad > 25) {
                return ((velocidad - 25) * 10);
            } else return 0;
        }
        else{
            if (velocidad > 100) {
                return ((velocidad-100)*2);
            } else return 0;
        }
    }


    public String nombreVia(){
        switch (tipoVia){
            case 1: return ("Residencial");
            case 2: return ("Escolar");
            case 3: return ("Autopista");
            default: return "";
        }
    }


    public void informacionMulta(){
        System.out.println();
        System.out.println("Conductor:"+getNombre());
        System.out.println("ID:"+getId());
        System.out.println("Transitaba en la via: "+nombreVia());
        System.out.println("Velocidad del vehículo: "+getVelocidad()+"km/h");
        if(obtenerMulta()==0){
            System.out.println("No excede el límite de velocidad");
        }else System.out.println("Monto de multa: $"+obtenerMulta());
    }


    public int getTipoVia() {
        return tipoVia;
    }

    public int getVelocidad() {
        return velocidad;
    }

    public String getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setId(String id) {
        this.id = id;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setTipoVia(int tipoVia) {
        this.tipoVia = tipoVia;
    }

    public void setVelocidad(int velocidad) {
        this.velocidad = velocidad;
    }
}
