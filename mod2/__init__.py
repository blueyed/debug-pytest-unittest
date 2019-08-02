from mod1 import FirstTestCase


class SecondTestCase(FirstTestCase):
    def test_2nd(self):
        print("test_2nd", self)
