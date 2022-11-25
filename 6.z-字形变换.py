#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def _split(self, s: str):
        begin, end = 1, len(s) - 1
        res = [s[0]]
        while begin < end:
            res.append(s[begin]+s[end])
            begin += 1
            end -= 1
        res.append(s[begin])
        return res

    def convert2(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        single_size = 2 * numRows - 2
        s += ' ' * (single_size - len(s) % single_size)
        res = []
        for i in range(len(s) // single_size):
            res.append(self._split(s[i*single_size:(i+1)*single_size]))
        ans = ''
        for i in zip(*res):
            ans += ''.join(i)
        ans = ans.replace(' ', '')
        return ans

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        res = [''] * numRows
        idx = 0
        size = numRows * 2 - 2
        for i in s:
            if idx == size:
                idx = 0
            if idx < numRows:
                res[idx] += i
            else:
                res[size - idx] += i
            idx += 1
        s= ''.join(res)
        return s


# @lc code=end
assert Solution().convert(s="PAYPALISHIRING", numRows=3) == 'PAHNAPLSIIGYIR'
assert Solution().convert(s="PAYPALISHIRING", numRows=4) == 'PINALSIGYAHRPI'
Solution().convert(s="A", numRows=1)

