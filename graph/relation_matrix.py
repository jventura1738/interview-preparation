# Justin Ventura | Twitter

import sys

"""
EX1:
[[1 1 0 0]
 [1 1 1 0]
 [0 1 1 0]
 [0 0 0 1]]

python3 relation_matrix.py 4 1100 1110 0110 0001
-> 2

EX2:
    0 1 2 3 4 5 6
-----------------
0 | 1 1 1 0 0 0 0
1 | 1 1 1 0 0 0 0
2 | 1 1 1 1 0 0 0
3 | 0 0 1 1 0 0 0
4 | 0 0 0 0 1 0 0
5 | 0 0 0 0 0 1 1
6 | 0 0 0 0 0 1 1

python3 relation_matrix.py 7 1110000 1110000 1111000 0011000 0000100 0000011 0000011
-> 3

EX3:
100
010
001

python3 relation_matrix.py 3 100 010 001
-> 3
"""

visited = set()


def DFS(v_i, graph):
    if v_i not in visited:
        visited.add(v_i)
        for v_j in graph[v_i]:
            DFS(v_j, graph)


def num_groups(graph):
    groups = 0
    for v_i in graph.keys():
        if v_i not in visited:
            DFS(v_i, graph)
            groups += 1
    return groups


if __name__ == '__main__':
    n = int(sys.argv[1])
    related = []
    for i, line in enumerate(sys.argv[2:]):
        related.append(list(line))

    graph = {i: [] for i in range(n)}

    for r in range(1, n):
        for c in range(0, n-1):
            curr = int(related[r][c])
            if curr == 1:
                graph[r].append(c)
                graph[c].append(r)

    print(num_groups(graph))
