import sys

sys.setrecursionlimit(10**6)  # Increase recursion limit for deep graphs

def dfs(node, graph, dp, finish_node):
    """Returns the longest path length from 'node' and the corresponding smallest finish node."""
    if node in dp:  # Return memoized result
        return dp[node]
    
    max_length = 0
    best_end = node  # Default finishing node is itself

    if node in graph:
        for neighbor in graph[node]:
            path_length, end_node = dfs(neighbor, graph, dp, finish_node)
            if path_length + 1 > max_length or (path_length + 1 == max_length and end_node < best_end):
                max_length = path_length + 1
                best_end = end_node
    
    dp[node] = (max_length, best_end)  # Memoize result
    return dp[node]

def create_graph(edges):
    """Creates adjacency list from input edges."""
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
    return graph

def main():
    case_num = 0
    while True:
        case_num += 1
        n = int(input())  # Number of nodes
        if n == 0:
            break

        s = int(input())  # Start node
        edges = []

        while True:
            u, v = map(int, input().split())
            if (u, v) == (0, 0):
                break
            edges.append((u, v))

        graph = create_graph(edges)
        dp = {}  # Memoization table
        
        # Compute longest path from s
        max_length, final_node = dfs(s, graph, dp, s)

        print(f"Case {case_num}: The longest path from {s} has length {max_length}, finishing at {final_node}.")
        print()  # Print extra newline for formatting

if __name__ == "__main__":
    main()
