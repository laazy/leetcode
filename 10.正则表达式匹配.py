#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def match_star(self, s: str, p: str):
        if s[0] != p[0] and p[0] != '.':
            return ''
        for idx, i in enumerate(s):
            if i == s[0]:
                yield s[idx+1:]

    def isMatch(self, s: str, p: str) -> bool:
        if not (s or p):
            return True
        if not p:
            return False
        if len(s) > 1 and len(p) > 1 and p[1] == '*':
            for i in self.match_star(s, p[:2]):
                if i and self.isMatch(i, p[2:]):
                    return True
        else:
            return (p[0] == '.' or s[0] == p[0]) and self.isMatch(s[1:], p[1:])
            

# @lc code=end
# print(Solution().isMatch(s= "aa", p = "a"))
# print(Solution().isMatch(s="aa", p="a*"))
print(Solution().isMatch(s= "ab", p = ".*"))
