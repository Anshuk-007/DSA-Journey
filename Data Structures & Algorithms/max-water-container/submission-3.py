class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        
        left = 0
        right = len(heights)-1
        m = 0 
        while left< right:
            a = min(heights[left], heights[right])
            b = right- left
            area = a*b
            m = max(m, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return m
            


        