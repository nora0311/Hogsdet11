from unit.test_demo import TestDemo
import pytest


def inc(x):
    return x + 1


def test_answer():
    return inc(3) == 5


# module的作用
def setup_module():
    print("setup module")


def setup_function():
    print("setup_function")


# 多个测试用例写到一个类里
class TestClass:
    def setup(self):
        print("setup")

    # 定义类级别的方法要加classmethod,也叫装饰器
    @classmethod
    def setup_class(self):
        print("setup class")

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "hello")

    def test_x(self):
        demo = TestDemo()
        demo.fun_1()

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            1 / 0
