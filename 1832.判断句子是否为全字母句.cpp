#include <vector>
#include <string>
#include <iostream>

using namespace std;
/*
 * @lc app=leetcode.cn id=1832 lang=cpp
 *
 * [1832] 判断句子是否为全字母句
 */

// @lc code=start
class Solution {
public:
    bool checkIfPangram(string sentence) {
        uint32_t ans = (1 << 26) - 1;
        for (const auto &i: sentence)
            ans &= ~(1 << (i - 'a'));
        return ans == 0;
    }
};
// @lc code=end
int main(){
    cout << Solution().checkIfPangram("hxsdz") << "\n";
}