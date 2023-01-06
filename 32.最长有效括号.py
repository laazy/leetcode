#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses_dp(self, s: str) -> int:
        memo = [0] * len(s)
        ans = 0
        for i in range(1, len(s)):
            if s[i] != ')':
                continue
            if s[i-1] == '(':
                memo[i] = memo[i-2] + 2
            elif memo[i-1] != 0:
                left = i - memo[i-1] - 1
                if left >= 0 and s[left] == '(':
                    memo[i] = memo[i-1] + 2 + memo[left-1]
            ans = max(ans, memo[i])
        return ans
    
    def longestValidParentheses(self, s: str) -> int:
        def helper(s: str, rev: bool = False) -> int:
            l=r=c=0
            for i in s:
                if i == '(':
                    l+=1
                else:
                    r+=1
                if l == r:
                    c = max(c, l+r)
                elif not rev and l<r:
                    l=r=0
                elif rev and l>r:
                    l=r=0
            return c
        return max(helper(s), helper(reversed(s), True))
                          
# @lc code=end

print(Solution().longestValidParentheses("(()"))
print(Solution().longestValidParentheses("(()))())("))
print(Solution().longestValidParentheses(""))
print(Solution().longestValidParentheses("()(())"))
