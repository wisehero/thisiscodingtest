"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""

N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

for i in range(N - 1):
    for j in range(N - 1 - i):
        if A[j] > A[j + 1]:
            temp = A[j]
            A[j] = A[j + 1]
            A[j + 1] = temp

for i in range(N):
    print(A[i])
