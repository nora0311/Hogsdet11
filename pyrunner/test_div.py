import pytest

from pyrunner.div import div


@pytest.mark.happy
def test_div_int():
    assert div(10, 2) == 5
    assert div(10, 5) == 2
    assert div(1000000, 1) == 1000000


@pytest.mark.happy
@pytest.mark.parametrize("number1, number2, expection", {(10, 2, 5), (10, 5, 2), (1000000, 1, 1000000), (100, 200, 0.5)})
def test_div_int_param(number1, number2, expection):
    assert div(number1, number2) == expection


@pytest.mark.happy
def test_div_float():
    assert div(10, 3) == 3.333333
    assert div(10.2, 0.3) == 34.0


@pytest.mark.exception
def test_div_expection():
    assert div(10, 'a')
    assert div('abc', 10)


def test_div_zero():
    # assert div(10, 0) == None
    assert div(0, 10) == 0
# 需不需要写这个用例，是由于商业需求来决定。其实也就是按照需求写用例。
