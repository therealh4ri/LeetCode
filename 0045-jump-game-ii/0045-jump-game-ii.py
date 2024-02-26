from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        farthest = 0
        while r < len(nums) - 1:
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res

    
