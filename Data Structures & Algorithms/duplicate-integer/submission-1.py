Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

this was the problem

Solution:
create a hashmap
go through each element of list
if element alr in hashmap return True
else add that element into hashmap 
after loop ends return False

        








class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if(num in hashset):
                return True
            
            hashset.add(num)
                
        return False



        
