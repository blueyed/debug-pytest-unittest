from unittest import TestCase

from mixin import MyMixin


class FirstTestCase(MyMixin, TestCase):
    def test_1st(self):
        print("test_1st", self)
