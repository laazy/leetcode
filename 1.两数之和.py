from typing import List
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for idx, i in enumerate(nums):
            if target - i in checked:
                return [idx, checked[target - i]]
            checked[i] = idx
# @lc code=end
