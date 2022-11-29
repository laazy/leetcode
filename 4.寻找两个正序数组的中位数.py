#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        if len(num) % 2 != 0:
            return num[len(num) // 2]
        return (num[len(num) // 2] + num[len(num) // 2-1]) / 2
# @lc code=end

