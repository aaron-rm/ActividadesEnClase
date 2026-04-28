package cSistema.cServicios;

public class Cita {
    private Cliente cliente;
    private String servicio;
    private String metodoServicio;
    private String fecha;
    private String horario;

    public Cita(Cliente cliente, String servicio, String metodoServicio, String fecha, String horario) {
        this.cliente = cliente;
        this.servicio = servicio;
        this.metodoServicio = metodoServicio;
        this.fecha = fecha;
        this.horario = horario;
    }

    public String getServicio() {
        return servicio;
    }

    public String getMetodoServicio() {
        return metodoServicio;
    }

    public String getFecha() {
        return fecha;
    }

    public String getHorario() {
        return horario;
    }
}
