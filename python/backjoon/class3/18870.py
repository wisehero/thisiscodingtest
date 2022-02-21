# 시간초과
# import sys
#
# n = int(sys.stdin.readline())
# locations = list(map(int, sys.stdin.readline().split()))
#
# set_locations = set(locations)
#
# result = []
# for i in locations:
#     m = 0
#     for j in set_locations:
#         if i > j:
#             m += 1
#     result.append(m)
#
# for i in result:
#     print(i, end=' ')

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))  # 2 4 -10 4 -9
arr2 = sorted(list(set(arr)))  # 2 4 -10 -9

dictionary = {arr2[i]: i for i in range(len(arr2))}
for i in arr:
    print(dictionary[i], end=' ')
