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
            sleep(0.5)

class ThreadPool:
    def __init__(self, size: int) -> None:
        self.size = size
        self._tasks = []
        self._running_count = 0
        self._lock = Lock()
        self._cond = Condition(self._lock)
        self._thread = Thread(target=self._handler)
        self._thread.start()
        
    def _worker(self, func, args, kwargs, result: Result):
        val = func(*args, **kwargs)
        with result.lock:
            result.value = val
            result.ready = True
        with self._lock:
            self._running_count -= 1
            self._cond.notify_all()
        
    def _handler(self):
        while True:
            with self._lock:
                while  self._running_count >= self.size or len(self._tasks) == 0:
                    self._cond.wait()
                task = self._tasks.pop(0)
                if task is None:
                    return
                self._running_count += 1
                Thread(target=self._worker, args=task).start()
        
    def submit(self, func, *args, **kwargs):
        with self._lock:
            result = Result()
            self._tasks.append((func, args, kwargs, result))
            self._cond.notify_all()
                
    def exit(self):
        with self._lock:
            self._cond.wait_for(lambda: len(self._tasks) == 0)
            self._tasks.append(None)
        self._thread.join()
    

if __name__ == "__main__":
    tp = ThreadPool(2)
    def foo(a=None):
        print(a, f' {time.ctime()}')
        time.sleep(1)
    for _ in range(5):
        tp.submit(foo)
    
    for i in range(5):
        tp.submit(foo, i)
    tp.exit()