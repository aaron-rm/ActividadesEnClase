package IniciarSesion;

import javax.swing.*;
import java.io.IOException;

public class IniciarSesion extends JPanel{
    private JPanel JPIniciarSesion;
    private JTextField entradaUsuario;
    private JTextField entradaContrasenia;
    private JButton botonIniciarSesion;
    private JButton botonCrearCuenta;
    private JButton botonVerCuentas;
    private JTextPane salidaCuentas;
    private JLabel salidaEstadoDeSesion;
    int contCuentas = -1;
    DatosSesion usuario = new DatosSesion("","");

    public IniciarSesion(){
        try {
        botonIniciarSesion.addActionListener(ActionListener ->{
            validarEntradas();
            if (usuario.iniciarSesion(entradaUsuario.getText(),entradaContrasenia.getText())){
                salidaEstadoDeSesion.setText("Cuenta válida");
                if (true){
                    //mandar a panel administrador

                }else {
                    //mandar a panel usuario

                }
            }else {
                salidaEstadoDeSesion.setText("Cuenta inválida");
            }
        });

        botonCrearCuenta.addActionListener(ActionListener->{
            validarEntradas();
            System.out.println("Cuenta creada");
            usuario = new DatosSesion(entradaUsuario.getText().trim(),entradaContrasenia.getText().trim());
            salidaEstadoDeSesion.setText("Cuenta Creada");
        });

        botonVerCuentas.addActionListener(ActionListener->{
            if (contCuentas == -1){
                salidaCuentas.setText("No hay usuarios");
            }

            salidaCuentas.setText(usuario.mostrarDatos(contCuentas));

        });

        }
        catch (NumberFormatException e){
            System.err.println(e.getMessage());
        }
        catch (NullPointerException e){
            System.err.println(e.getMessage());
        }
        catch (RuntimeException e){
            System.err.println(e.getMessage());
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }

    public void validarEntradas(){
        if (entradaUsuario.getText().trim().equals("")|| entradaContrasenia.getText().trim().equals("")){
            salidaEstadoDeSesion.setText("! Rellene todos los campos");
            throw new RuntimeException();
        }
    }


    public JPanel getJPIniciarSesion(){
        return JPIniciarSesion;
    }
}