'''
1. n에서 1을 뺀다.
2. n을 k로 나눈다.(n이 k로 나누어질 때만 선택가능)

두 방법을 선택함과 동시에 최소 횟수로 1이 나오게하는 프로그램을 작성
'''

n, k = map(int, input().split())
count = 0

while n != 1:
    if n % k == 0:
        n = n // k
        count += 1
    else:
        n = n - 1
        count += 1
print(count)
