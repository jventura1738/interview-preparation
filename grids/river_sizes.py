# Justin Ventura

def riverSizes(matrix):
    visited = set()
    total = list()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if size := find_river(matrix, i, j, visited):
                total.append(size)
    return total


def find_river(matrix, i, j, visited):
    if not valid_move(matrix, i, j) or matrix[i][j] == 0:
        return 0
    if i*10**5+j in visited:
        return 0
    size = 1
    visited.add(i*10**5+j)
    size += find_river(matrix, i+1, j, visited)
    size += find_river(matrix, i, j+1, visited)
    size += find_river(matrix, i-1, j, visited)
    size += find_river(matrix, i, j-1, visited)
    return size


def valid_move(arr, i, j):
    return True if 0 <= i < len(arr) and 0 <= j < len(arr[0]) else False


if __name__ == '__main__':
    matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]
    ]
    result = riverSizes(matrix)    
    assert sorted(result) == [1, 2, 2, 2, 5]
    print(result)
