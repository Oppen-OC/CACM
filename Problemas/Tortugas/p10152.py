import sys
import math

def stack_it(lista, elemento):
    lista.remove(elemento)
    lista.insert(0, elemento)
    return lista


def resolver(n, ini, fin):  
    # Identificar el sufijo correcto más largo en ini
    pointer = 0
    for i in range(n-1, -1, -1):
        if ini[i] != fin[i]:
            pointer = i+1
            break
        
    # Subset de tortugas a mover
    actual = [(x, ini[x]) for x in range(0, pointer)] 
    final =  [(x, fin[x]) for x in range(0, pointer)]
    
    actual = ini[:pointer]
    final = fin[:pointer]
    
    
    aux = [actual[i] == final[i] for i in range(0, pointer)]
    
    for i in range(pointer-1, -1, -1):  # Iterate backwards from n-1 to 0:
        while(aux[i] == False):
            if actual[i] != final[i]:
                print(actual[i])
                actual = stack_it(actual, actual[i])
                aux = [actual[i] == final[i] for i in range(0, pointer)]
    print("\n")

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