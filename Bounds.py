import math
import Compute


# This class is intended for different inequialitis in Error Correcting Theorem
class Bounds:
    def generalized_hamming_bound(self, n, delta, q):
        inner_sum = 0.0
        d = delta * n
        for i in range(0, math.floor((d-1)/2) + 1, 1):
            inner_sum += Compute.ncr(n, i) * math.pow(q-1, i)
        k = n - math.log(inner_sum, q)
        rate = k / n
        return rate
    bound_arr = [generalized_hamming_bound]


global bounds_inst
bounds_inst = Bounds()