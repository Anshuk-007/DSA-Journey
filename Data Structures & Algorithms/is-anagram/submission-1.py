class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_1 = sorted(t)
        s_1 = sorted(s)
        if t_1 == s_1:
            return True
        else:
            return False
            
        
        