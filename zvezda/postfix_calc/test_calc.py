from postfix_calc import postfix_calc
from math import isnan
import warnings

def test_simply_calc():
    assert postfix_calc("2.0 3 + 1e-1 /") == 50.0
    assert postfix_calc("") is None and postfix_calc(None) is None
    with warnings.catch_warnings(record=True) as w:
        assert isnan(postfix_calc("3 0 / 3 +"))
        assert len(w) == 1
