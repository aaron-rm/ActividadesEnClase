# Tic-Tac-Toe 3D 🎮

Proyecto semestral de Organización y Arquitectura de Computadoras. Juego sobre un cubo **4×4×4**: gana quien forme una línea de cuatro fichas en un eje, una diagonal de plano o una diagonal espacial.

## Estructura modular

| Archivo | Responsabilidad |
| --- | --- |
| [main.py](main.py) | Entrada: conecta menú, tablero, bot, conexión e interfaz. |
| [config.py](config.py) | Tamaño del tablero, textos y colores compartidos. |
| [logica.py](logica.py) | Estado y reglas de la partida en la clase `Tablero`. |
| [bot_ia.py](bot_ia.py) | Bot: intenta ganar, bloquear y elegir una casilla según su heurística. |
| [menu.py](menu.py) | Selección de modo y configuración de host o cliente con Tkinter. |
| [interfaz.py](interfaz.py) | Cubo Matplotlib, tableros por capa, controles y chat. |
| [red.py](red.py) | Sockets TCP, mensajes JSON, colas y descubrimiento UDP. |
| [ejecutar.bat](ejecutar.bat) | Lanzador de Windows desde la carpeta del proyecto. |
| [Documentación.docx](Documentaci%C3%B3n.docx) | Informe académico y tutorial del juego y de la conexión. |

## Ejecución

Desde esta carpeta, con Python 3 y Tkinter disponible:

```powershell
python -m pip install matplotlib
python main.py
```

En Windows también puedes abrir `ejecutar.bat`. El lanzador cambia a su propia carpeta antes de iniciar el programa.

## Modos y controles

- **2 Jugadores:** turnos en una misma computadora.
- **Contra la Computadora:** el bot juega como O.
- **Online:** un jugador aloja la partida y otro se conecta por una red accesible entre ambos equipos.

Juega haciendo clic en una casilla libre del cubo o en los tableros 2D por capa. La orientación del cubo se controla con el selector X/Y/Z y el deslizador de ángulo. **Reiniciar** vuelve a empezar la partida y sincroniza el reinicio en modo Online.

## Partidas en red

El tutorial de la entrega utiliza Radmin VPN para conectar ambos equipos a una misma red virtual. El programa intercambia directamente jugadas, reinicios y mensajes de chat; no utiliza un servidor central.

1. Conecta ambos equipos a la misma red local o virtual.
2. Un jugador elige **Online → Ser Host**; juega con X.
3. El otro elige **Online → Unirme a un Host**, selecciona una partida descubierta o introduce la IP y el puerto; juega con O.
4. Una vez conectados, juega en tu turno y utiliza el panel de chat para comunicarte.

El puerto predeterminado de juego es **TCP 5050**; el descubrimiento utiliza **UDP 5051**. La conexión requiere que esos puertos sean accesibles. Si el descubrimiento automático no encuentra una partida, utiliza la conexión manual por IP. La interfaz informa de las desconexiones.

La [versión en un solo archivo](../Tictactoe3d.py) se conserva en la carpeta de la asignatura.

[← Volver al portafolio](../../../readme.md)
