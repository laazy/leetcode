from typing import List
#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start


class Solution:
    def swap(self, nums: List[int], val: int):
        if val <= 0 or val > len(nums):
            return
        if nums[val - 1] == val:
            return
        tmp = nums[val - 1]
        nums[val - 1] = val 
        self.swap(nums, tmp)

    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in nums:
            self.swap(nums, i)
        for idx, i in enumerate(nums):
            if idx + 1 != i:
                return idx + 1
        # if nums[0] == 0:        
        return len(nums) + 1
        # return len(nums) + 1

# @lc code=end

print(Solution().firstMissingPositive([1,2,4]))
print(Solution().firstMissingPositive([2, 1]))
print(Solution().firstMissingPositive([1]))
print(Solution().firstMissingPositive([3,4,-1,1]))
print(Solution().firstMissingPositive([1,2,0]))