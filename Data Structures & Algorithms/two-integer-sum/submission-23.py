from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       prev_sum = {}
       for i , num in enumerate(nums):
        diff = target - num
        if diff in prev_sum:
            return [prev_sum[diff],i]
        prev_sum[num] = i
