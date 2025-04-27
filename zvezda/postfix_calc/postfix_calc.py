import database.Spisok.SList as SList
import warnings

def _pop_two(sl : SList):
    a = sl.val
    b = sl.next.val
    return a, b, sl.next.next

def _isfloat(s : str):
    try:
        float(s)
    except ValueError:
        return False
    return True

def postfix_calc(expression):
    if not isinstance(expression, str):
        return None
    sp : SList = None
    size = 0
    for i in expression.split():
        if _isfloat(i):
            size += 1
            sp = SList.prepend(sp, float(i))
            continue
        elif i not in "+-/*":
            warnings.warn(f"Unknown symbol: {i}", RuntimeWarning)
            continue
        elif size < 2:
            warnings.warn(f"stack size is too small. Last: {SList.get_last(sp)}", RuntimeWarning)
            continue
        size -= 1
        b, a, sp = _pop_two(sp)
        if i == "+":
            sp = SList.prepend(sp, a+b)
        elif i == '-':
            sp = SList.prepend(sp, a-b)
        elif i == "*":
            sp = SList.prepend(sp, a*b)
        elif b == 0.0:
            warnings.warn(f"division by zero: {a}/{b}", RuntimeWarning)
            sp = SList.prepend(sp, float('nan'))
        else:
            sp = SList.prepend(sp, a/b)

    return SList.get_last(sp)


