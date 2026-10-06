<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*, java.time.*, java.time.format.DateTimeFormatter" %>
<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calendario de Actividades | La Universidad del Pueblo</title>
        <link rel="stylesheet" href="css/style.css">
    </head>
    <body>
        <%@ include file="html/header.html" %>

        <h2>Calendario de Actividades - Junio</h2>
        <%
            // 1. Configuración de fechas
            YearMonth ym = YearMonth.now(); // Mes actual
            int diasEnMes = ym.lengthOfMonth();
            
            // 2. Obtener eventos de la DB y guardarlos en un Mapa para acceso rápido
            // Usaremos un Map<String, List<String>> donde la llave es la fecha "yyyy-MM-dd"
            java.util.Map<String, java.util.List<String>> eventosPorDia = new java.util.HashMap<>();
            
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conexion = DriverManager.getConnection("jdbc:mysql://localhost:3306/taller4", "root", "");
            Statement st = conexion.createStatement();
            String sql = "SELECT fecha, horario, 'Programación' as materia FROM programacion " +
                        "UNION SELECT fecha, horario, 'Soldadura' as materia FROM soldadura " +
                        "UNION SELECT fecha, horario, 'Electrónica' as materia FROM electronica";
            ResultSet rs = st.executeQuery(sql);
            
            while(rs.next()){
                String fecha = rs.getString("fecha");
                String detalle = rs.getString("materia") + ": " + rs.getString("horario");
                eventosPorDia.computeIfAbsent(fecha, k -> new java.util.ArrayList<>()).add(detalle);
            }
            conexion.close();
        %>

        <div class="calendar-grid">
            <div>Lunes</div><div>Martes</div><div>Miércoles</div><div>Jueves</div><div>Viernes</div><div>Sábado</div><div>Domingo</div>
            
            <%
                // 3. Iterar por cada día del mes
                for (int i = 1; i <= diasEnMes; i++) {
                    LocalDate fechaActual = ym.atDay(i);
                    String fechaStr = fechaActual.toString(); // Formato yyyy-MM-dd
            %>
                    <div class="day-box">
                        <strong><%= i %></strong>
                        <% 
                            // 4. Si hay eventos para este día, los mostramos
                            if (eventosPorDia.containsKey(fechaStr)) {
                                for (String evento : eventosPorDia.get(fechaStr)) {
                        %>
                                    <a href="ESTUDIANTES.jsp"><div class="activity"><%= evento %></div></a>
                        <% 
                                }
                            }
                        %>
                    </div>
            <%
                }
            %>
        </div>
        

        <%@ include file="html/footer.html" %>
    </body>
</html>