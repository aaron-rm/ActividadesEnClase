import numpy as np

# ============================================
# Función para truncar (sin redondear)
# ============================================
def truncar(valor, decimales):
    factor = 10 ** decimales
    return int(valor * factor) / factor

# ============================================
# Método de Gauss-Seidel
# ============================================
def gauss_seidel(A, b, x0, tol, max_iter, decimales):
    n = len(A)
    x = np.array(x0, dtype=float)

    print("\nIter | Valores aproximados | Error (%)")
    print("--------------------------------------------------")

    for k in range(1, max_iter + 1):
        x_old = x.copy()
        for i in range(n):
            suma = 0
            for j in range(n):
                if j != i:
                    # Gauss-Seidel usa el valor de x[j] más reciente
                    suma += A[i][j] * x[j]
            
            valor = (b[i] - suma) / A[i][i]
            x[i] = truncar(valor, decimales)

        # Calcular error máximo
        error_max = 0
        for i in range(n):
            if x[i] != 0:
                error = abs((x[i] - x_old[i]) / x[i]) * 100
            else:
                error = abs(x[i] - x_old[i]) * 100

            if error > error_max:
                error_max = error

        # Mostrar resultados con formato
        print(f"{k:>4} | {x} | {error_max:.4f}")

        # Verificar convergencia
        if error_max < tol:
            print("\nConvergió")
            return x

    print("\nNo convergió en el máximo de iteraciones")
    return x

### MAIN ---- Programa Principal
def gaussSeidel():
    # 1. Definir tamaño del sistema
    n = int(input("Ingrese el tamaño de la matriz (n x n): "))

    # 2. Inicializar matriz A y vector b
    A = np.zeros((n, n))
    print("\n--- Ingrese los coeficientes de la matriz A ---")
    for i in range(n):
        for j in range(n):
            A[i, j] = float(input(f"A[{i+1}][{j+1}]: "))

    b = np.zeros(n)
    print("\n--- Ingrese los valores del vector b ---")
    for i in range(n):
        b[i] = float(input(f"b[{i+1}]: "))

    # 3. Parámetros adicionales
    # Creamos x0 automáticamente como ceros
    x0 = np.zeros(n)

    tol_input = float(input("\nIngrese el % de tolerancia (ej. 0.01): "))
    max_it = int(input("Ingrese el máximo de iteraciones: "))
    dec = int(input("Ingrese la cantidad de decimales para truncar: "))

    # 4. Ejecución del método
    sol = gauss_seidel(A, b, x0, tol=tol_input, max_iter=max_it, decimales=dec)

    print("\nSolución aproximada final:")
    print(sol)
