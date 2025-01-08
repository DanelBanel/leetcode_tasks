#!/usr/bin/python3
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        nums.reverse()
        k %= len(nums)
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums
