class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict  = {}
        t_dict = {}
        for num in s:
            s_dict[num] = s_dict.get(num, 0) + 1
        for num in t:
            t_dict[num] = t_dict.get(num, 0) + 1
        if s_dict == t_dict:
            return True
        else:
            return  False
        
        