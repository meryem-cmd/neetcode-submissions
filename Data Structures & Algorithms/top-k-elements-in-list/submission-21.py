from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]  # +1 to avoid index error
        
        for n, count in c.items():   # ✅ iterate over unique keys
            freq[count].append(n)

        new_l = []
        for j in range(len(freq) - 1, 0, -1):
            new_l.extend(freq[j])    # ✅ extend not append
            if len(new_l) >= k:      # ✅ check element count
                return new_l[:k]

        

        