#include <threads.h>
#include <mutex>
#include <condition_variable>
#include <vector>
#include <iostream>
#include <string>

using namespace std;
/**
 * 线程池：
 *   1. 固定 worker
 *   2. 提交函数、参数
 *   3. 依此返回运行结果
 * 
 * 需要技术：
 *   1. 函数式编程
 *   2. 锁
 *   3. 条件变量
 */

class ThreadPool{
    public:
        // TODO: support passing function
        // TODO: support passing arbitrary arguments
        // TODO: support return arbitrary value
        // TODO: thread has group
        // TODO: run in new thread
        vector<int> apply(vector<int> &args){
            vector<int> ans;
            for (auto i: args){
                ans.push_back(foo(i));
            }
            return ans;
        }

        ThreadPool(size_t size){
            pool_size = size;
        }

    private: 
        size_t pool_size;
        int foo(int arg){
            return arg * arg;
        }
};

int main(){
    ThreadPool tp(4);
    vector<int> args {1, 2, 3, 4};
    auto ans = tp.apply(args);
    // TODO: python's enumerate in cpp
    for (size_t i = 0; i < args.size(); i++){
        cout << "input: " << args[i] << "  output: " << ans[i] << endl;
    }
}