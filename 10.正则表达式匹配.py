#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    cache = {}


    def isMatch2(self, s, p):
        # use cache
        if (s, p) in self.cache:
            return self.cache[(s, p)]
        if not p:
            return not s
        if p[-1] == '*':
            if self.isMatch(s, p[:-2]):
                self.cache[(s, p)] = True
                return True
            if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch(s[:-1], p):
                self.cache[(s, p)] = True
                return True
        if s and (p[-1] == s[-1] or p[-1] == '.') and self.isMatch(s[:-1], p[:-1]):
            self.cache[(s, p)] = True
            return True
        self.cache[(s, p)] = False
        return False

    def match_star(self, s: str, p: str):
        yield s
        for idx, i in enumerate(s):
            if i == p[0] or p[0] == '.':
                yield s[idx+1:]
            else:
                break

    def isMatch(self, s: str, p: str) -> bool:

        # if not (s or p): # s == p == ''
        #     return True
        if not p:  # p == '', s != ''
            return not s
        # p != '', s != '', but p starts with '\s*'
        if len(p) > 1 and p[1] == '*':
            for i in self.match_star(s, p[:2]):
                if self.isMatch(i, p[2:]):
                    return True
            return False
        else: # normal p
            return bool(s) and (p[0] == '.' or s[0] == p[0]) and self.isMatch(s[1:], p[1:])
            

# @lc code=end
assert Solution().isMatch(s= "aa", p = "a") == False
assert Solution().isMatch(s="aa", p="a*") == True
assert Solution().isMatch(s= "ab", p = ".*") == True
assert Solution().isMatch(s= "aab", p = "c*a*b") == True
assert Solution().isMatch(s= "ab", p = ".*c") == False
assert Solution().isMatch(s="aaa", p="ab*ac*a") == True
assert Solution().isMatch(s="a", p="ab*") == True
assert Solution().isMatch(s="aaa", p="aaaa") == False
