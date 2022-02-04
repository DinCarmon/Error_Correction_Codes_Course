import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom  # or / in Python 2

# 0<=x<=1
def entropy(q, x):
    ent = x * math.log(q-1, q) -\
          x * math.log(x, q) -\
          (1-x) * math.log(1-x, q)
    return ent

def johnson(q, delta):
    john = (1 - 1 /q) *\
           (1 - math.sqrt(1 - (q * delta) / (q - 1)))
    return john