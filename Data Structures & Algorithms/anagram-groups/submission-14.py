from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            count = [0] * 26
            
            for c in s:
                diff = ord(c) - ord("a")
                count[diff] += 1
            d[tuple(count)].append(s)

        return list(d.values())



        


