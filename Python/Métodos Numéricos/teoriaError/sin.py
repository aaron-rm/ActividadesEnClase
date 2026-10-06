import math

def taylor_sin(x, n):
    suma = 0
    for k in range(n + 1):
        # termino = (x ** k) / math.factorial(k)
        termino = ((-1) ** k) * (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
        suma += termino
    return suma

def sin():
    x = float(input("Punto a evaluar (en radianes): x="))
    n = int(input("Cantidad de iteraciones: n="))
    for n in range(n):
        aprox = taylor_sin(x, n)
        real = math.sin(x)
        error_abs = abs(real - aprox)
        error_rel = error_abs / abs(real) if real != 0 else 0

        print(f"n={n}")
        print(f"Aproximación = {aprox:.10f}")
        print(f"Valor real   = {real:.10f}")
        print(f"Error rel    = {error_rel:.10f}")
        print("-" * 40)
    pass

