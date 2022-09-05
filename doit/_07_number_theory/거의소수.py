"""
1. 숫자 입력을 받는다.
2. 소수를 구해놓는다.
3. 구해 놓은 소수를 바탕으로 소수의 제곱수를 찾는다.
"""

import math

n, m = map(int, input().split())
A = [0] * 10000001

# 수 채워넣기
for i in range(2, len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A)) + 1)):
    if A[i] == 0:
        continue
    for j in range(i + i, len(A), i):  # 배수 지우기
        A[j] = 0

count = 0

for i in range(2, 10000001):
    if A[i] != 0:
        temp = A[i]
        while A[i] <= m / temp:
            if A[i] >= n / temp:
                count += 1
            temp = temp * A[i]

print(count)
