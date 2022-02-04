import operator as op
from functools import reduce
import math
import Bounds
import Config
import numpy as np


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom  # or / in Python 2

# 0<=x<=1
def entropy(q, x):
    ent = 0
    if not(x == 0 or x == 1):
        ent = x * math.log(q-1, q) -\
              x * math.log(x, q) -\
              (1-x) * math.log(1-x, q)
    return ent

def johnson(q, delta):
    john = 0
    if delta <= (q - 1) / q:
        john = (1 - 1 / q) *\
               (1 - math.sqrt(1 - (q * delta) / (q - 1)))
    return john


def calculate_delta_to_rate_plot():
    # delta axis values
    delta_arr = np.arange(1.0 / Config.n, 1, Config.res)
    graph_arr = [None] * len(Bounds.bounds_inst.bound_arr)
    name_arr = [None] * len(Bounds.bounds_inst.bound_arr)
    for i in range(0, len(Bounds.bounds_inst.bound_arr)):
        bound = Bounds.bounds_inst.bound_arr[i]
        name_arr[i] = bound(Bounds.bounds_inst, Config.n, delta_arr[0], Config.q)[1]
        graph_arr[i] = [bound(Bounds.bounds_inst, Config.n, delta, Config.q)[0] for delta in delta_arr]
    return delta_arr, graph_arr, name_arr


def create_bound(bound_type_req, q_req):
    # delta axis values
    delta_arr = np.arange(1.0 / Config.n, 1, Config.res)
    bound = getattr(Bounds.bounds_inst, bound_type_req)
    graph_arr = [bound(Config.n, delta, q_req)[0] for delta in delta_arr]
    name_arr = bound(Config.n, delta_arr[0], q_req)[1]
    return [bound_type_req, q_req, delta_arr, graph_arr, name_arr]
