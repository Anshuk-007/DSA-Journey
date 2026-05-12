class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = {}

        for i in nums:
            if i in s:
                s[i]+=1
            else:
                s[i] =1
        for j in s:
            if s[j] > (len(nums))/2:
                return j


        
                
        

        
           
        

            
        