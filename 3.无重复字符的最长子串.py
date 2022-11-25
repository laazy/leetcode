#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        begin = 0
        checked = set()
        max_size = 1
        for end, i in enumerate(s):
            if i in checked:
                while s[begin] != i:
                    checked.remove(s[begin])
                    begin += 1
                checked.remove(s[begin])
                begin += 1
            checked.add(i)
            max_size = max(max_size, end - begin + 1)
        return max_size

# @lc code=end
print(Solution().lengthOfLongestSubstring('abcabcbb'))
print(Solution().lengthOfLongestSubstring('bbbbb'))
print(Solution().lengthOfLongestSubstring('pwwkew'))
print(Solution().lengthOfLongestSubstring('a'))
print(Solution().lengthOfLongestSubstring('au'))
