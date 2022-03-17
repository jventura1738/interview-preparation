# Justin Ventura

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    Given an integer array nums, return true if there is a duplicate
    value in the array.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == '__main__':
    result = contains_duplicate([-1, 0, 1, 2, -1, -4])
    assert result == True
    print(result)
