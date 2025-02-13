import sys
import math

def resolver(n, ini, fin):
    inicial = [(x, ini[x]) for x in range(0, len(ini))]
    final = [(x, fin[x]) for x in range(0, len(fin))]
    print(inicial)
    print(final)

def fun():
    lines = sys.stdin.read().strip().split("\n")
    pointer = 1
    for k in range (0, int(lines[0])):
        n = int(lines[pointer]) # Tamaño de cada stack
        size = n*2 + 1          # Tamaño del caso de prueba

        original = [0]*n
        final = [0]*n

        for aux in range (0, size-1):
            if aux <= math.floor(size/2) -1:
                original[aux] = lines[aux + pointer +1]
            else:
                final[aux - math.floor(size/2) -1] = lines[aux + pointer]
                
        pointer += size         # Apunta al final del stack
        resolver(n, original, final)

def main():
    fun()
    
if __name__ == "__main__":
    main()  
    
    # Numero de casos de prueba K 
    # Tamaño de stack n
    # Orden original de las tortugas (n posiciones)