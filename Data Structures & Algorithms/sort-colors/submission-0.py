class Solution:
    def sortColors(self, nums: List[int]) -> None:
        mp = {}

        for num in nums:

            if num not in mp:
                mp[num] = []

            mp[num].append(num)

        k = 0

        for key in sorted(mp):

            for val in mp[key]:
                nums[k] = val
                k += 1
        


            
             

            
        