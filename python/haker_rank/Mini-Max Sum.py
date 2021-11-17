import math
import os
import random
import re
import sys
from itertools import combinations


def miniMaxSum(arr):
    a = []
    for i in combinations(arr, 4):
        a.append(sum(i))
    print(min(a), max(a))


miniMaxSum([1, 2, 3, 4, 5])
