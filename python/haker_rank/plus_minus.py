import math
import re


def plusMinus(arr):
    length = len(arr)
    p = 0
    n = 0
    zero = 0
    for i in arr:
        if i > 0:
            p += 1
        elif i < 0:
            n += 1
        else:
            zero += 1
    print("{:.6f}".format(p / length))
    print("{:.6f}".format(n / length))
    print("{:.6f}".format(zero / length))
