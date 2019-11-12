__version__ = '0.0.1'

import threading
import timeouter.core

g = threading.local()


class TimeoutException(Exception):
    pass


def init(timeout):
    g._to = timeouter.core.Timeouter(timeout)


def check(message=None):
    return g._to.check(message)


def get():
    return g._to.get()


def has(timeout):
    return g._to.has(timeout)


def reset():
    return g._to.reset()


def set_timeout(timeout):
    return g._to.set_timeout(timeout)


def set_exception_class(e):
    g._to.set_exception_class(e)


def set_default_exception_class(e):
    timeouter.core.TimeoutException = e


set_default_exception_class(TimeoutException)
Timeouter = timeouter.core.Timeouter