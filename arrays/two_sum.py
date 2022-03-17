# Justin Ventura Amazon Prep

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Find the unique solution i, j where a[i] + a[j] = target

    Complexity( n=len(nums) ):
        Time: O(n + dict_lookup)
        Space: O(n)
    """
    seen = dict()
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    result = two_sum([2, 7, 11, 15], 9)
    assert result == [0, 1]
    print(result)
