from math import gcd

# num
# den
class Rational:
    def __eq__(self, other):
        return self.__cmp__(other) == 0
    def __cmp__(self, other):
        if isinstance(other, Rational):
            return compare(self, other)
        elif isinstance(other, list):
            if len(other) != 2:
                raise Exception("Rational __cmp__: other должен иметь размерность 2")
            return compare(self, create(other[0], other[1]))
    def __str__(self):
        return f"{self.num}/{self.den} (float64: {to_float(self)})"

def _check_is_invalid_args(a, b):
    return not (isinstance(a, Rational) and isinstance(b, Rational))

def create(numer, denom):
    r = Rational()
    if numer == 0:
        r.num = 0
        r.den = 0
        return r
    elif not denom or not numer:
        return None
    r.num = abs(numer) * (-1 if numer * denom < 0 else 1)
    r.den = abs(denom)
    _balance(r)
    return r

def compare(a, b):
    if _check_is_invalid_args(a,b):
        return None
    t = sub(a, b).num
    if t > 0:
        return 1
    elif not t:
        return 0
    else:
        return -1

def to_int(r):
    if not isinstance(r, Rational):
        return None
    return r.num//r.den

def to_float(r):
    if not isinstance(r, Rational):
        return None
    return r.num/r.den

def _nod(first, second):
    a, b = abs(first), abs(second)
    while b != 0:
        if a >= b:
            a, b = b, a%b
        else:
            a, b = a, b%a
    return a

def _balance(r):
    if not isinstance(r, Rational):
        return None
    k = _nod(r.num, r.den)
    r.num //= k
    r.den //= k

def add(a, b):
    if _check_is_invalid_args(a,b):
        return None
    return create(a.num * b.den + b.num * a.den, a.den * b.den)

def sub(a, b):
    if _check_is_invalid_args(a,b):
        return None
    return create(a.num * b.den - b.num * a.den, a.den * b.den)

def mul(a, b):
    if _check_is_invalid_args(a,b):
        return None
    return create(a.num * b.num, a.den * b.den)

def div(a, b):
    if _check_is_invalid_args(a,b):
        return None
    return create(a.num * b.den, a.den * b.num)

def power(n, pw):
    if not isinstance(n, Rational):
        return None
    if pw > 0:
        a = create(n.num, n.den)
    else:
        a = create(n.den, n.num)
    r = create(1, 1)
    if pw&1:
        r.num, r.den = a.num, a.den
    pw >>= 1

    while pw > 0:
        a = mul(a, a)
        if pw&1:
            r = mul(a, r)
        pw >>= 1
    return r

def to_str(r):
    if not isinstance(r, Rational):
        return None
    return f"{r.num}/{r.den}"



