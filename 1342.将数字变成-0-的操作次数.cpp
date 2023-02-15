/*
 * @lc app=leetcode.cn id=1342 lang=cpp
 *
 * [1342] 将数字变成 0 的操作次数
 */

// @lc code=start
class Solution {
   public:
    int numberOfSteps(int num) {
        int cnt = 0;
        while (num) {
            if (num % 2 == 0)
                num /= 2;
            else
                num -= 1;
            cnt++;
        }
        return cnt;
    }
};
// @lc code=end
