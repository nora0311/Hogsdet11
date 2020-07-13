def div(a, b):
    return a / b


def test_div():
    assert div(10, 2) == 5
    assert div(0, 10) == 0
    # assert div(5, 0) == None
