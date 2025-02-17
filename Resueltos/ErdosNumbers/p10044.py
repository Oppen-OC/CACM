import sys
from collections import deque

# Función lanzadera
def explorer(graph):
    distances = {"Erdos, P.": 0}  # Diccionario para almacenar las distancias mínimas
    queue = deque([("Erdos, P.", 0)])  # Cola para BFS (nombre, distancia)
    res = []

    while queue:
        name, dist = queue.popleft()  # O(1) en lugar de pop(0) que es O(n)
        res.append((name, dist))

        for neighbor in graph.get(name, []):
            if neighbor not in distances:  # Solo se actualiza si aún no ha sido visitado
                distances[neighbor] = dist + 1
                queue.append((neighbor, dist + 1))

    return res

def splitter(line):  
    """Recibe una línea del bloque P y devuelve una lista con los nombres."""
    line = line.split(":")
    names = line[0].split(",")
    res = []
    for x in range(0, len(names), 2):
        if x+1 < len(names):
            res.append(names[x].strip() + ", " + names[x+1].strip())
        else: 
            res.append(names[-1].strip())        
    return res

def fun():
    graph = {}
    
    Scenarios = int(input())
    point = 1

    for Scenario in range(1, Scenarios + 1):
        P, N = map(int, input().split())

        cont = 0
        # Crear el grafo
        while(cont < P):
            cont += 1
            names = splitter(input())
            for name in names:
                if name not in graph:
                    graph[name] = []
                graph[name].extend([x for x in names if x != name])

        # Busca los autores dentro del grafo
        erdosNums = explorer(graph)

        # Construir la salida sin línea vacía final
        result = [f"Scenario {Scenario}"]
        cont = 0
        while(cont < N):
            cont += 1
            name = input()
            val = next((t[1] for t in erdosNums if t[0] == name), "infinity")
            result.append(name + " " + str(val))
        #if Scenario != Scenarios: result.append("")
        
        print("\n".join(result))  # Evita la línea vacía final


def main():
    fun()
    
if __name__ == "__main__":
    main()
