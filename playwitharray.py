import math
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 1, 3, 4, 4, 9, 1, 2, 2, 3]
def sum_arr(a):
    return sum(a)
def product(a):
    return math.prod(a)
def str_concat(a):
    s = ""
    for i in a:
        s += str(i)
    return s
def unique_elem(a):
    return list(set(a))
