from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h = set()
        for num in nums:
            if num in h:
                return num
            h.add(num)


s = Solution()
ret = s.findDuplicate(nums = [1,3,4,2,4])
print(ret)