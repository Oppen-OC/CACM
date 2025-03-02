
def explore(graph, s, length):
    paths = graph[s]
    if paths is None: 
        return length, s
    else: 
        return explore(graph, s)

def create_graph(a):
    # Primera linea input()
    graph = {}
    for ini, fin in a:
        if ini not in graph: 
            graph[ini] = []
        graph[ini].append(fin)

    return graph

def main():
    cont = 0
    while True:
        cont += 1
        n = int(input())
        if n == 0:
            return
        
        s = int(input())
        a = []
        a.append(tuple(map(int, input().strip().split())))
        while a[-1] != (0,0):
            a.append(tuple(map(int, input().strip().split())))
        
        graph = create_graph(sorted(a[:-1]))
        l, fin = explore(graph, s, 0)

        print("Case", cont, ": The longest path from", s, "has length", l,", finishing at", fin,".")
        
    
if __name__ == "__main__":
    main()
    
    # n = Numero de puntos que puede visitar cesar
    # s = punto de inicio
    # a = n aristas
    # 0 0 = fin del caso