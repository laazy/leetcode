#include <chrono>
#include <condition_variable>
#include <cstdlib>
#include <functional>
#include <future>
#include <iostream>
#include <mutex>
#include <queue>
#include <thread>
#include <vector>

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
        terminated = false;
        pool_size = std::min(static_cast<size_t>(std::thread::hardware_concurrency()), size);
        threads.reserve(pool_size);
        for (size_t i = 0; i < pool_size; i++) {
            threads.push_back(std::thread([i, this]() {
                while (true) {
                    std::function<void()> task;
                    {
                        std::unique_lock<std::mutex> lock(mtx);
                        while (tasks.size() == 0) {
                            if (terminated) {
                                return;
                            }
                            cv.wait(lock);
                        }
                        task = tasks.front();
                        tasks.pop();
                    }
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
                throw std::runtime_error("Thread pool has been terminated!");
            }
            tasks.push([task]() -> void { (*task)(); });
        }
        cv.notify_one();
        return fut;
    }

    void close() {
        {
            std::unique_lock<std::mutex> lock(mtx);
            terminated = true;
        }
        cv.notify_all();
        for (auto& t : threads) {
            t.join();
        }
    }

   private:
    size_t pool_size;
    std::vector<std::thread> threads;
    std::queue<std::function<void()>> tasks;
    std::mutex mtx;
    std::condition_variable cv;
    bool terminated;
};

int foo(int arg) {
    std::this_thread::sleep_for(std::chrono::milliseconds(500 + std::rand() % 1000));
    return arg * arg;
}

int g(int a, int b) {
    std::this_thread::sleep_for(std::chrono::milliseconds(500 + std::rand() % 1000));
    return a * b;
}

int main() {
    ThreadPool tp(32);
    std::vector<std::future<int>> ans;
    for (int i = 0; i < 128; i++) {
        ans.push_back(tp.submit(foo, i));
    }
    for (int i = 0; i < 128; i++) {
        ans.push_back(tp.submit(g, i, 128 - i));
    }

    tp.close();
    for (auto& i : ans) {
        std::cout << i.get() << "\n";
    }
}