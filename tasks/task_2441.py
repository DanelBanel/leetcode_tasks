#!/usr/bin/python3
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        for el in sorted_nums:
            if -el in nums:
                return el
        return -1
