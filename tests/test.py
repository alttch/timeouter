#!/usr/bin/env python3

from pathlib import Path
import sys

sys.path.insert(0, Path().absolute().parent.as_posix())
import timeouter

import unittest
import time

from types import SimpleNamespace


class CustomTimeoutException(Exception):
    pass


class Test(unittest.TestCase):

    def run(self, result=None):
        if not result.errors:
            super(Test, self).run(result)

    def test001_thread(self):
        timeouter.init(0.1)
        self.check_timer(timeouter)

    def test002_object(self):
        self.check_timer(timeouter.Timer(0.1))

    def test099_default_exception(self):
        timeouter.set_default_exception_class(CustomTimeoutException)
        t = timeouter.Timer(0.01)
        time.sleep(0.011)
        self.assertRaises(CustomTimeoutException, t.check)

    def check_timer(self, t):
        time.sleep(0.05)
        self.assertTrue(t.has(0.01))
        self.assertFalse(t.has(1))
        time.sleep(0.06)
        self.assertFalse(t.has(0.01))
        self.assertRaises(TimeoutError, t.check)
        t.set_exception_class(CustomTimeoutException)
        self.assertRaises(CustomTimeoutException, t.check)
        t.reset()
        self.assertTrue(t.has(0.01))
        t.check()
        self.assertLess(t.get(), 0.1)
        self.assertLess(t.get(laps=5), 0.02)


if __name__ == '__main__':
    import argparse
    test_suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    test_result = unittest.TextTestRunner().run(test_suite)
    sys.exit(not test_result.wasSuccessful())
