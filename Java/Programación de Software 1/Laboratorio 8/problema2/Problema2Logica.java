package Lab8.problema2;

import javax.swing.*;

public class Problema2Logica {

    private int inicio,fin;

    public Problema2Logica(String txtInf, String txtSup){
        try {
            this.inicio = Integer.parseInt(txtInf);
            this.fin = Integer.parseInt(txtSup);

            if (inicio > fin){
                throw new ArithmeticException();
            }




        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(null, "Por favor, ingrese números válidos.");
        }
        catch (ArithmeticException ex) {
            JOptionPane.showMessageDialog(null, "El límite inferior no puede ser mayor al límite superior");
        }

    }

    public ListModel getLista(DefaultListModel listaPalindromos, JCheckBox checkBoxExtra){
        listaPalindromos.clear();
        try {
            for (int i = inicio; i <= fin; i++) {
                if (checkBoxExtra.isSelected()){
                    if (i > -10 && i < 10){
                        listaPalindromos.clear();
                    }else if (esPalindromo(i)) {
                        listaPalindromos.addElement(i);
                    }
                }else if (esPalindromo(i)) {
                    listaPalindromos.addElement(i);
                }
            }
        }
        catch (NullPointerException ex){
            JOptionPane.showMessageDialog(null, "No existen palindromos en este rango");
        }

        return listaPalindromos;
    }

    private boolean esPalindromo(int n){
        String original = String.valueOf(Math.abs(n));
        String reverso = new StringBuilder(original).reverse().toString();
        return original.equals(reverso);
    }
}
