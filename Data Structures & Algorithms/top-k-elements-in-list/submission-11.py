from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        for num, count in c.items():
            freq[count].append(num)

        el = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                el.append(j)
                if len(el) == k:
                    return el