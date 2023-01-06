from typing import List
#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wl = len(words[0])
        sl = wl * len(words)
        wc = defaultdict(int)
        for i in words:
            wc[i] += 1
        ans = []
        begin = 0
        end = len(s) - sl
        while begin <= end:
            ws = defaultdict(int)
            for i in range(0, sl, wl):
                ws[s[begin+i: begin+i+wl]] += 1
            if ws == wc:
                ans.append(begin)
            begin += 1
        return ans
                
        
# @lc code=end
print(Solution().findSubstring('barfoothefoobarman', ["foo","bar"]))
print(Solution().findSubstring('barfoofoobarthefoobarman', ["foo","bar", "the"]))
print(Solution().findSubstring('wordgoodgoodgoodbestword', ["word","good","best","word"]))
print(Solution().findSubstring('wordgoodgoodgoodbestword', ["word","good","best","good"]))
