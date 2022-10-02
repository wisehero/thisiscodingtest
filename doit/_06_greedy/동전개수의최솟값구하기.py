"""
BOJ 11047번

그리디 알고리즘은 우선순위 큐(파이썬에서는 heapq)를
주로 사용한다. 
"""

N, K = map(int, input().split())
A = [0] * N

for i in range(N):
    A[i] = int(input())

count = 0

for i in range(N - 1, -1, ):
    if A[i] <= K:
        count += int(K / A[i])
        K = K % A[i]

print(count)


