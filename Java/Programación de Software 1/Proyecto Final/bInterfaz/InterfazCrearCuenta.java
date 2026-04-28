package bInterfaz;

import cSistema.aUsuario.Cliente;
import cSistema.aUsuario.Cuenta;

import javax.swing.*;
import java.awt.*;

public class InterfazCrearCuenta extends JDialog {
    private final int ICON_SCALE = 30;
    private JPanel InterfazPrincipal;
    private JButton limpiarCamposButton;
    private JButton crearCuentaButton;
    private JTextField txtNombre;
    private JTextField txtID;
    private JTextField txtTelefono;
    private JTextField txtCorreo;
    private JTextField txtUsuario;
    private JTextField txtContrasenia;
    private JButton volverButton;
    public Cuenta cuenta;
    private boolean estado;

    public InterfazCrearCuenta(JFrame frame) {
        //frame principal
        super(frame,"Crear Cuenta",true);
        setSize(720,480);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(frame.DISPOSE_ON_CLOSE);
        setContentPane(getInterfazPrincipal());

        limpiarCamposButton.addActionListener(e -> {
            //vaciar todos los campos
            txtNombre.setText("");
            txtID.setText("");
            txtTelefono.setText("");
            txtCorreo.setText("");
            txtUsuario.setText("");
            txtContrasenia.setText("");
        });

        crearCuentaButton.addActionListener(e -> {
            //crear una cuenta
            boolean verificado = false;
            try {
                String nombre = validarVacio(txtNombre.getText().trim());
                String id = validarVacio(txtID.getText().trim());
                int telefono = validarTelefono(txtTelefono.getText().trim());
                String correo = validarVacio(txtCorreo.getText().trim());
                String usuario = validarVacio(txtUsuario.getText().trim());
                String contrasenia = validarVacio(txtContrasenia.getText().trim());


                Cliente cliente = new Cliente(id,nombre,telefono,correo);
                this.cuenta = new Cuenta(usuario,contrasenia,cliente);

                verificado = true;
            }catch (NullPointerException exception){
                JOptionPane.showMessageDialog(null,exception.getMessage());

            }

            if(verificado){
                JOptionPane.showMessageDialog(null, "Cuenta creada con éxito");
                estado = true;
                dispose();
            }


        });

        volverButton.addActionListener(event->{
            estado = false;
            dispose();
        });
    }

    public boolean getEstado(){
        return estado;
    }


    public Cuenta getCuenta() {
        return cuenta;
    }
    public int validarTelefono(String texto){
        int num=0;
        if (texto.equals("")){
            throw new NullPointerException("Rellene todos los campos");
        }else
        try {
            num = Integer.parseInt(texto);
        }catch (NumberFormatException exception){
            throw new NullPointerException("Inserte un número de teléfono válido");
        }
        return num;
    }

    public String validarVacio(String dato) throws NullPointerException{
        if (dato.equals("")){
            throw new NullPointerException("Rellene todos los campos");
        }
        return dato;
    }

    public JPanel getInterfazPrincipal() {
        return InterfazPrincipal;
    }
}
