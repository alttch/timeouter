import time


class TimeoutException(Exception):
    pass


class Timer():

    def __init__(self, timeout):
        self.set_timeout(timeout)
        self.reset()
        self.TimeoutException = TimeoutException

    def has(self, timeout=0):
        return self.get() - timeout > 0

    def check(self, message=None):
        if self.get() <= 0:
            raise self.TimeoutException(
                message) if message is not None else self.TimeoutException

    def get(self):
        return self.start_time + self._timeout - time.time()

    def reset(self):
        self.start_time = time.time()

    def set_timeout(self, timeout):
        self._timeout = float(timeout)

    def set_exception_class(self, e):
        self.TimeoutException = e
