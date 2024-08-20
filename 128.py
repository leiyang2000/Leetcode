from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        nums = set(nums)
        res = 0

        for num in nums:
            x = d.get(num-1, 0)
            y = d.get(num+1, 0)
            
            d[num-x] = x + 1 + y
            d[num+y] = x + 1 + y

            if x + 1 + y > res:
               res = x+1+y

        return res
    

s = Solution()
ret = s.longestConsecutive(nums = [100,4,200,1,3,2])
print(ret)