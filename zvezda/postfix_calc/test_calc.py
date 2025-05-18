from postfix_calc import postfix_calc
from math import isnan

def _try_calc(arg, exc):
    try:
        postfix_calc(arg)
        assert False
    except exc:
        pass


def test_simply_calc():
    assert postfix_calc("2.0 3 + 1e-1 /") == 50.0
    assert postfix_calc("15 3 %") == 0
    assert postfix_calc("") is None and postfix_calc(None) is None
    assert postfix_calc("2.0 3 + 0 *") == 0
    assert postfix_calc("3 5 2 * + 10 4 - 6 / + 7 2 * 1 + - 4 2 ^ + 2 %") == 1
    assert isnan(postfix_calc("3 2 nan / *"))

def test_mnogo_chisel():
    _try_calc("3 2 4 /", RuntimeError)

def test_malo_chisel():
    _try_calc("3 2 4 / + -", BufferError)

def test_zero():
    _try_calc("3 2 0 * /", ZeroDivisionError)

def test_UnkValue():
    _try_calc("2 0 - petya", ValueError)
