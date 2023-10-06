import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {}

        for vertex in vertices:
            self.adj_list[vertex] = []

    def add_edge(self, u, v, w):
        self.adj_list[u].append((v, w))
        self.adj_list[v].append((u, w))

    def dijkstra(self, source):
        # Initialize distances with infinity and source with 0
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[source] = 0

        # Priority queue to store (distance, vertex) pairs
        pq = [(0, source)]

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            # Skip if we've already found a shorter path
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight

                # If a shorter path is found, update the distance and push it to the priority queue
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

# Example usage
vertices = ['A', 'B', 'C', 'D', 'E']
graph = Graph(vertices)

graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 3)
graph.add_edge('B', 'C', 1)
graph.add_edge('B', 'D', 4)
graph.add_edge('C', 'D', 1)
graph.add_edge('D', 'E', 2)

source_vertex = 'A'
distances = graph.dijkstra(source_vertex)

print("Shortest distances from", source_vertex)
for vertex, distance in distances.items():
    print(f"To {vertex}: {distance}")
