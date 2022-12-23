from typing import List
#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = 0
        next_buy = 10 ** 5
        for i in prices:
            if i < next_buy:
                next_buy = i
            if i - next_buy > sell - buy:
                buy = next_buy
                sell = i
        return sell - buy
# @lc code=end

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))
