

def graph(teams, tables, N, M):
    graph = [0]*4
    aux = [0]*N
    for i in range(0, N):
        aux[i] = (0, i)
    graph[0] = aux
    
    for i in range(0, N):
        aux = [0]*teams[i]
        for j in range(0, M):
            

def main():
    # N = Numero de equipos
    # M = Numero de mesas
    while True:
        N, M = input().split(" ")
        N, M = int(N), int(M)
        if N == 0 and M == 0:
            break

        teams = list(map(int, input().split(" ")))
        tables = list(map(int, input().split(" ")))
       
        graph(teams, tables, N, M)
    
    
    
if __name__ == "__main__":
    main()
    # python p0001.py <1.in> 1.out
    # escripe en 1.out con print