#include <iostream>
#include <string>
#include <vector>

using namespace std;
/*
 * @lc app=leetcode.cn id=91 lang=cpp
 *
 * [91] 解码方法
 */

// @lc code=start
class Solution {
   public:
    bool isNum(const char& c1, const char& c2) {
        // int val = ((c1 - '0') * 10 + c2 - '0');
        // return val && (val <= 26) && (c1 - '0');
        if (c1 == '1')
            return true;
        if (c1 != '2')
            return false;
        // so that, c1 == '2'
        if (c2 > '6')
            return false;
        return true;
    }

    int numDecodings(string s) {
        size_t n = s.size();
        if (!n || s[0] == '0')
            return 0;
        int dp[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 1; i < n; i++) {
            // bool is_num = ;
            dp[i + 1] = 0;
            if (s[i] != '0')
                dp[i + 1] += dp[i];
            if (isNum(s[i - 1], s[i]))
                dp[i + 1] += dp[i - 1];
            // if (s[i] == '0') {
            //     if (is_num)
            //         dp[i + 1] = dp[i - 1];
            //     else
            //         return 0;
            // } else if (is_num)
            //     dp[i + 1] = dp[i - 1] + dp[i];
            // else
            //     dp[i + 1] = dp[i];
        }
        return dp[n];
    }

    int numDecodings2(string s) {
        int len = s.size();
        if (!len)
            return 0;
        int dp[105];
        dp[0] = s[0] == '0' ? 0 : 1;
        for (int i = 1; i < len; i++) {
            dp[i] = 0;
            if (s[i] != '0') {
                dp[i] += dp[i - 1];
            }
            if (i >= 1 && (s[i - 1] == '1' || s[i - 1] == '2')) {
                int val = (s[i - 1] - '0') * 10 + s[i] - '0';
                if (val <= 26) {
                    if (i == 1) {
                        dp[i]++;
                    } else {
                        dp[i] += dp[i - 2];
                    }
                }
            }
        }
        return dp[len - 1];
    }
};
// @lc code=end
int main() {
    cout << Solution().numDecodings("226") << " <-> 3"
         << "\n";
    cout << Solution().numDecodings("06") << " <-> 0"
         << "\n";
    cout << Solution().numDecodings("27") << " <-> 1"
         << "\n";
    cout << Solution().numDecodings("10") << " <-> 1"
         << "\n";
    cout << Solution().numDecodings("10011") << " <-> 0"
         << "\n";
    cout << Solution().numDecodings("230") << " <-> 0"
         << "\n";
}
