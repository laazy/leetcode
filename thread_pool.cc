#include <chrono>
#include <condition_variable>
#include <ctime>
#include <functional>
#include <future>
#include <iostream>
#include <mutex>
#include <queue>
#include <string>
#include <thread>
#include <vector>

// using namespace std;
/**
 * 线程池：
 *   1. 固定 worker
 *   2. 提交函数、参数
 *   3. 依此返回运行结果
 *
 */

std::mutex cout_mtx;

class ThreadPool {
   public:
    ThreadPool(size_t size) {
        // TODO: get min(cpu, size)
        terminated = false;
        pool_size = std::min(static_cast<size_t>(std::thread::hardware_concurrency()), size);
        threads.reserve(pool_size);
        for (size_t i = 0; i < pool_size; i++) {
            std::cout << "Thread Pool: Try to create worker[" << i << "]\n";
            threads.push_back(std::thread([i, this]() {
                while (true) {
                    std::function<void()> task;
                    {
                        // {
                        //     std::unique_lock<std::mutex> lock(cout_mtx);
                        //     std::cout << "    Worker[" << i << "]: try to get lock\n";
                        // }
                        std::unique_lock<std::mutex> lock(mtx);
                        while (tasks.size() == 0) {
                            if (terminated) {
                                // {
                                //     std::unique_lock<std::mutex>lock(cout_mtx);
                                //     std::cout << "    Worker[" << i << "]: ready to return\n";
                                // }
                                return;
                            }
                            // {
                            //     std::unique_lock<std::mutex>lock(cout_mtx);
                            //     std::cout << "    Worker[" << i << "]: before wait\n";
                            // }
                            cv.wait(lock);
                            // {
                            //     std::unique_lock<std::mutex>lock(cout_mtx);
                            //     std::cout << "    Worker[" << i << "]: after wait\n";
                            // }
                        }
                        task = tasks.front();
                        tasks.pop();
                    }
                    // {
                    //     std::unique_lock<std::mutex>lock(cout_mtx);
                    //     std::cout << "    Worker[" << i << "]: begin to execute task!\n";
                    // }
                    task();
                }
            }));
        }
    }

    template <class F, class... Args>
    auto submit(F&& f, Args&&... args) -> std::future<typename std::result_of<F(Args...)>::type> {
        using return_type = typename std::result_of<F(Args...)>::type;
        auto task = std::make_shared<std::packaged_task<return_type()>>(
            std::bind(std::forward<F>(f), std::forward<Args>(args)...));
        auto fut = task->get_future();

        {
            std::unique_lock<std::mutex> lock(mtx);
            if (terminated) {
                throw std::runtime_error("Thread pool has been stopped!");
            }
            tasks.push([task]() -> void { (*task)(); });
        }
        cv.notify_one();
        return fut;
    }

    void close() {
        {
            std::cout << "Thread Pool: try to close\n";
            std::unique_lock<std::mutex> lock(mtx);
            terminated = true;
            std::cout << "Thread Pool: set flag\n";
        }
        cv.notify_all();
        // for (auto& t : threads) {
        for (int i = 0; i < threads.size(); i++) {
            auto& t = threads[i];
            std::cout << "Thread Pool: try close thread " << i << " \n";
            t.join();
            std::cout << "Thread Pool: closed\n";
        }
    }

   private:
    void worker() {
        while (true) {
            std::function<void()> task;
            {
                std::unique_lock<std::mutex> lock(mtx);
                while (tasks.size() == 0) {
                    cv.wait(lock);
                    if (terminated)
                        return;
                }
                task = tasks.front();
                tasks.pop();
            }
            task();
        }
    }

    size_t pool_size;
    std::vector<std::thread> threads;
    std::queue<std::function<void()>> tasks;
    std::mutex mtx;
    std::condition_variable cv;
    bool terminated;
};

int foo(int arg) {
    std::this_thread::sleep_for(std::chrono::milliseconds(1000));
    auto tmp = time(0);
    {
        std::unique_lock<std::mutex> lock(cout_mtx);
        std::cout << "    Func: " << arg << " " << ctime(&tmp);
    }
    return arg * arg;
}

int main() {
    ThreadPool tp(32);
    // std::vector<int> args{1, 2, 3, 4};
    std::vector<std::future<int>> ans;
    auto tmp = time(0);
    {
        std::unique_lock<std::mutex> lock(cout_mtx);
        std::cout << "Main: submit start! " << ctime(&tmp);
    }
    for (int i = 0; i < 128; i++) {
        ans.push_back(tp.submit(foo, i));
    }
    tmp = time(0);
    {
        std::unique_lock<std::mutex> lock(cout_mtx);
        std::cout << "Main: submit complete! " << ctime(&tmp);
    }

    tp.close();
    // std::this_thread::sleep_for(std::chrono::seconds(12));
    // return 0;
    tmp = time(0);
    std::cout << "Main: closed!" << ctime(&tmp);
    for (auto& i : ans) {
        std::cout << i.get() << "\n";
    }
    tmp = time(0);
    std::cout << "Main: all Completed!" << ctime(&tmp);
}