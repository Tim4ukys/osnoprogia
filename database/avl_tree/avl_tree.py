
class _Node:
    def __init__(self, data):
        self.data = data

    left = None
    right = None
    data = None
    height = 0

# ~~~~~~~~~~~~~~~~~~~~~~

def _height(a : _Node):
    return a.height if a else -1

def _fix_height(a : _Node):
    a.height = max(_height(a.right), _height(a.left)) + 1

def _lr(a : _Node):
    a.right, a.left = a.left, a.right
    b = a.left
    b.left, b.right = b.right, b.left
    b.left, a.right = a.right, b.left
    a.data, b.data = b.data, a.data
    _fix_height(b)
    _fix_height(a)

def _rr(a : _Node):
    a.right, a.left = a.left, a.right
    b = a.right
    b.left, b.right = b.right, b.left
    a.left, b.right = b.right, a.left
    a.data, b.data = b.data, a.data
    _fix_height(b)
    _fix_height(a)


# ~~~~~~~~~~~~~~~~~~~~~~

class Tree(_Node):
    def __init__(self):
        self.height = -1
        pass

    cmpFunc = None

# ~~~~~~~~~~~~~~~~~~~~~~

def create(cmp_function) -> Tree:
    if not cmp_function:
        return None
    r = Tree()
    r.cmpFunc  = cmp_function
    return r

# ~~~~~~~~~~~~~~~~~~~~~~
def _fix_balance(tr : Tree):
    r_height, l_height = _height(tr.right), _height(tr.left)
    balance = r_height - l_height
    if balance > 1: # lr
        b = tr.right
        if _height(b.left) > _height(b.right):
            _rr(tr.right)
        _lr(tr)
    elif balance < -1: # rr
        b = tr.left
        if _height(b.right) > _height(b.left):
            _lr(tr.left)
        _rr(tr)
    else:
        _fix_height(tr)

def insert(tr : Tree, data, cmp_func = None):
    if not tr:
        return _Node(data)
    elif not tr.data:
        tr.data = data
        tr.height = 0
        return None

    if not cmp_func:
        cmp_func = tr.cmpFunc
    cmp = cmp_func(data, tr.data)
    if cmp == 0:
        data, tr.data = tr.data, data
        return data
    r = insert(tr.left if cmp < 0 else tr.right, data, cmp_func)
    if not isinstance(r, _Node):
        return r
    elif cmp < 0:
        tr.left = r
    else:
        tr.right = r
    _fix_balance(tr)
    return tr if not hasattr(tr, "cmpFunc") else None

def _get_del_min(tr : Tree):
    if not tr:
        return None, None

    if not tr.left:
        sv_data = tr.data
        if tr.right:
            tr.data = tr.right.data
            tr.right = None
            tr.height -= 1
            return sv_data, tr
        else:
            return sv_data, None

    save_data, tr.left = _get_del_min(tr.left)
    _fix_balance(tr)
    return save_data, tr


def delete(tr : Tree, data, cmp_func = None):
    if not tr or not tr.data:
        return None
    if not cmp_func:
        cmp_func = tr.cmpFunc

    cmp = cmp_func(data, tr.data)
    if cmp == 0:
        save_data = tr.data
        tr.data, tr.right = _get_del_min(tr.right)
        _fix_height(tr)
        if tr.height == 0 and hasattr(tr, "cmpFunc"):
            tr.height = -1
        return save_data

    nm = delete(tr.left if cmp < 0 else tr.right, data, cmp_func)
    if cmp < 0 and tr.left and not tr.left.data:
        tr.left = None
    elif tr.right and not tr.right.data:
        tr.right = None
    _fix_balance(tr)
    return nm

def foreach(tr : Tree, func, extra_data):
    if not tr or tr.height == -1:
        return
    foreach(tr.left, func, extra_data)
    func(tr.data, extra_data)
    foreach(tr.right, func, extra_data)

def find(tr : Tree, data):
    if not tr or tr.height == -1:
        return
    c = tr.cmpFunc(tr.data, data)
    if c < 0:
        return find(tr.left, data)
    elif c > 0:
        return find(tr.right, data)
    else:
        return tr.data

def _clc_size(_, x):
    x[0] += 1
def size(tr : Tree):
    a = [0]
    foreach(tr, _clc_size, a)
    return a[0]

def clear(tr : Tree):
    tr.data = None
    tr.right = None
    tr.left = None
