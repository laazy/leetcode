from debug_util import Memo, DefaultMemo
#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, text, pattern):
        memo = Memo()

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

        ans = dp(0, 0)
        memo.dump('dp')
        return ans


    def isMatch_sp(self, s, p):
        # dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp = DefaultMemo(False)
        dp[0,0] = True
        for i in range(1, len(p)):
            dp[i + 1,0] = dp[i - 1,0] and p[i] == '*'
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    dp[i + 1,j + 1] = dp[i - 1,j + 1] or dp[i,j + 1]
                    if p[i - 1] == s[j] or p[i - 1] == '.':
                        dp[i + 1,j + 1] |= dp[i + 1,j]
                else:
                    dp[i + 1,j + 1] = dp[i,j] and (p[i] == s[j] or p[i] == '.')
        dp.dump('sp')
        return dp[-1,-1]

    def isMatch2(self, s, p):
        self.cache = Memo()
        def wrap(s,p):
        # use cache
            if (s, p) in self.cache:
                return self.cache[(s, p)]
            if not p:
                return not s
            if p[-1] == '*':
                if wrap(s, p[:-2]):
                    self.cache[(s, p)] = True
                    return True
                if s and (s[-1] == p[-2] or p[-2] == '.') and wrap(s[:-1], p):
                    self.cache[(s, p)] = True
                    return True
            if s and (p[-1] == s[-1] or p[-1] == '.') and wrap(s[:-1], p[:-1]):
                self.cache[(s, p)] = True
                return True
            self.cache[(s, p)] = False
            return False
        ans = wrap(s,p)
        self.cache.dump('2')
        return ans

    def match_star(self, s: str, p: str):
        yield s
        for idx, i in enumerate(s):
            if i == p[0] or p[0] == '.':
                yield s[idx+1:]
            else:
                break

    def isMatch3(self, s: str, p: str) -> bool:

        # if not (s or p): # s == p == ''
        #     return True
        if not p:  # p == '', s != ''
            return not s
        # p != '', s != '', but p starts with '\s*'
        if len(p) > 1 and p[1] == '*':
            for i in self.match_star(s, p[:2]):
                if self.isMatch3(i, p[2:]):
                    return True
            return False
        else:  # normal p
            return bool(s) and (p[0] == '.' or s[0] == p[0]) and self.isMatch3(s[1:], p[1:])


# @lc code=end
assert Solution().isMatch("aa", "a") == False
assert Solution().isMatch("aa", "a*") == True
assert Solution().isMatch("ab", ".*") == True
assert Solution().isMatch("aab", "c*a*b") == True
assert Solution().isMatch("ab", ".*c") == False
assert Solution().isMatch("aaa", "ab*ac*a") == True
assert Solution().isMatch("a", "ab*") == True
assert Solution().isMatch("aaa", "aaaa") == False
assert Solution().isMatch3('babbaabaabaaaaabbbbabaababbababbbaabbbbbbbbbababaabbabbaaabaaabbababbaaabbbbababbbaaababbbbababababaaaabbbbabbbabbabbbaaabaabaababbababbbabaaabbbbaaabbbabbabbbbaabaabbabaabababbbababaaabaaabbbabbaaaabab',
    'baa.*b.*ab.*aa.*bb.*bbbaab.*b.*abbb.*bbb.*b.*aa.*b.*b.*ab.*.*ab.*b.*abb.*a.*bbb.*a.*a.*b.*baa.*b.*bb.*b.*ba.*b.*') == False
# assert Solution().isMatch2('babbaabaabaaaaabbbbabaababbababbbaabbbbbbbbbababaabbabbaaabaaabbababbaaabbbbababbbaaababbbbababababaaaabbbbabbbabbabbbaaabaabaababbababbbabaaabbbbaaabbbabbabbbbaabaabbabaabababbbababaaabaaabbbabbaaaabab',
#     'baa.*b.*ab.*aa.*bb.*bbbaab.*b.*abbb.*bbb.*b.*aa.*b.*b.*ab.*.*ab.*b.*abb.*a.*bbb.*a.*a.*b.*baa.*b.*bb.*b.*ba.*b.*') == False
assert Solution().isMatch('babbaabaabaaaaabbbbabaababbababbbaabbbbbbbbbababaabbabbaaabaaabbababbaaabbbbababbbaaababbbbababababaaaabbbbabbbabbabbbaaabaabaababbababbbabaaabbbbaaabbbabbabbbbaabaabbabaabababbbababaaabaaabbbabbaaaabab',
    'baa.*b.*ab.*aa.*bb.*bbbaab.*b.*abbb.*bbb.*b.*aa.*b.*b.*ab.*.*ab.*b.*abb.*a.*bbb.*a.*a.*b.*baa.*b.*bb.*b.*ba.*b.*') == False
# assert Solution().isMatch_sp('babbaabaabaaaaabbbbabaababbababbbaabbbbbbbbbababaabbabbaaabaaabbababbaaabbbbababbbaaababbbbababababaaaabbbbabbbabbabbbaaabaabaababbababbbabaaabbbbaaabbbabbabbbbaabaabbabaabababbbababaaabaaabbbabbaaaabab',
#     'baa.*b.*ab.*aa.*bb.*bbbaab.*b.*abbb.*bbb.*b.*aa.*b.*b.*ab.*.*ab.*b.*abb.*a.*bbb.*a.*a.*b.*baa.*b.*bb.*b.*ba.*b.*') == False
