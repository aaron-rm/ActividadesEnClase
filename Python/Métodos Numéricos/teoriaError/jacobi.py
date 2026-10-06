import numpy as np

# ============================================
# Función para truncar (sin redondear)
# ============================================
def truncar(valor, decimales):
    factor = 10 ** decimales
    return int(valor * factor) / factor

# ============================================
# Método de Jacobi
# ============================================
def jacobi_simple(A, b, x0, tol, max_iter, decimales):
    n = len(A)
    x_old = np.array(x0, dtype=float)

    print("\nIter | Valores aproximados | Error (%)")
    print("--------------------------------------------------")

    for k in range(1, max_iter + 1):
        x_new = np.zeros(n)
        for i in range(n):
            suma = 0
            for j in range(n):
                if j != i:
                    suma += A[i][j] * x_old[j]
            valor = (b[i] - suma) / A[i][i]
            x_new[i] = truncar(valor, decimales)

        error_max = 0
        for i in range(n):
            if x_new[i] != 0:
                error = abs((x_new[i] - x_old[i]) / x_new[i]) * 100
            else:
                error = abs(x_new[i] - x_old[i]) * 100

            if error > error_max:
                error_max = error

        print(f"{k:>4} | {x_new} | {error_max:.4f}")

        if error_max < tol:
            print("\nConvergió")
            return x_new

        x_old = x_new.copy()

    print("\nNo convergió en el máximo de iteraciones")
    return x_new

### MAIN ---- Programa Principal
def jacobi():
    # 1. Definir tamaño de la matriz
    n = int(input("Ingrese el tamaño de la matriz (n x n): "))

    # 2. Inicializar matriz A y vector b
    A = []
    print("\n--- Ingrese los valores de la matriz de coeficientes A ---")
    for i in range(n):
        fila = []
        for j in range(n):
            valor = float(input(f"Elemento A[{i+1}][{j+1}]: "))
            fila.append(valor)
        A.append(fila)

    b = []
    print("\n--- Ingrese los valores del vector de resultados b ---")
    for i in range(n):
        valor = float(input(f"Elemento b[{i+1}]: "))
        b.append(valor)

    # 3. Vector inicial (opcional: podrías pedirlo también por input)
    x0 = [0] * n 

    # 4. Parámetros de control
    tolerancia = float(input("\nIngrese el % de tolerancia (ej. 0.01): "))
    max_it = int(input("Ingrese el máximo de iteraciones: "))
    dec = int(input("Ingrese la cantidad de decimales para truncar: "))

    # Ejecución
    sol = jacobi_simple(A, b, x0, tol=tolerancia, max_iter=max_it, decimales=dec)

    print("\nSolución aproximada final:")
    print(sol)
