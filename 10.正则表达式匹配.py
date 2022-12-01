#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch_dp(self, text, pattern):
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[i, j]
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {
                    text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    ans = dp(i, j+2) or first_match and dp(i+1, j)
                else:
                    ans = first_match and dp(i+1, j+1)
            memo[i, j] = ans
            return ans

        return dp(0, 0)

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
        else:  # normal p
            return bool(s) and (p[0] == '.' or s[0] == p[0]) and self.isMatch(s[1:], p[1:])


# @lc code=end
assert Solution().isMatch3("aa", "a") == False
assert Solution().isMatch3("aa", "a*") == True
assert Solution().isMatch3("ab", ".*") == True
assert Solution().isMatch3("aab", "c*a*b") == True
assert Solution().isMatch3("ab", ".*c") == False
assert Solution().isMatch3("aaa", "ab*ac*a") == True
assert Solution().isMatch3("a", "ab*") == True
assert Solution().isMatch3("aaa", "aaaa") == False
