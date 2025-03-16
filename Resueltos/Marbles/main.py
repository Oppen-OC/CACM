import math

# Algoritmo extendido de Euclides para encontrar x, y en la identidad de Bézout
def gcdExtended(a, b): 
    if a == 0: 
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def solve(n, c1, n1, c2, n2):
    g, x, y = gcdExtended(n1, n2)

    if n % g != 0:
        print("failed")
        return

    # Escalar la solución
    x *= n // g
    y *= n // g
    n1 //= g
    n2 //= g

    # Encontrar el rango válido de k
    minimo = math.ceil(-x / n2)
    maximo = math.floor(y / n1)

    if minimo > maximo:
        print("failed")
        return

    # Calcular los costos para ambos extremos
    res1 = c1 * (x + n2 * minimo) + c2 * (y - n1 * minimo)
    res2 = c1 * (x + n2 * maximo) + c2 * (y - n1 * maximo)

    # Seleccionar la solución con menor costo
    if res1 < res2:
        print(x + n2 * minimo, y - n1 * minimo)
    else:
        print(x + n2 * maximo, y - n1 * maximo)

def main():
    while True:
        n = int(input().strip())
        if n == 0:
            return
        c1, n1 = map(int, input().strip().split())
        c2, n2 = map(int, input().strip().split())

        solve(n, c1, n1, c2, n2)

if __name__ == "__main__":
    main()
