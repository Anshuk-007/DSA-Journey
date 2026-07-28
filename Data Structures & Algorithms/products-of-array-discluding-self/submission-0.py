class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        d = []

        for i in range(len(nums)):
            product = 1

            for j in range(len(nums)):
                if i == j :
                    continue

                product *= nums[j]

            d.append(product)
        return d


            
        