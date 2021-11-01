# Justin Ventura


def maxSubsetSumNoAdjacent(arr):
    if not len(arr):
        return 0
    if len(arr) == 1:
        return arr[0]
    second = arr[0]
    first = max(arr[0:2])
    for i in range(2, len(arr)):
        curr = max(first, second + arr[i])
        second = first
        first = curr
    return first


if __name__ == '__main__':
    test = [75, 105, 120, 75, 90, 135]
    result = maxSubsetSumNoAdjacent(test)
    assert result == 330
    print(result)
