import heapq

def find_shortest_paths(city_pairs, start_city, end_city, num_paths):
    # Create a dictionary to store the graph
    graph = {}
    for cities, distance in city_pairs:
        city1, city2 = cities
        if city1 not in graph:
            graph[city1] = {}
        if city2 not in graph:
            graph[city2] = {}
        graph[city1][city2] = distance
        graph[city2][city1] = distance

    # Create a list to store the paths and distances
    paths = []

    for _ in range(num_paths):
        # Create a dictionary to store the shortest distances
        distances = {city: float('inf') for city in graph}
        distances[start_city] = 0

        # Create a dictionary to store the previous city in the shortest path
        previous = {city: None for city in graph}

        # Create a priority queue to store the cities to visit
        queue = [(0, start_city)]

        while queue:
            current_distance, current_city = heapq.heappop(queue)

            if current_city == end_city:
                break

            if current_distance > distances[current_city]:
                continue

            for neighbor, distance in graph[current_city].items():
                new_distance = current_distance + distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_city
                    heapq.heappush(queue, (new_distance, neighbor))

        # Reconstruct the shortest path
        path = []
        current_city = end_city
        while current_city:
            path.insert(0, current_city)
            current_city = previous[current_city]

        if path:
            paths.append((path, distances[end_city]))

        # Remove the edges of the found path to find the next shortest path
        for i in range(len(path) - 1):
            city1, city2 = path[i], path[i + 1]
            del graph[city1][city2]
            del graph[city2][city1]

    return paths

