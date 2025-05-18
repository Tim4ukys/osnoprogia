import database.Spisok.SList as SList

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
    stack : SList = None
    size = 0
    for i in expression.split():
        oper = {
            "-": lambda a, b: a-b,
            "+": lambda a, b: a+b,
            "*": lambda a, b: a*b,
            "/": lambda a, b: a/b,
            '^': lambda a, b: a**b,
            "%": lambda a, b: a%b
        }

        if _isfloat(i):
            size += 1
            stack = SList.prepend(stack, float(i))
            continue
        elif i not in oper.keys():
            raise ValueError(f"Unknown symbol: {i}")
        elif size < 2:
            raise BufferError(f"stack size is too small. Last: {SList.get_last(stack)}")
        size -= 1
        b, a, stack = _pop_two(stack)
        stack = SList.prepend(stack, oper[i](a, b))
    if size > 1:
        raise RuntimeError("stack still has numbers")
    return SList.get_last(stack)


