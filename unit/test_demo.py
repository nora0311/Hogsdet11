import unittest

class TestDemo(unittest.TestCase):
    #本次执行需要检查是否是用unittest执行的。
    #测试装置，fixture

     # def fun_1(self)-> str:
     #      x = None
     #      return x
     #
     #
     # def fun_2(self):
     #     x = None
     #     return x


    @classmethod
    def setUpClass(cls) -> None:
        print("setupClass")

    def setUp() -> None:
        print("setup")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownClass")

    def tearDown(self) -> None:
        print("teardown")

    def test_sum(self):
        x = 1 + 2
        print("test_sum")
        print(x)
        # 断言 逗号后面要加空格，期望值写在前面，真实的结果值写在第二个参数里。那么这个断言，需要确认下参数格式，几个参数
        # 这个函数，相等
        self.assertEqual(3, x, f'x=(x) expection=3')

    def test_demo(self):
        print("test_demo")
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
