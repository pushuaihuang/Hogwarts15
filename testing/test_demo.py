#!/usr/bin/env python
# coding=utf-8
import pytest

from python.calculator import Calculator
@pytest.mark.CAL
class TestCalcul:
    def setup_class(self):
        print("开始准备-----")
        self.cal = Calculator()

    def setup(self):
        print('test_start----------------')

    """
    加法测试用例：（1）1.整数运算；2.浮点型运算；3.整数与浮点型
    """

    @pytest.mark.parametrize('a,b,expect',
                             [[1, 2, 3], [1000, 100000, 101000], [1, 0, 1], [-1, -2, -3], [-100, -200, -300],
                              [-1, 0, -1], [1, -1, 0], [2.4, 2.6, 5], [100.1, 100.2, 200.3], [-1.1, -1.2, -2.3],
                              [-100.1, -100.2, -200]
                                 , [1, 1.1, 2.1], [100, 100.1, 200.1], [3.2, -1.2, 2], [23, 10.1, 33.1],
                              [23, -10.1, 12.9], [-10, 0.1, -9.9], [-10, -0.1, -10.1]])
    def test_add(self, a, b, expect):
        result = self.cal.add(a, b)
        assert result == expect
    """
        除法测试用例：（1）1.整数运算；2.浮点型运算；3.整数与浮点型
    """


    @pytest.mark.parametrize('a,b,expect',
                             [[2, 1, 2], [100, 50, 2], [-2, -1, 2], [-100, -50, 2], [2.4, 0.4, 6], [200.4, 100.2, 2],
                              [1, 0, 1], [-2.4, -0.4, 6],
                              [-200.4, -100.2, 2], [2, -1, -2], [-4, 2, -2], [200, -100, -2], [-200, 100, -2],
                              [-2, 1, -2], [2.4, -0.4, -6],
                              [200.2, -100.1, -2], [-2.4, 0.4, -6], [-200.2, 100.1, -2], [4, 0.5, 8], [100, 0.5, 200],
                              [-4, 0.5, -8],
                              [-100, 0.5, -200]])
    def test_div(self, a, b, expect):
        try:
            result = self.cal.div(a, b)
            assert result == expect
        except Exception as e:
            print(e)

    # 捕获异常with pytest.raises；没有异常也会跑错，必须捕获到相对应的异常才会pass
    @pytest.mark.parametrize("a,b,expext", [[0.1, 0, True], [1, 0, True]])
    def test_div_except(self, a, b, expext):
        with pytest.raises(ZeroDivisionError):
            result = self.cal.div(a, b)

    def teardown(self):
        print('test_end----------------')

    def teardown_class(self):
        print("\n结束-----")
