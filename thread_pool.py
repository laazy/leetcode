from threading import Thread, Lock, Condition
import time


class Result:
    def __init__(self) -> None:
        self.lock = Lock()
        self.value = None
        self.ready = False

    def get(self):
        while True:
            with self.lock:
                if self.ready:
                    return self.value
            time.sleep(0.5)

class ThreadPool:
    def __init__(self, size: int) -> None:
        self.size = size
        self._tasks = []
        self._threads = [Thread(target=self._worker) for _ in range(size)]
        self._cond = Condition(Lock())
        self._running = True
        
        for i in self._threads:
            i.start()

    def _worker(self):
        while True:
            with self._cond:
                while len(self._tasks) == 0:
                    if not self._running:
                        return
                    self._cond.wait()
                func, args, kwargs, result = self._tasks.pop(0)
            val = func(*args, **kwargs)
            with result.lock:
                result.value = val
                result.ready = True

    def submit(self, func, *args, **kwargs) -> Result:
        with self._cond:
            result = Result()
            self._tasks.append((func, args, kwargs, result))
            self._cond.notify()
            return result

    def exit(self):
        with self._cond:
            self._running = False
            self._cond.notify_all()
        for i in self._threads:
            i.join()


if __name__ == "__main__":
    tp = ThreadPool(2)

    def foo(a=None):
        print(a, f' {time.ctime()}')
        time.sleep(1)
        return a
    ans = []
    for _ in range(5):
        ans.append(tp.submit(foo))
    for i in range(5):
        ans.append(tp.submit(foo, i))
    tp.exit()
    for i in ans:
        print(i.get())
