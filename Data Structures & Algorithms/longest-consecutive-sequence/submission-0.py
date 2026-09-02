class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxlarg = 0
        for n in nums:
            if (n -1) not in nums:
                largest = 0
                while (n + largest) in nums:
                    largest += 1
                maxlarg = max(largest, maxlarg)
        return maxlarg



        