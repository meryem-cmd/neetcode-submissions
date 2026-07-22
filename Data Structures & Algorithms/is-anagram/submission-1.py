class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
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

        for ch in first:
            if(first[ch] != second.get(ch,0)):
                 return False
            
        return True
       
       
           

        

        