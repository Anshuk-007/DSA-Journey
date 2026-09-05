class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = {}
        r = []
        for i in nums:
            if i in c :
                c[i] = c[i]+1
            else:
                c[i] = 1
        for i in c:
            if c[i] > int(len(nums)/3):
                r.append(i)
        return r


        

        

        

        