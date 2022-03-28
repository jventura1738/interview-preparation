# Justin Ventura

from typing import List


# Max subarray solution using Kadane's Algorithm:
def max_subarray(nums: List[int] = None) -> int:
    maxSoFar = float('-inf')
    maxToHere = 0
    for num in nums:
        maxToHere = max(num, maxToHere + num)
        maxSoFar = max(maxToHere, maxSoFar)
    return maxSoFar


if __name__ == '__main__':
    print('joe momma')
