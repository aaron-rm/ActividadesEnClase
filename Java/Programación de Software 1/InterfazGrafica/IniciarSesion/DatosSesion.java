package IniciarSesion;

public class DatosSesion {
    private String[] usuario;
    private String[] contrasenia;
    private int tipoCuenta;     // 0 Administrador, 1 Usuario
    private final String usuarioAdministrador = "Administrador";
    private final String contraseniaAdministrador = "Administrador";
    private int contCuentas=-1;

    public DatosSesion(String Usuario, String Contrasenia){
        contCuentas =+ 1;
        this.usuario[contCuentas]=Usuario;
        this.contrasenia[contCuentas]=Contrasenia;
    }

    public boolean iniciarSesion(String usuarioInterfaz, String contraseniaInterfaz){
        if (usuarioInterfaz.equals(usuarioAdministrador)){
            if (contraseniaInterfaz.equals(contraseniaAdministrador)){
                this.tipoCuenta = 0;
                System.out.println("Cuenta admin válida");
                return true;
            }
        }else if (usuarioInterfaz.equals(usuario)){
            if (contraseniaInterfaz.equals(contrasenia)){
                this.tipoCuenta = 1;
                System.out.println("Cuenta usuario válida");
                return true;
            }else {
                return false;
            }
        }else {
            return false;
        }
        return false;
    }

    public String mostrarDatos(int i){
        for (i=0;i<=contCuentas;i++){
            return ("Usuario: " + usuario[i]);
        }
        return "";
    }

}
