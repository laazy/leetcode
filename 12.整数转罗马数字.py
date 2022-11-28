#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        array = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        ans = ''
        begin = 0
        while num:
            for idx, (n, s) in enumerate(array[begin:]):
                if num >= n:
                    begin = idx
                    break
            num -= n
            ans += s
        return ans
# @lc code=end


def s(*args, **kwargs):
    s = Solution().intToRoman(*args, **kwargs)
    print(s)


s(num=3)
s(num=4)
s(num=9)
s(num=58)
s(num=1994)
