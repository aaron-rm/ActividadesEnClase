from typing import List, Set, Dict
import re, random, time, tracemalloc
import matplotlib.pyplot as plt

# Definición de tipo para mayor claridad
Matrix = List[List[float]]

class EntradaDatos:
    def leer_datos(self):
        while True:
            try:
                print("\n--- 1. RELLENAR DATOS ---")
                n = int(input("   Ingrese el numero total de puntos (incluyendo el deposito): "))
                if n <= 1:
                    print("   El numero de puntos debe ser mayor que 1.")
                    continue

                cap = int(input("   Ingrese la capacidad maxima de paquetes por conductor: "))
                if cap <= 0:
                    print("   La capacidad debe ser positiva.")
                    continue

                P = int(input("   Ingrese el total de paquetes a repartir: "))
                if P <= 0:
                    print("   El total de paquetes debe ser positivo.")
                    continue

                break
            except ValueError:
                print("      Error: Debe ingresar solo numeros enteros validos. Intente de nuevo.\n")
                1
        print(f"\n   Datos ingresados correctamente:")
        print(f"   → Numero de puntos: {n}")
        print(f"   → Capacidad por conductor: {cap}")
        print(f"   → Total de paquetes: {P}\n")
        return n, cap, P

    def leer_matriz_distancias(self, n):
        print("   A continuacion, ingrese las distancias en kilometros (solo la mitad superior).")
        matriz = [[0.0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                while True:
                    try:
                        distancia = float(input(f"      Distancia entre punto {i} y punto {j}: "))
                        if distancia < 0:
                            print("         Error: La distancia no puede ser negativa. Intente de nuevo.\n")
                        else:
                            matriz[i][j] = distancia
                            matriz[j][i] = distancia
                            break
                    except ValueError:
                        print("         Error: Debe ingresar un numero válido.\n")
        return matriz

    def generar_matriz_aleatoria(self, n):
        matriz = [[0.0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                valor = float(random.randint(5, 100))
                matriz[i][j] = valor
                matriz[j][i] = valor
        return matriz

    def mostrar_matriz(self, matriz):
        n = len(matriz)
        print("\n   De/A |", end="")
        for j in range(n):
            print(f" {j:5}", end="")
        print("\n   " + "-" * (7 + 6 * n))
        for i in range(n):
            print(f"     {i:2} |", end="")
            for j in range(n):
                print(f" {matriz[i][j]:5.1f}", end="")
            print()

    # --- INICIO DE LOS MÉTODOS MEJORADOS (BASADOS EN TU GUÍA) ---
    
    def leer_opcion_menu(self) -> str:
        """Lee la opción del submenú del editor de forma robusta."""
        while True:
            raw = input("   Seleccione una opción: ").strip().lower()
            if raw in {"1", "editar", "e"}:
                return "1"
            if raw in {"0", "salir", "s"}:
                return "0"
            print("      Error: Opción no válida. Ingrese 1 (Editar) o 0 (Salir).\n")

    def leer_indice(self, msg: str, n: int) -> int:
        """Lee un índice de fila/columna de forma robusta."""
        while True:
            raw = input(f"      Ingrese {msg} (0 a {n-1}) o 'x' para cancelar: ").strip().lower()
            if raw == "x":
                return -1
            try:
                k = int(raw)
                if 0 <= k < n:
                    return k
                else:
                    print(f"      Error: Índice fuera de rango. Debe estar entre 0 y {n-1}.\n")
            except ValueError:
                print("      Error: Entrada no válida, se requiere un número entero.\n")

    def leer_distancia(self) -> float:
        """Lee un nuevo valor de distancia de forma robusta."""
        while True:
            raw = input(f"      Ingrese el nuevo valor de distancia (>= 0) o 'x' para cancelar: ").strip().lower()
            if raw == "x":
                return -1.0
            try:
                v = float(raw)
                if v < 0:
                    print("         Error: La distancia no puede ser negativa. Inténtelo de nuevo.\n")
                    continue
                return v
            except ValueError:
                print("         Error: Entrada no válida, se requiere un número. Inténtelo de nuevo.\n")

    def editar_matriz(self, M: Matrix) -> Matrix:
        """
        Editor interactivo que permite al usuario modificar valores de la matriz.
        """
        n = len(M)
        while True:
            self.mostrar_matriz(M)
            print("\n   --- Editor de Matriz ---")
            print("      1) Editar un valor")
            print("      0) Guardar y Salir del editor")
            
            # Se usan los nuevos métodos robustos con self.
            opcion = self.leer_opcion_menu()

            if opcion == "0":
                print("   Saliendo del editor...")
                break

            i = self.leer_indice("la Fila", n)
            if i == -1:
                print("         Edición cancelada.\n")
                continue

            j = self.leer_indice("la Columna", n)
            if j == -1:
                print("         Edición cancelada.\n")
                continue

            if i == j:
                print("         Error: La diagonal principal debe ser 0. No se permite editar.\n")
                continue

            nuevo = self.leer_distancia()
            if nuevo < 0:
                print("         Edición cancelada.\n")
                continue

            M[i][j] = float(nuevo)
            M[j][i] = float(nuevo) # Mantener la simetría
            print("         ¡Valor actualizado correctamente!\n")
        return M

class DistribuidorPaquetes:
    """
    Módulo 4: Distribución de Paquetes por Conductor
    Walter Gonzalez
    """
    
    @staticmethod
    def asignar_paquetes(total_paquetes: int, capacidad: int) -> List[int]:
        """
        Divide los paquetes entre conductores según la capacidad máxima.
        Si sobran paquetes, los asigna al último conductor.
        
        Complejidad: O(k) donde k = total_paquetes / capacidad
        """
        paquetes_por_conductor = []
        paquetes_restantes = total_paquetes
        
        while paquetes_restantes > 0:
            if paquetes_restantes >= capacidad:
                paquetes_por_conductor.append(capacidad)
                paquetes_restantes -= capacidad
            else:
                paquetes_por_conductor.append(paquetes_restantes)
                paquetes_restantes = 0
        
        return paquetes_por_conductor
    
    @staticmethod
    def calcular_num_conductores(total_paquetes: int, capacidad: int) -> int:
        """Calcula el número de conductores necesarios"""
        if total_paquetes % capacidad == 0:
            return total_paquetes // capacidad
        else:
            return (total_paquetes // capacidad) + 1

class AsignadorRutas:
    """
    Módulos 5 y 6: Asignación y Optimización de Rutas
    Eliber Oropeza y Aaron Remarchuk
    """
    
    def __init__(self):
        self.puntos_visitados = set()
        self.depot = 0  # Punto de partida (almacén)
    
    def asignar_rutas(self, n_puntos: int, paquetes_por_conductor: List[int], 
                     matriz: List[List[int]]) -> List[List[int]]:
        """
        Asigna rutas a cada conductor usando estrategia del vecino más cercano.
        
        Complejidad: O(k * n²) donde k = número de conductores
        """
        rutas = []
        self.puntos_visitados.clear()
        
        for num_paquetes in paquetes_por_conductor:
            ruta = self._asignar_ruta_conductor(n_puntos, num_paquetes, matriz)
            rutas.append(ruta)
        
        return rutas
    
    def _asignar_ruta_conductor(self, n_puntos: int, num_paquetes: int,
                               matriz: List[List[int]]) -> List[int]:
        """
        Asigna una ruta a un conductor específico.
        
        Complejidad: O(n²)
        """
        ruta = [self.depot]
        actual = self.depot
        puntos_asignados = 0
        
        while puntos_asignados < num_paquetes:
            mejor_punto = self._encontrar_punto_mas_cercano(actual, n_puntos, matriz)
            
            if mejor_punto == -1:
                # Si no hay más puntos, generar nuevos disponibles
                mejor_punto = self._encontrar_punto_disponible(n_puntos)
                if mejor_punto == -1:
                    break
            
            if mejor_punto != -1:
                ruta.append(mejor_punto)
                self.puntos_visitados.add(mejor_punto)
                actual = mejor_punto
                puntos_asignados += 1
        
        # Regresar al depósito
        ruta.append(self.depot)
        return ruta
    
    def _encontrar_punto_mas_cercano(self, actual: int, n_puntos: int,
                                   matriz: List[List[int]]) -> int:
        """
        Encuentra el punto no visitado más cercano.
        
        Complejidad: O(n)
        """
        min_distancia = float('inf')
        mejor_punto = -1
        
        for i in range(1, n_puntos):  # Empezar desde 1 (el 0 es el depot)
            if i not in self.puntos_visitados and matriz[actual][i] < min_distancia:
                min_distancia = matriz[actual][i]
                mejor_punto = i
        
        return mejor_punto
    
    def _encontrar_punto_disponible(self, n_puntos: int) -> int:
        """
        Encuentra cualquier punto disponible no visitado.
        
        Complejidad: O(n)
        """
        for i in range(1, n_puntos):
            if i not in self.puntos_visitados:
                return i
        return -1

class CalculadorMetricas:
    """
    Módulo 7: Cálculo de Métricas (distancia y tiempo)
    Kahil Reyna
    """
    
    @staticmethod
    def calcular_distancia_ruta(ruta: List[int], matriz: List[List[int]]) -> int:
        """
        Calcula la distancia total de una ruta.
        
        Complejidad: O(m) donde m = longitud de la ruta
        """
        distancia_total = 0
        for i in range(len(ruta) - 1):
            distancia_total += matriz[ruta[i]][ruta[i + 1]]
        return distancia_total
    
    @staticmethod
    def calcular_tiempo_ruta(distancia: int, velocidad_promedio: int = 1) -> int:
        """
        Calcula el tiempo estimado de una ruta.
        Asume que cada unidad de distancia = 1 minuto
        """
        return distancia * velocidad_promedio
    
    def calcular_metricas_globales(self, rutas: List[List[int]], 
                                 paquetes_por_conductor: List[int],
                                 matriz: List[List[int]]) -> Dict:
        """
        Calcula métricas globales del sistema.
        
        Complejidad: O(k * m) donde k = conductores, m = longitud promedio de ruta
        """
        if not rutas:
            return {}
        
        distancias = []
        tiempos = []
        
        for ruta in rutas:
            dist = self.calcular_distancia_ruta(ruta, matriz)
            distancias.append(dist)
            tiempos.append(self.calcular_tiempo_ruta(dist))
        
        return {
            'distancia_total': sum(distancias),
            'distancia_promedio': sum(distancias) / len(distancias),
            'tiempo_total': sum(tiempos),
            'tiempo_promedio': sum(tiempos) / len(tiempos),
            'num_conductores': len(rutas),
            'distancias': distancias,
            'tiempos': tiempos,
            'paquetes_totales': sum(paquetes_por_conductor)
        }

class AnalizadorComplejidad:
    def analisis_empirico(self, n_valores: List[int]) -> List[Dict]:
        distribuidor = DistribuidorPaquetes()
        asignador = AsignadorRutas()
        calculador = CalculadorMetricas()
        entrada_temp = EntradaDatos()
        
        print("\n" + "="*70)
        print("ANÁLISIS EMPÍRICO DE COMPLEJIDAD")
        print("="*70)
        
        resultados = []
        
        for n in n_valores:
            print(f"Probando con n = {n} puntos...")
            
            # Generar datos de prueba consistentes
            matriz = entrada_temp.generar_matriz_aleatoria(n)
            capacidad = 10  # Usar valores fijos para un análisis consistente
            total_paquetes = n - 1 # Un paquete por cada punto de entrega
            
            # Medir tiempo y memoria
            tracemalloc.start()
            inicio = time.time()
            
            paquetes_por_conductor = distribuidor.asignar_paquetes(total_paquetes, capacidad)
            rutas = asignador.asignar_rutas(n, paquetes_por_conductor, matriz)
            metricas = calculador.calcular_metricas_globales(rutas, paquetes_por_conductor, matriz)
            
            fin = time.time()
            memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            tiempo_ejecucion_ms = (fin - inicio) * 1000
            memoria_pico_mb = memoria_pico / (1024 * 1024)
            
            resultados.append({
                'n': n,
                'tiempo_ms': tiempo_ejecucion_ms,
                'memoria_mb': memoria_pico_mb
            })
            
            print(f"  → Tiempo: {tiempo_ejecucion_ms:.2f} ms | Memoria pico: {memoria_pico_mb:.4f} MB")
        
        self._mostrar_tabla_resultados(resultados)
        return resultados
    
    def _mostrar_tabla_resultados(self, resultados: List[Dict]):
        """Muestra una tabla de resumen con los resultados del análisis."""
        print("\n" + "="*50)
        print("TABLA DE RESULTADOS - ANÁLISIS EMPÍRICO")
        print("="*50)
        print(f"{'n':>10} {'Tiempo (ms)':>20} {'Memoria (MB)':>20}")
        print("-" * 50)
        
        for r in resultados:
            print(f"{r['n']:>10} {r['tiempo_ms']:>20.2f} {r['memoria_mb']:>20.4f}")

    # <-- NUEVO MÉTODO para las gráficas
    def mostrar_graficas(self, resultados_analisis: List[Dict]):


        print("\nGenerando gráficas de complejidad...")
        n_valores = [r['n'] for r in resultados_analisis]
        tiempos_ms = [r['tiempo_ms'] for r in resultados_analisis]
        memorias_mb = [r['memoria_mb'] for r in resultados_analisis]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        fig.suptitle('Análisis Empírico de Complejidad', fontsize=16)

        ax1.plot(n_valores, tiempos_ms, marker='o', color='b')
        ax1.set_title('Complejidad Temporal')
        ax1.set_xlabel('Tamaño de Entrada (n)')
        ax1.set_ylabel('Tiempo de Ejecución (ms)')
        ax1.grid(True, which="both", ls="--")
        ax1.set_xscale('log')
        ax1.set_yscale('log')

        ax2.plot(n_valores, memorias_mb, marker='s', color='r')
        ax2.set_title('Complejidad Espacial')
        ax2.set_xlabel('Tamaño de Entrada (n)')
        ax2.set_ylabel('Uso de Memoria (MB)')
        ax2.grid(True, which="both", ls="--")
        ax2.set_xscale('log')
        ax2.set_yscale('log')
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        print("Mostrando gráficas... Cierra la ventana para continuar.")
        plt.show()

class VisualizadorResultados:
    """
    Módulo 8: Visualización de Resultados
    Mijael Vallejos
    """
    
    def __init__(self):
        self.calculador = CalculadorMetricas() # <--- ¡YA NO NECESITAS EL PUNTO!
    
    def mostrar_resultados(self, rutas: List[List[int]], 
                         paquetes_por_conductor: List[int],
                         matriz: List[List[int]]):
        """
        Muestra los resultados de forma ordenada.
        
        Complejidad: O(k * m) donde k = conductores, m = longitud promedio de ruta
        """
        print("\n" + "="*70)
        print("RESULTADOS DE ASIGNACIÓN DE RUTAS")
        print("="*70)
        
        for i, ruta in enumerate(rutas, 1):
            distancia = self.calculador.calcular_distancia_ruta(ruta, matriz)
            tiempo = self.calculador.calcular_tiempo_ruta(distancia)
            
            print(f"\nCONDUCTOR {i}:")
            print(f"  Ruta: {' → '.join(map(str, ruta))}")
            print(f"  Distancia total: {distancia} km")
            print(f"  Paquetes transportados: {paquetes_por_conductor[i-1]}")
            print(f"  Tiempo estimado: {tiempo} minutos")
        
        self._mostrar_resumen_global(rutas, paquetes_por_conductor, matriz)
    
    def _mostrar_resumen_global(self, rutas: List[List[int]],
                              paquetes_por_conductor: List[int],
                              matriz: List[List[int]]):
        """Muestra el resumen global del sistema"""
        metricas = self.calculador.calcular_metricas_globales(
            rutas, paquetes_por_conductor, matriz
        )
        
        print("\n" + "="*70)
        print("RESUMEN GLOBAL DEL SISTEMA")
        print("="*70)
        print(f"Total de conductores: {metricas['num_conductores']}")
        print(f"Total de paquetes entregados: {metricas['paquetes_totales']}")
        print(f"Distancia total recorrida: {metricas['distancia_total']} km")
        print(f"Distancia promedio por conductor: {metricas['distancia_promedio']:.2f} km")
        print(f"Tiempo total estimado: {metricas['tiempo_total']} minutos")
        print(f"Tiempo promedio por conductor: {metricas['tiempo_promedio']:.2f} minutos")
        
        print(f"\nDistribución de paquetes: {paquetes_por_conductor}")

def menu():
    # Inicializar objetos de las clases
    entrada = EntradaDatos()
    distribuidor = DistribuidorPaquetes()
    asignador = AsignadorRutas()
    visualizador = VisualizadorResultados()
    analizador = AnalizadorComplejidad()
    
    # Variables para guardar datos entre opciones
    n, cap, P = 0, 0, 0
    matriz = []
    resultados_analisis = [] # Para guardar los datos del análisis
    
    while True:
        print("\n" + "="*60)
        print("SISTEMA DE RUTAS DE ENTREGA - MENÚ PRINCIPAL")
        print("="*60)
        print("  1) Rellenar datos (Puntos, Capacidad, Matriz)")
        print("  2) Mostrar resultados de rutas")
        print("  3) Realizar análisis empírico y ver tabla")
        print("  4) Mostrar gráficas del análisis")
        print("  5) Salir")
        print("="*60)
    
        try:
            opcion = int(input("\nSeleccione una opción (1-5): "))
        except ValueError:
            print("  Error: Debe ingresar un número válido. Intente de nuevo.\n")
            continue  
        
        if opcion == 1:
            n, cap, P = entrada.leer_datos()
            
            # <--- INICIO DEL CAMBIO: SE RESTAURA EL SUBMENÚ DE GENERACIÓN ---
            print("\nMétodos de generación de matriz:")
            print("  1) Entrada manual")
            print("  2) Generación aleatoria")
            
            # Bucle para asegurar que el usuario elija una opción válida
            while True:
                try:
                    opcion_gen = int(input("Seleccione un método (1/2): "))
                    if opcion_gen == 1:
                        matriz = entrada.leer_matriz_distancias(n)
                        break
                    elif opcion_gen == 2:
                        matriz = entrada.generar_matriz_aleatoria(n)
                        break
                    else:
                        print("  Error: Opción no válida. Por favor, ingrese 1 o 2.")
                        continue
                except ValueError:
                    print("  Error: Debe ingresar un número válido (1 o 2).")
                    continue

            print("\nMatriz de distancias actual:")
            entrada.mostrar_matriz(matriz)

            # Bucle para asegurar que el usuario elija una opción válida
            while True:
                try:
                    opcion_gen = input("\n¿Desea editar la matriz? (si/no): ").lower()
                    if opcion_gen == 'si':
                        matriz = entrada.editar_matriz(matriz)
                        break
                    elif opcion_gen == 'no':
                        break
                    else:
                        print("  Error: Opción no válida. Por favor, ingrese si o no.")
                        continue
                except ValueError:
                    print("  Error: Debe ingresar una opción válida.")
                    continue
        
        elif opcion == 2:
            if not matriz:
                print("\n  Error: Primero debe rellenar los datos en la Opción 1.")
                continue
            
            print("\n--- 2. MOSTRANDO RESULTADOS DE RUTAS ---")
            paquetes = distribuidor.asignar_paquetes(P, cap)
            rutas = asignador.asignar_rutas(n, paquetes, matriz)
            visualizador.mostrar_resultados(rutas, paquetes, matriz)

        elif opcion == 3:
            print("\n--- 3. REALIZANDO ANÁLISIS EMPÍRICO ---")
            print("Esto puede tardar unos momentos...")
            n_valores = [50, 100, 500, 1000, 2000, 3000]
            resultados_analisis = analizador.analisis_empirico(n_valores)
            print("\nAnálisis completado. Puede ver las gráficas en la opción 4.")

        elif opcion == 4:
            if not resultados_analisis:
                print("\n  Error: Primero debe ejecutar la Opción 3.")
                continue
            print("\n--- 4. MOSTRANDO GRÁFICAS DEL ANÁLISIS ---")
            analizador.mostrar_graficas(resultados_analisis)

        elif opcion == 5:
            print("\nSaliendo del programa... ¡Hasta luego!")
            break
            
        else:
            print("   Error: Opción no válida. Intente nuevamente.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    menu()