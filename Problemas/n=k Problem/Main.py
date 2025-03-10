import math

def fun(k):
    n = 1
    while True:
        S_n = n * (n + 1) / 2
        if S_n >= k and (S_n - k) % 2 == 0:
            return n
        n += 1


def main():
    cases = int(input())
    for _ in range(0,cases):
        input()
        k = int(math.fabs(int(input())))
        print(fun(k))
        print()

            
    
if __name__ == "__main__":
    main()
    
    # Buscamos obtener la n mas pequeña con la que se puede obtener k 
    # n = numero de casos de prueba
    # k = número objetivo