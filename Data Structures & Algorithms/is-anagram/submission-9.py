from collections import defaultdict 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = defaultdict(int)
        t_hash = defaultdict(int)
        for si in s:
            s_hash[si] += 1;
            
        for ti in t:
            
            t_hash[ti] += 1;

        if s_hash == t_hash:
            return True
        else:
            return False

            