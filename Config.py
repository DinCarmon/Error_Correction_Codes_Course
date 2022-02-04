import math
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
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

    def gilbert_vershamov_bound(self, n, delta, q):
        Rate = 1 - entropy(q, delta)
        return Rate

    def singleton_bound(self, n, delta, q):
        d = delta * n
        k = n - d + 1
        rate = k / n
        return rate

    def plotkin_bound(self, n, delta, q):
        plotkin_divider = (1 - 1 / q) * n
        d = delta * n
        rate = 0
        if d == plotkin_divider:
            num_of_code_words = 2 * q * n
            # stronger specific bound
            if q == 2:
                num_of_code_words = q * n
            k = math.log(num_of_code_words, q)
            rate = k / n
        else:
            if d > plotkin_divider:
                num_of_code_words = q * n / (q * d - (q-1) * n)
                k = math.log(num_of_code_words, q)
                rate = k / n
            else:
                rate = 1 - (q / (q-1)) * delta
        return rate

    def elias_bassalygo_bound(self, n, delta, q):
        rate = 1 - entropy(q, johnson(q, delta))
        return rate
