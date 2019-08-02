from mixin import MyMixin


class FirstTestCase(MyMixin):
    def test_1st(self):
        print("test_1st", self)
