class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        
        for ch in s:
            if(ch in first):
                first[ch] += 1
            else:
                first[ch] = 1


        second = {}
        for ch in t:
            if(ch in second):
                second[ch] += 1
            else:
                second[ch] = 1


        if(first == second):
            return True
        else:
            return False

        

        