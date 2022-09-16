# Justin Ventura

from helpers import create_graph
from queue import PriorityQueue


def dijkstras_algorithm(graph: dict, start: int) -> dict:
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    visited = set()

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        currDist, currNode = pq.get()
        visited.add(currNode)
        for neighbor, weight in graph[currNode]:
            if neighbor in visited:
                continue

            dist[neighbor] = min(dist[neighbor], currDist + weight)
            pq.put((dist[neighbor], neighbor))

    return dist


if __name__ == '__main__':
    n = 4
    edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    graph = create_graph(edges)

    assert dijkstras_algorithm(graph, 0) == {1: 3, 0: 0, 2: 4, 3: 5}
