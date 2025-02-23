import sys
import heapq

def min_gas_cost(distance, stations):
    stations.append((distance, 0))  # Add final destination as a "station" with zero cost
    
    fuel_capacity = 200  # Maximum tank capacity
    fuel = 100  # Starts with 100 litres (half tank)
    cost = 0  # Total cost
    position = 0  # Current location
    min_heap = []  # Min-heap for gas prices (stores price per litre)

    for station_distance, price in stations:
        needed_fuel = station_distance - position  # Fuel required to reach this station

        while fuel < needed_fuel:  # If we can't reach the next station, buy fuel
            if not min_heap:  # No cheaper fuel available -> Impossible
                return "Impossible"
            
            cheapest_price = heapq.heappop(min_heap)  # Buy from cheapest available station
            fuel_to_buy = min(fuel_capacity - fuel, needed_fuel)  # Buy just enough to reach next stop
            cost += cheapest_price * fuel_to_buy  # Update cost
            fuel += fuel_to_buy  # Refill fuel
        
        fuel -= needed_fuel  # Travel to the station
        position = station_distance
        heapq.heappush(min_heap, price)  # Store price for future use

    return str(cost)

def main():
    input_data = sys.stdin.read().strip().split("\n")
    index = 0
    num_cases = int(input_data[index])
    index += 1

    results = []
    
    for _ in range(num_cases):
        while input_data[index] == "":
            index += 1  # Skip blank lines
        
        distance = int(input_data[index])
        index += 1
        stations = []
        
        while index < len(input_data) and input_data[index] != "":
            d, p = map(int, input_data[index].split())
            stations.append((d, p))
            index += 1
        
        results.append(min_gas_cost(distance, stations))
    
    sys.stdout.write("\n\n".join(results) + "\n")

if __name__ == "__main__":
    main()
