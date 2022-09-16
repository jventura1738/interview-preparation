# Justin Ventura


import logging

from typing import DefaultDict


# [to, from, weight]
def create_graph(edges: list) -> dict:
    graph = DefaultDict(list)
    for edge in edges:
        fro, to, weight = edge
        graph[to].append((fro, weight))
        graph[fro].append((to, weight))

    logging.debug(graph)
    return graph
