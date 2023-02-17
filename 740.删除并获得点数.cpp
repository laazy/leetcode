#include <vector>
#include <string>
#include <iostream>
#include <map>

using namespace std;
/*
 * @lc app=leetcode.cn id=740 lang=cpp
 *
 * [740] 删除并获得点数
 */

// @lc code=start
class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        map<int, int> memo;
        int n = 0;
        for(const auto &i : nums){
            memo[i]++;
            n = max(i, n);
        }
        int dp0 = 0, dp1 = memo[1], ans=memo[n];
        for (int i = 2; i <= n; i++) {
            ans = max(dp0 + memo[i]*i, dp1);
            dp0 = dp1;
            dp1 = ans;
        }
        return ans;
    }
};
// @lc code=end

