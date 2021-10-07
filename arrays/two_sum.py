# Justin Ventura Amazon Prep

import sys
from typing import List


def two_sum(self, nums: List[int], target: int) -> List[int]:
    """Find the unique solution i, j where a[i] + a[j] = target

    Complexity( n=len(nums) ):
        Time: O(n + dict_lookup)
        Space: O(n)
    """
    d = {}
    for i, e in enumerate(nums):
        tmp = target - e
        if tmp in d.keys():
            return [d[tmp], i]
        d[e] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
