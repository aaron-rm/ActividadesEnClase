package bInterfaz;

import cSistema.aUsuario.Cliente;
import cSistema.aUsuario.Cuenta;
import cSistema.cServicios.Agenda;
import cSistema.cServicios.Cita;

import javax.swing.*;
import java.awt.*;

public class InterfazCuenta extends JFrame{
    private final int ICON_SCALE = 30;
    private JPanel InterfazPrincipal;
    private JTextField usuarioTextField;
    private JTextField contraseñaTextField;
    private JButton limpiarCamposButton;
    private JButton crearCuentaButton;
    private JButton iniciarSesiónButton;
    private JButton salirButton;
    private JButton volverAlMenúPrincipalButton;
    private Cuenta usuario;
    private int cantUsuariosActuales;

    public InterfazCuenta(Cuenta[] usuarios, Agenda citas, int cantUsuarios){
        //frame principal
        JFrame frame = new JFrame("\uD835\uDE4E\uD835\uDE65\uD835\uDE5A\uD835\uDE5A\uD835\uDE59\uD835\uDE47\uD835\uDE56\uD835\uDE57 | Iniciar Sesión");
        frame.setVisible(true);
        frame.setContentPane(getInterfazPrincipal());
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
        frame.setSize(720,480);
        frame.setResizable(true);
        frame.setLocationRelativeTo(null);
        ImageIcon iconEmpresa = new ImageIcon(getClass().getResource("/images/SpeedLab LOGO.png"));
        frame.setIconImage(iconEmpresa.getImage().getScaledInstance(ICON_SCALE, ICON_SCALE, Image.SCALE_SMOOTH));

        this.cantUsuariosActuales = cantUsuarios;


        volverAlMenúPrincipalButton.addActionListener(e->{
            frame.dispose();
            new InterfazPrincipal(usuarios, citas, cantUsuariosActuales);
        });
        iniciarSesiónButton.addActionListener(e -> {

            try {
                String user = usuarioTextField.getText().trim();
                String contrasenia = contraseñaTextField.getText().trim();
                boolean seleccionUsuario=false;
                if (user.matches("") || contrasenia.matches("")){
                    throw new RuntimeException("Rellene todos los datos");
                }else {


                    for (int i = 0; i < cantUsuariosActuales; i++) {
                        if (usuarios[i].getIdCuenta().equals(user) && usuarios[i].getPassword().equals(contrasenia)) {
                            usuario = usuarios[i];
                            frame.dispose();
                            new InterfazProductos(usuarios,citas,usuario,cantUsuariosActuales);
                            seleccionUsuario = true;
                        }else {
                            seleccionUsuario = false;
                        }
                    }

                }
                if(seleccionUsuario){
                    JOptionPane.showMessageDialog(this,"Bienvenido "+usuario.cliente.getNombre());
                }else {
                    throw new RuntimeException("No se ha encontrado ninguna cuenta");
                }



            }catch (NullPointerException exception){
                JOptionPane.showMessageDialog(null,"No existe esta cuenta");
            }
            catch (RuntimeException exception){
                JOptionPane.showMessageDialog(null,exception.getMessage());
            }
        });

        limpiarCamposButton.addActionListener(e -> {
            //vaciar los campos
            usuarioTextField.setText("");
            contraseñaTextField.setText("");
        });

        salirButton.addActionListener(e -> {
           System.exit(0);
        });

        crearCuentaButton.addActionListener(e -> {
            //crear una cuenta
            if (cantUsuariosActuales>=usuarios.length){
                JOptionPane.showMessageDialog(null,"Límite de usuarios alcanzado");
            }else{
                InterfazCrearCuenta cuenta = new InterfazCrearCuenta(frame);
                cuenta.setVisible(true);

                boolean estado = cuenta.getEstado();
                if(estado){
                    usuarios[cantUsuariosActuales] = cuenta.getCuenta();
                    cantUsuariosActuales+=1;
                    usuario = cuenta.getCuenta();
                    int opcion = JOptionPane.showConfirmDialog(
                            null,
                            "¿Deseas iniciar sesión con la cuenta creada?",
                            "Iniciar Sesión",
                            JOptionPane.YES_NO_OPTION
                    );

                    if (opcion == JOptionPane.YES_OPTION) {
                        frame.dispose();
                        new InterfazProductos(usuarios,citas,usuario,cantUsuariosActuales);
                    }
                }

            }

        });
    }





    public JPanel getInterfazPrincipal() {
        return InterfazPrincipal;
    }

}

