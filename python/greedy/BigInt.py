"""
 큰 수의 법칙
"""

# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 입력받은 수 정렬
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 가장 작은 수
cnt = 0
max_cnt = 0
sum = 0

while cnt < m:
    if max_cnt == k:
        sum += second
        max_cnt = 0
        cnt += 1
        continue
    sum += first
    max_cnt += 1
    cnt += 1

print(sum)
