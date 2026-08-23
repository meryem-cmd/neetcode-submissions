from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for s in strs:
            c = [0] * 26
            for ch in s:
                place = ord(ch) - ord("a")
                c[place] += 1
            
            d[tuple(c)].append(s)

        return list(d.values())
            
        