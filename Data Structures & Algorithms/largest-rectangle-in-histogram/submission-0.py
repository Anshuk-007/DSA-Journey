class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        m = 0
        for i in range(len(heights)):
            
                
            while len(stack)> 0 and heights[i]< heights[stack[-1]]:
                
                popped = stack.pop()

                if len(stack) == 0:
                    l = i
                else:
                    l = i - stack[-1] - 1

                area = l*heights[popped]
                m = max(area,m)
            stack.append(i)
        while len(stack)> 0 :
                
            popped = stack.pop()

            if len(stack) == 0:
                l = len(heights)
            else:
                l = len(heights) - stack[-1] - 1

            area = l*heights[popped]
            m = max(area,m)    
        return m