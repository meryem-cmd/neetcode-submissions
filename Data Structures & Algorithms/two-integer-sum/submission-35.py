from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_d = defaultdict()
        for i, n in enumerate(nums):
            diff = target - n
            if diff not in hash_d:
                hash_d[n] = i
            else:
                return [hash_d[diff], i]

        