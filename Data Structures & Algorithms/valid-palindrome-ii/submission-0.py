class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        lst = list(s)
        for i in range(len(lst)):
            temp = lst[:]
            temp.pop(i)

            if temp == temp[::-1]:
                return True
            
        return False
            

        