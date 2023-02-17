#include <iostream>
#include <string>
#include <vector>

using namespace std;
/*
 * @lc app=leetcode.cn id=198 lang=cpp
 *
 * [198] 打家劫舍
 */

// @lc code=start
class Solution {
   public:
    int rob(vector<int>& nums) {
        size_t n = nums.size();
        if (n == 1)
            return nums[0];
        int memo[n];
        memo[0] = nums[0];
        memo[1] = max(nums[0], nums[1]);
        for (int i = 2; i < n; i++)
            memo[i] = max(nums[i] + memo[i - 2], memo[i - 1]);
        return memo[n - 1];
    }
};
// @lc code=end
