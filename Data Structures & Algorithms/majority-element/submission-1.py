class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count =0
        troop = 0
        for i in nums:
            if count == 0:
                troop = i
            if i == troop:
                count+=1
            else:
                count-=1
        return troop
            
        


        
                
        

        
           
        

            
        