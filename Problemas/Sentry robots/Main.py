import numpy as np    
from collections import defaultdict
  
                        
def indexs(matrix, value):
    cont = 0
    index = []
    for x, i in enumerate(matrix):
        if x == value:
            cont += 1
            index.append(i)
        i += 1
    return cont, index                    

def fun(matrix, pois, obs, x, y):
    # Primera linea input()
    print(matrix)
    new_matrix = []
    for i in range(0, y):
        cont, index = indexs(matrix, 8)
        line = matrix[i]
        if cont > 0:
            for j in range(0, cont):
                new_matrix.append(line[:index[j]])
                new_matrix.append(line[index[j]:])
        else:
            new_matrix.append(line[i])
        print(i)
        print(new_matrix)

def main():
    testCases = int(input())
    for _ in range(0, testCases):
        input()
        aux = input().split(" ")
        x, y = int(aux[0]), int(aux[1])
        matrix = np.zeros((x, y))
        P = int(input())
        pois = [0]*P
        for j in range(0, P):
            pois[j] = input().split(" ")
            pois[j] = (int(pois[j][0]) -1, int(pois[j][1]) -1)
            matrix[pois[j][0]][pois[j][1]] = "1"

        O = int(input())
        obs = [0]*O
        for j in range(0, O):
            obs[j] = input().split(" ")
            obs[j] = (int(obs[j][0]) -1, int(obs[j][1]) -1)
            matrix[obs[j][0]][obs[j][1]] = "8"
            
        update_M = fun(matrix, pois, obs, x, y)
        
# This class represents a directed graph 
# using adjacency matrix representation
class Graph:

    def __init__(self, graph):
        self.graph = graph # residual graph
        self. ROW = len(graph)
        # self.COL = len(gr[0])

    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''

    def BFS(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False]*(self.ROW)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    # If we find a connection to the sink node, 
                    # then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True

        # We didn't reach sink in BFS starting 
        # from source, so return false
        return False
            
    
    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)

        max_flow = 0 # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow
    
# Create a graph given in the above diagram
"""
graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

g = Graph(graph)
source = 0; sink = 5

print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink))
"""
if __name__ == "__main__":
    main()
    
    # python p0001.py <1.in> 1.out
    # escripe en 1.out con print