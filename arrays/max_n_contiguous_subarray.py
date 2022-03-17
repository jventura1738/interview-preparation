# Justin Ventura

from typing import List


def max_n_contiguous_subarray(nums: List[int], n: int) -> List[int]:
    """
    Given an integer array nums, return the maximum sum of three contiguous
    elements in the array.
    """
    if len(nums) < n:
        return None

    max_sum = sum(nums[:n])
    for i in range(n, len(nums)):

        if sum(nums[i - n + 1:i + 1]) > max_sum:
            max_sum = sum(nums[i - n + 1:i + 1])

    return max_sum


# Tests here:
def test_max_n_contiguous_subarray():
    result = max_n_contiguous_subarray([1, 2, 3, 4, 5], 3)
    assert result == 12

    result = max_n_contiguous_subarray([1, 2, 3, 4, 5], 2)
    assert result == 9

    result = max_n_contiguous_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4], 3)
    assert result == 5


if __name__ == '__main__':
    test_max_n_contiguous_subarray()
    print('All tests passed.')
