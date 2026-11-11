import math

class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []
 
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
 
 
    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])
 
    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
  
    def kruskal(self, cond):
        res = 0
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            # print("Edge:",u, v,end =" ")
            # print("-",weight)
            res += weight
            
        print(round(res,2))
        if not cond: print()


def fun(freckels, N, cond):
    if N > 2:
        aristas = int((N * (N - 1)) / 2)
        g = Graph(N)
        for i in range(0, N):
            x0, y0 = freckels[i][0], freckels[i][1]
            for j in range(i, N):
                if j != i:
                    x1, y1 = freckels[j][0], freckels[j][1]
                    distance = math.sqrt((x1-x0)**2 + (y1-y0)**2)
                    # print(i, j, distance)
                    g.add_edge(i, j, distance)
        g.kruskal(cond)
        
    else: 
        g = Graph(N)
        x0, y0 = freckels[0][0], freckels[0][1]
        x1, y1 = freckels[1][0], freckels[1][1]
        distance = math.sqrt((x1-x0)**2 + (y1-y0)**2)
        g.add_edge(0, 1, distance)
        g.kruskal(cond)



def main():
    testCases = int(input())
    
    for j in range(0, testCases):
        # print("Test case nº:", j)
        input()
        N = int(input())
        cond = j == testCases -1
        # print(N)
        freckels = [0] * N
        for i in range(0, N):
            aux = input().split(" ")
            freckels[i] = (float(aux[0]), float(aux[1]))
        
        fun(freckels, N, cond)
    
if __name__ == "__main__":
    main()
    
    # python p0001.py <1.in> 1.out
    # escripe en 1.out con print