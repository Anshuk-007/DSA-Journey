class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        
        for i in nums:
            
            key = i
            if i not in m:
                m[key] = 1
            else:
                m[key]+=1

        
        items = list(m.items())
        items.sort(key = lambda x:x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(items[i][0])
            
        return res

            


            
        
            
            

        