import sys
import math
# import numpy as np

def replace_inter(from_idx, to_idx, queue, turtles_map):
    print("replace_inter: ", from_idx, to_idx, queue, turtles_map)
    
    # Create a list with the turtles to be replaced and their target positions
    replace = [(turtle, turtles_map[turtle]) for turtle in queue[from_idx : to_idx + 1]]
    # Sort the list by the target positions (from last to first)
    replace = sorted(replace, key = lambda x: x[1], reverse = True)
    
    # Replace the turtles in the queue
    new_queue = queue.copy()
    pointer = 0
    
    # Add the replaced turtles
    for turtle, _ in replace:
        print(new_queue, pointer, '\n')
        new_queue[pointer] = turtle
        pointer += 1
    
        
    # Add the remaining turtles
    for idx in range(0, from_idx):
        print(new_queue, pointer, '\n')
        new_queue[pointer] = queue[idx]
        pointer += 1
        
    for idx in range(to_idx + 1, len(queue)):
        print(new_queue, pointer, '\n')
        new_queue[pointer] = queue[idx]
        pointer += 1
        
    return new_queue
    

def resolver(n, ini, fin):
    # Map turtle names to their target positions
    turtles_map = {}
    for idx in range(n):
        turtles_map[fin[idx]] = idx
        
    for idx in range(n - 1, -1, -1):
        if ini[idx] != fin[idx]:
            elem_idx = ini.index(fin[idx])
            ini = replace_inter(elem_idx + 1, idx, fin, turtles_map)
            
    print(ini)
        

def fun():
    lines = sys.stdin.read().strip().split("\n")
    pointer = 1
    
    for k in range (0, int(lines[0])):
        n = int(lines[pointer]) # Tamaño de cada stack
        size = n*2 + 1          # Tamaño del caso de prueba

        original = [0] * n # np.empty(n, dtype = str)
        final = [0] * n # np.empty(n, dtype = str)

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