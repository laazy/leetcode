#include <iostream>
#include <vector>
using namespace std;

/*
 * @lc app=leetcode.cn id=746 lang=cpp
 *
 * [746] 使用最小花费爬楼梯
 */

// @lc code=start
class Solution {
   public:
    int minCostClimbingStairs(vector<int>& cost) {
        size_t n = cost.size();
        int n0 = 0, n1 = 0, ans;
        for (int i = 2; i <= n; i++) {
            ans = min(n1 + cost[i - 1], n0 + cost[i - 2]);
            n0 = n1;
            n1 = ans;
        }
        return ans;
    }
};
// @lc code=end

int main() {
    vector<int> input{10, 15, 20};
    cout << Solution().minCostClimbingStairs(input) << "\n";
}