import sys
import heapq

def dijkstra(graph, fire_stations, n):
    """Compute the shortest distance from any intersection to the nearest fire station."""
    dist = [float('inf')] * (n + 1)
    pq = []
    
    for f in fire_stations:
        heapq.heappush(pq, (0, f))
        dist[f] = 0
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
        
        for v, length in graph[u]:
            if dist[v] > d + length:
                dist[v] = d + length
                heapq.heappush(pq, (dist[v], v))
    
    return dist

def find_best_fire_station(fire_stations, graph, n):
    """Find the best intersection to place a new fire station to minimize max distance."""
    original_dist = dijkstra(graph, fire_stations, n)
    
    best_location = 1
    best_max_dist = float('inf')
    
    for new_station in range(1, n + 1):
        if new_station in fire_stations:
            continue
        
        new_dist = dijkstra(graph, fire_stations + [new_station], n)
        max_dist = max(new_dist[1:])
        
        if max_dist < best_max_dist:
            best_max_dist = max_dist
            best_location = new_station
    
    return best_location

def main():
    input_data = sys.stdin.read().strip().split('\n')
    index = 0
    cases = int(input_data[index])
    index += 1
    
    results = []
    for _ in range(cases):
        while not input_data[index].strip():
            index += 1
        
        f, i = map(int, input_data[index].split())
        index += 1
        
        fire_stations = []
        for _ in range(f):
            fire_stations.append(int(input_data[index]))
            index += 1
        
        graph = {j: [] for j in range(1, i + 1)}
        
        while index < len(input_data) and input_data[index].strip():
            u, v, length = map(int, input_data[index].split())
            graph[u].append((v, length))
            graph[v].append((u, length))
            index += 1
        
        results.append(str(find_best_fire_station(fire_stations, graph, i)))
    
    print('\n\n'.join(results))

if __name__ == "__main__":
    main()
