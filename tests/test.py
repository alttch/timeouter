#!/usr/bin/env python3

from pathlib import Path
import sys
import os

sys.path.insert(0, Path().absolute().parent.as_posix())
import timeouter

import unittest
import time

from types import SimpleNamespace

result = SimpleNamespace()

class CustomTimeoutException(Exception): pass


class Test(unittest.TestCase):

    def run(self, result=None):
        if not result.errors:
            super(Test, self).run(result)

    def test001_thread(self):
        timeouter.init(0.1)
        time.sleep(0.05)
        self.assertTrue(timeouter.has(0.01))
        self.assertFalse(timeouter.has(1))
        time.sleep(0.06)
        self.assertFalse(timeouter.has(0.01))
        self.assertRaises(timeouter.TimeoutException, timeouter.check)
        timeouter.set_exception_class(CustomTimeoutException)
        self.assertRaises(CustomTimeoutException, timeouter.check)
        timeouter.reset()
        self.assertTrue(timeouter.has(0.01))
        timeouter.check()

    def test002_object(self):
        t = timeouter.Timer(0.1)
        time.sleep(0.05)
        self.assertTrue(t.has(0.01))
        self.assertFalse(t.has(1))
        time.sleep(0.06)
        self.assertFalse(t.has(0.01))
        self.assertRaises(t.TimeoutException, t.check)
        t.set_exception_class(CustomTimeoutException)
        self.assertRaises(CustomTimeoutException, t.check)
        t.reset()
        self.assertTrue(t.has(0.01))
        t.check()

if __name__ == '__main__':
    import argparse
    test_suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    test_result = unittest.TextTestRunner().run(test_suite)
    sys.exit(not test_result.wasSuccessful())
