import math

def taylor_cos(x, n):
    suma = 0
    for k in range(n + 1):
        # La fórmula del coseno usa potencias pares (2k) y alterna signos
        termino = ((-1) ** k) * (x ** (2 * k)) / math.factorial(2 * k)
        suma += termino
    return suma

def cos():
    x = float(input("Punto a evaluar (en radianes): x="))
    n = int(input("Cantidad de iteraciones: n="))
    for n in range(n):
        aprox = taylor_cos(x, n)
        real = math.cos(x)
        error_abs = abs(real - aprox)
        error_rel = error_abs / abs(real) if real != 0 else 0

        print(f"n={n}")
        print(f"Aproximación = {aprox:.10f}")
        print(f"Valor real   = {real:.10f}")
        print(f"Error rel    = {error_rel:.10f}")
        print("-" * 40)
    pass