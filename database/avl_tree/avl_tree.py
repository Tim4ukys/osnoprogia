
class _Node:
    def __init__(self, data):
        self.data = data

    left = None
    right = None
    data = None
    height = 0

# ~~~~~~~~~~~~~~~~~~~~~~
# mb ret new root

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
    _fix_height(tr)

# fix:
# 1. node == None в двух случаях | complete
# 2. вынести fix_balance в отдельную функцию, дабы связать функу с delete | complete
# 3. чекнуть функу, когда нужный элемент tr | complete
# 4. tr ссылка на голову внутри  | complete
# 5. избавиться от hasattr | naxya??
def insert(tr : Tree, data, cmp_func = None):
    if not tr:
        return _Node(data)
    elif not tr.data:
        tr.data = data
        tr.height = 0
        return None

    # <~
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

# переписать
def delete(tr : Tree, data, cmp_func = None):
    if not tr or not tr.data:
        return None
    if not cmp_func:
        cmp_func = tr.cmpFunc

    cmp = cmp_func(data, tr.data)
    if cmp == 0:
        save_data = tr.data
        if tr.right:
            nm = tr.right
            par = None
            while nm.left:
                par, nm = nm, nm.left
            if par:
                par.left = None
            else:
                tr.right = None
            tr.data = nm.data
        else:
            if tr.left:
                tr.data = tr.left.data
                tr.left = None
            else:
                if hasattr(tr, "cmpFunc"):
                    tr.data = None
                    tr.height = -1
                    return save_data
                else:
                    return None, save_data

    nm = delete(tr.left if cmp < 0 else tr.right, data, cmp_func)
    if isinstance(nm, list):
        if cmp < 0:
            tr.left = None
        else:
            tr.right = None
    _fix_balance(tr)
    return nm[1] if isinstance(nm, list) else nm


"""
def delete(tr : Tree, data, cmp_func = None):
    if not tr or not tr.data:
        return None

    # <~
    if not cmp_func:
        cmp_func = tr.cmpFunc
    cmp = cmp_func(data, tr.data)
    if cmp == 0:
        # ~~~~~~~~~~~
        # фиксануть
        r = tr.right
        if r:
            r.left = tr.left
        else:
            r = tr.left
        return (tr.data, r) if not hasattr(tr, "cmpFunc") else tr.data
        # ~~~~~~~~~~~
    r = delete(tr.left if cmp < 0 else tr.right, data, cmp_func)
    if not r:
        return
    save_data, next_point = r
    if cmp < 0:
        tr.left = next_point
    else:
        tr.right = next_point
    _fix_balance(tr)
    return (save_data, tr) if not hasattr(tr, "cmpFunc") else save_data
"""


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
