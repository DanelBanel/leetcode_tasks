#!/usr/bin/python3

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            if target - num in seen:
                return [idx, seen[target - num]]
            elif num not in seen:
                seen[num] = idx
