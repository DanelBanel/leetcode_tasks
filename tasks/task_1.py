from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #print(f"Target: {target}")
        seen = {}
        for idx, num in enumerate(nums):
            #print(f"Num: {num}")
            #print(f"Seen: {seen}")
            if target - num in seen:
                return [idx, seen[target - num]]
            elif num not in seen:
                seen[num] = idx