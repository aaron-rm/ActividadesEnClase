<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Soporte | La Universidad del Pueblo</title>
        <link rel="stylesheet" href="css/style.css">
    </head>
    <body class="body-soporte">
        <%@ include file="html/header.html" %>

        <h1 class="h1-soporte">Nuestro Equipo de Soporte</h1>
        <%
            List<Map<String, String>> equipo = new ArrayList<>();
            
            Map<String, String> m1 = new HashMap<>();
            m1.put("nombre", "Aaron Remarchuk"); m1.put("cedula", "8-1042-134"); m1.put("edad", "19"); m1.put("foto", "img/Aaron Remarchuk foto.png");
            equipo.add(m1);

        %>

        <div class="soporte-container">
            <% for(Map<String, String> miembro : equipo) { %>
                <div class="integrante-card">
                    <img src="<%= miembro.get("foto") %>" alt="Foto de <%= miembro.get("nombre") %>">
                    <h3><%= miembro.get("nombre") %></h3>
                    <p><strong>Cédula:</strong> <%= miembro.get("cedula") %></p>
                    <p><strong>Edad:</strong> <%= miembro.get("edad") %> años</p>
                </div>
            <% } %>
        </div>

        <%@ include file="html/footer.html" %>
    </body>
</html>