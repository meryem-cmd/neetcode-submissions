from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for str in strs:
            sorted_str = tuple(sorted(str))
            d[sorted_str].append(str)

        return list(d.values())
       

        