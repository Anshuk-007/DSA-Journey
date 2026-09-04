class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = strs[0]
        for i in strs:
            if len(i)< len (shortest):
                shortest = i

        prefix = ""
        for i in range(len(shortest)):
            ch = shortest[i]
            for j in strs:
                if j[i] != ch:
                    return prefix
            prefix+=ch
        return prefix



           

        
