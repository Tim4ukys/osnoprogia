from collections import deque

class _Node:
    def __init__(self, data, rt):
        self.data = data
        self.root = rt

    root = None
    left = None
    right = None
    data = None

# ~~~~~~~~~~~~~~~~~~~~~~

def _lr(a : _Node):
    a.right, a.left = a.left, a.right
    b = a.left
    b.left, b.right = b.right, b.left
    if b.left:
        b.left.root = a
    if a.right:
        a.right.root = b
    b.left, a.right = a.right, b.left
    a.data, b.data = b.data, a.data

def _rr(a : _Node):
    a.right, a.left = a.left, a.right
    b = a.right
    b.left, b.right = b.right, b.left
    if b.right:
        b.right.root = a
    if a.left:
        a.left.root = b
    a.left, b.right = b.right, a.left
    a.data, b.data = b.data, a.data

# ~~~~~~~~~~~~~~~~~~~~~~

class Tree:
    root : _Node = None
    cmpFunc = None

# ~~~~~~~~~~~~~~~~~~~~~~

def create(cmp_function):
    if not cmp_function:
        return None
    r = Tree()
    r.cmpFunc  = cmp_function
    return r

# ~~~~~~~~~~~~~~~~~~~~~~
def _height(tr : _Node):
    if not tr:
        return 0
    deq = deque()
    deq.append(tr)
    ans = 0
    while len(deq) > 0:
        c = len(deq)
        while c > 0:
            ch = deq.popleft()
            c -= 1
            if ch.left: deq.append(ch.left)
            if ch.right: deq.append(ch.right)
        ans += 1
    return ans


def _fix_balance(tr : _Node):
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

def insert(tr : Tree, data):
    if not tr:
        return None
    if not tr.root:
        tr.root = _Node(data, None)
        return None

    # Ищу куда вставить
    ch = tr.root
    while True:
        cmp = tr.cmpFunc(data, ch.data)
        if cmp == 0:
            sv_data, ch.data = ch.data, data
            return sv_data
        if cmp < 0:
            if not ch.left:
                ch.left = _Node(data, ch)
                break
            else:
                ch = ch.left
        else:
            if not ch.right:
                ch.right = _Node(data, ch)
                break
            else:
                ch = ch.right

    # Балансировка
    while ch:
        _fix_balance(ch)
        ch = ch.root

def _get_del_min(tr : Tree):
    if not tr:
        return None, None

    if not tr.left:
        sv_data = tr.data
        if tr.right:
            tr.data = tr.right.data
            tr.right = None
            return sv_data, tr
        else:
            return sv_data, None

    save_data, tr.left = _get_del_min(tr.left)
    _fix_balance(tr)
    return save_data, tr


def delete(tr : Tree, data):
    if not tr or not tr.root:
        return

    ch = tr.root
    save_data = None
    while True:
        if not ch:
            return None
        cmp = tr.cmpFunc(data, ch.data)
        if cmp == 0:
            save_data = ch.data
            if not ch.right:
                if ch.left:
                    ch.data, ch.left = ch.left.data, None
                elif not ch.root:
                    tr.root = None
                elif tr.cmpFunc(ch.data, ch.root.data) < 0:
                    ch.root.left = None
                else:
                    ch.root.right = None
                ch = ch.root
            else:
                min_ch = ch.right
                if not min_ch.left:
                    if not min_ch.right:
                        ch.data = min_ch.data
                        ch.right = None
                    else:
                        ch.data, min_ch.data = min_ch.data, min_ch.right.data
                        min_ch.right = None
                else:
                    while min_ch.left:
                        min_ch = min_ch.left
                    if min_ch.right:
                        ch.data, min_ch.data = min_ch.data, min_ch.right.data
                        min_ch.right = None
                    else:
                        ch.data = min_ch.data
                        min_ch.root.left = None
                ch = min_ch.root
            break
        elif cmp < 0:
            ch = ch.left
        else:
            ch = ch.right

    while ch:
        _fix_balance(ch)
        ch = ch.root
    return save_data


def foreach(tr : Tree, func, extra_data):
    if not tr.root:
        return
    stack = []
    ch = tr.root
    while len(stack) > 0 or ch:
        while ch:
            stack.append(ch)
            ch = ch.left
        ch = stack.pop()
        func(ch.data, extra_data)
        ch = ch.right

def find(tr : Tree, data):
    if not tr:
        return None
    ch = tr.root
    while ch:
        cmp = tr.cmpFunc(data, ch.data)
        if cmp == 0:
            return ch.data
        elif cmp < 0:
            ch = ch.left
        else:
            ch = ch.right
    return None

def _clc_size(_, x):
    x[0] += 1
def size(tr : Tree):
    a = [0]
    foreach(tr, _clc_size, a)
    return a[0]

def clear(tr : Tree):
    tr.root = None
