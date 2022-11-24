from typing import List
#
# @lc app=leetcode.cn id=372 lang=python3
#
# [372] 超级次方
#

# @lc code=start


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        power = a
        res = 1
        for i in reversed(b):
            res = power ** i % 1337 * res % 1337
            power = power ** 10 % 1337
        return res
        


        
# @lc code=end

# print(Solution().superPow(2, [3]))
print(Solution().superPow(a=2, b=[1, 0]))
print(Solution().superPow(a=1, b=[4, 3, 3, 8, 5, 2]))
print(Solution().superPow(2147483647, [2,0,0]))