import time

TimeoutException = TimeoutError


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

    def get(self, laps=1):
        return (self._start_time + self._timeout - time.perf_counter()) / laps

    def reset(self):
        self._start_time = time.perf_counter()

    def set_timeout(self, timeout):
        self._timeout = float(timeout)

    def set_exception_class(self, e):
        self.TimeoutException = e
