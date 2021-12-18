def solution(L, x):
    if len(L) == 0:
        return -1
    answer = -1
    start = 0
    end = len(L) - 1
    while start <= end:
        middle = (start + end) // 2

        if x == L[middle]:
            answer = middle
            return answer
        # x가 중간보다 낮을 때
        elif x < L[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return answer


import sys

n = int(input())

n_list = list(map(int, sys.stdin.readline().split()))

m = int(input())

m_list = list(map(int, sys.stdin.readline().split()))

n_list.sort()

for i in m_list:
    if solution(n_list, i) >= 0:
        print(1)
    else:
        print(0)
