from queue import PriorityQueue


class Dijkstra:
    def __init__(self, total_vertices: int) -> None:
        self.total_vertices = total_vertices
        self.edges = [[-1 for _ in range(total_vertices)] for _ in range(total_vertices)]
        self.visited = []
    
    def add_edge(self, origin_node: int, destination_node: int, weight: int) -> None:
        self.edges[origin_node][destination_node] = weight
        self.edges[destination_node][origin_node] = weight

    def get_distances(self, start_node: int) -> list :
        distances = [float('inf')] * self.total_vertices
        distances[start_node] = 0

        pq = PriorityQueue()
        pq.put((0, start_node))

        while not pq.empty():
            dist, current_vertex = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.total_vertices):
                distance = self.edges[current_vertex][neighbor]

                if distance != -1 and neighbor not in self.visited:
                    old_cost = distances[neighbor]
                    new_cost = distances[current_vertex] + distance

                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        distances[neighbor] = new_cost
        return distances

def main():
    g = Dijkstra(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 6, 7)
    g.add_edge(1, 6, 11)
    g.add_edge(1, 7, 20)
    g.add_edge(1, 2, 9)
    g.add_edge(2, 3, 6)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 4, 10)
    g.add_edge(3, 5, 5)
    g.add_edge(4, 5, 15)
    g.add_edge(4, 7, 1)
    g.add_edge(4, 8, 5)
    g.add_edge(5, 8, 12)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 8, 3) 

    distances = g.get_distances(0)
    print(distances)


if __name__ == '__main__':
    main()
