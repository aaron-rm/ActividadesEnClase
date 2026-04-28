package Problema1;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            System.out.print("La fecha de hoy: ");
            String fecha = br.readLine();
            System.out.print("Digite el precio del producto: ");
            double precio = Double.parseDouble(br.readLine());

            Factura f = new Factura(fecha, precio);
            f.generarResumen();

            System.out.print("Desea ver mas detalles?: ");
            String verDetalles = br.readLine();
            if(verDetalles.equals("si")){
                DetalleFactura d = new DetalleFactura(f);
                d.generarResumen();
            }

        }catch (Exception e){
            System.err.println("No se puede realizar la operacion");
        }



    }
}
