#!/usr/bin/env pytest

from pathlib import Path
import sys
import pytest

sys.path.insert(0, Path().absolute().parent.as_posix())
import timeouter

import time


class CustomTimeoutException(Exception):
    pass


def test001_thread():
    timeouter.init(0.1)
    _test_timer(timeouter)


def test002_object():
    _test_timer(timeouter.Timer(0.1))


def test099_default_exception():
    timeouter.set_default_exception_class(CustomTimeoutException)
    t = timeouter.Timer(0.01)
    time.sleep(0.011)
    with pytest.raises(CustomTimeoutException):
        t.check()


def _test_timer(t):
    time.sleep(0.05)
    assert t.has(0.01) is True
    assert t.has(1) is False
    time.sleep(0.06)
    assert t.has(0.01) is False
    with pytest.raises(TimeoutError):
        t.check()
    t.set_exception_class(CustomTimeoutException)
    with pytest.raises(CustomTimeoutException):
        t.check()
    t.reset()
    assert t.has(0.01) is True
    t.check()
    assert t.get() < 0.1
    assert t.get(laps=5) < 0.02
