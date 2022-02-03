import math
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2


# This class is intended for different inequialitis in Error Correcting Theorem
class Bounds:
    def generalized_hamming_bound(self, n, delta, q):
        inner_sum = 0.0
        d = delta * n
        for i in range(0, math.floor((d-1)/2), 1):
            inner_sum += ncr(n, i) * math.pow(q-1, i)
        k = n - math.log(inner_sum, q)
        rate = k / n
        return rate
