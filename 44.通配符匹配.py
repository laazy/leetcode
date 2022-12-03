from debug_util import Memo
#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
from collections import defaultdict


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # memo = Memo()
        memo = {}

        def dp(i: int, j: int) -> bool:
            if i < 0 or j < 0:
                return False
            if i > 0 and j == 0:
                return False
            if (i, j) in memo:
                return memo[i, j]
            if p[j-1] != '*':
                ans = dp(i-1, j-1) and ((s[i-1] == p[j-1]) or p[j-1] == '?')
            else:
                ans = False
                for idx in range(i+1):
                    if dp(idx, j-1):
                        ans = True
                        break
            memo[i, j] = ans
            return ans
        memo[0, 0] = True
        while True:
            p = p.replace('**', '*')
            if p.count('**') == 0:
                break

        ans = dp(len(s), len(p))
        # memo.dump('my')
        return ans

    def isMatch2(self, s, p):
        dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
        # dp = Memo()
        # dp.data = defaultdict(bool)
        dp[0][0] = True
        for j in range(1, len(p)+1):
            if p[j-1] != '*':
                break
            dp[0][j] = True

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] in {s[i-1], '?'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        # dp.dump('dp')
        return dp[-1][-1]


# @lc code=end
print(Solution().isMatch(
    'babbaabaabaaaaabbbbabaababbababbbaabbbbbbbbbababaabbabbaaabaaabbababbaaabbbbababbbaaababbbbababababaaaabbbbabbbabbabbbaaabaabaababbababbbabaaabbbbaaabbbabbabbbbaabaabbabaabababbbababaaabaaabbbabbaaaabab',
    'baa*b*ab*aa**bb*bbbaab***b*abbb*bbb*b*aa*b*b*ab*********ab*b***abb***a*bbb***a*a*b*baa*b***bb*b**ba*b*'))
print('bb')
print(Solution().isMatch2(
    'babbaabaabaaaaabbbbabaababbababbbaabbbbbbbbbababaabbabbaaabaaabbababbaaabbbbababbbaaababbbbababababaaaabbbbabbbabbabbbaaabaabaababbababbbabaaabbbbaaabbbabbabbbbaabaabbabaabababbbababaaabaaabbbabbaaaabab',
    'baa*b*ab*aa**bb*bbbaab***b*abbb*bbb*b*aa*b*b*ab*********ab*b***abb***a*bbb***a*a*b*baa*b***bb*b**ba*b*'))
# print(Solution().isMatch('a', ''))
# print(Solution().isMatch('', '*'))
# print(Solution().isMatch('', 'a'))
# print(Solution().isMatch('aa', '*'))
# print(Solution().isMatch('cb', '?a'))
# print(Solution().isMatch('abceb', '*a*b'))
# print(Solution().isMatch('acdcb', 'a*c?b'))
