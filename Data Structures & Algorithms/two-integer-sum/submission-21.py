from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_hashmap:
                return [prev_hashmap[diff], i]
            prev_hashmap[num] = i