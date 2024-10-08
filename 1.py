from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):

            if target - nums[i] in d:

                return [i, d[target - nums[i]]]
            
            d[nums[i]] = i
            

s = Solution()
ret = s.twoSum(nums = [1,2,3,4],target = 7)
print(ret)