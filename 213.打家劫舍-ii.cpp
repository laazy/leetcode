#include <iostream>
#include <string>
#include <vector>

using namespace std;
/*
 * @lc app=leetcode.cn id=213 lang=cpp
 *
 * [213] 打家劫舍 II
 */

// @lc code=start
class Solution {
   public:
    int rob(vector<int>& nums) {
        size_t n = nums.size();
        if (n == 1)
            return nums[0];
        int dp[2][n];
        dp[0][0] = nums[0];
        dp[0][1] = max(nums[0], nums[1]);
        dp[1][1] = nums[1];
        dp[1][0] = 0;
        for (int i = 2; i < n; i++)
            for (int j = 0; j < 2;j++)
                dp[j][i] = max(dp[j][i - 1], dp[j][i - 2] + nums[i]);
        return max(dp[1][n - 1], dp[0][n - 2]);
    }
};
// @lc code=end
