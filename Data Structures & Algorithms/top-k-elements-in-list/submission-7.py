from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myl = []
        c = Counter(nums)
        m = c.most_common(k)
        i = 0
        while i <  k:
            myl.append(m[i][0])
            i += 1

        return myl