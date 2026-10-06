<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Registro de Estudiante Completado</title>
        <link rel="stylesheet" href="css/style.css">
    </head>
    <body>
        <%@ include file="html/header.html" %>
        
        <%
            // Conexión a la base de datos
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conexion = DriverManager.getConnection("jdbc:mysql://localhost:3306/taller4", "root", "");
            Statement dbstatement = conexion.createStatement();

            // Recolección de datos básicos
            String nombre = request.getParameter("nombre").toUpperCase();
            String cedula = request.getParameter("cedula").toUpperCase();
            int anio = Integer.parseInt(request.getParameter("anio"));
            String centro = request.getParameter("centro_regional").toUpperCase();
            float indice = Float.parseFloat(request.getParameter("indice"));

            // Recolección de múltiples cursos (checkboxes)
            String[] cursosSeleccionados = request.getParameterValues("cursos");
            String cursosString = "";
            
            if (cursosSeleccionados != null) {
                cursosString = String.join(", ", cursosSeleccionados);
            } else {
                cursosString = "Ninguno";
            }

            // Inserción en la base de datos
            String insertQuery = "INSERT INTO estudiante (nombre, cedula, anio, centroEDU, indice, cursos) VALUES ('" 
                     + nombre + "', '" 
                     + cedula + "', " 
                     + anio + ", '" 
                     + centro + "', " 
                     + indice + ", '" 
                     + cursosString + "')";
            
            dbstatement.executeUpdate(insertQuery);
            dbstatement.close();
            conexion.close();
        %>

        <section class="registro-exitoso">
            <h1>Registro Exitoso</h1>
            
            <main class="registro-info">
                <div class="info">
                    <h2>Datos del Estudiante:</h2>
                    <p><strong>Nombre:</strong> <%= nombre %></p>
                    <p><strong>Cédula:</strong> <%= cedula %></p>
                    <p><strong>Año lectivo:</strong> <%= anio %></p>
                    <p><strong>Centro Regional:</strong> <%= centro %></p>
                    <p><strong>Cursos elegidos:</strong> <%= cursosString %></p>
                    <p><strong>Índice Académico:</strong> <%= indice %></p>
                </div>
            </main>

            <div class="registro-volver">
                <a href="HOME.jsp">Volver al inicio</a>
            </div>
        </section>

        <%@ include file="html/footer.html" %>
    </body>
</html>