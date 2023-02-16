#include <vector>
using namespace std;

/*
 * @lc app=leetcode.cn id=53 lang=cpp
 *
 * [53] 最大子数组和
 */

// @lc code=start
class Solution {
   public:
    int maxSubArray(vector<int>& nums) {
        size_t n = nums.size();
        int last = nums[0], ans = nums[0];
        for (int i = 1; i < n; i++) {
            last = max(last + nums[i], nums[i]);
            ans = max(last, ans);
        }
        return ans;
    }
};
// @lc code=end
