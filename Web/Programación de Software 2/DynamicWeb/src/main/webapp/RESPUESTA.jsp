<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@ page import="java.sql.*" %>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Fin del Formulario</title>
        <link rel="stylesheet" href="CSS/style.css">
        <link rel="stylesheet" href="CSS/form.css">
        <link rel="stylesheet" href="CSS/resp.css">
    </head>
    <body>
        <%
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conexion = DriverManager.getConnection("jdbc:mysql://localhost:3306/prueba1", "root", "");
            Statement dbstatement = conexion.createStatement();
        %>
        <header>
            <h1>Gracias por su participación</h1>
        </header>
        <main>
            <% 
                String nombre = request.getParameter("nombre");
                if(nombre.equals("")){
                    nombre = "Sin Nombre";
                }
                String direccion = request.getParameter("direccion");
                if(direccion.equals("")){
                    direccion = "Sin Dirección";
                }
                String contrasenia = request.getParameter("contrasenia");
                if(contrasenia.equals("")){
                    contrasenia = "Sin Contraseña";
                }
                String provincia = request.getParameter("provincia");
                String[] herramientas = request.getParameterValues("herramientas");
                String herramientasConcatenadas = "";
                if(herramientas == null){
                    herramientas = new String[1];
                    herramientas[0] = "Sin Herramientas";
                    herramientasConcatenadas = herramientas[0];
                } else {
                    for(int i = 0; i < herramientas.length; i++){
                        herramientasConcatenadas += herramientas[i] + ",";
                    }
                }
                
                String insertQuery = "INSERT INTO usuario (nombre, direccion, contrasenia, provincia, herramientas) VALUES ('" + nombre + "', '" + direccion + "', '" + contrasenia + "', '" + provincia + "','" + herramientasConcatenadas + "')";
                dbstatement.executeUpdate(insertQuery);
                dbstatement.close();
            %>
            
            <div class="info">
                <h1><%= nombre %></h1>
                <p>Dirección: <%= direccion %></p>
                <p>Contraseña: <%= contrasenia %></p>
                <p>Provincia: <%= provincia %></p>
                <p>Herramientas:</p>
                <ul>
                <% 
                    for(int i = 0; i < herramientas.length; i++){
                        out.println("<li>" + herramientas[i] + "</li>");
                    }
                %>
                </ul>
            </div>
        </main>  
        <footer>
            <a href="HOME.html">Volver a Inicio</a>
            <a href="REGISTRO.html">Volver a Registro</a>
        </footer>
    </body>
</html>