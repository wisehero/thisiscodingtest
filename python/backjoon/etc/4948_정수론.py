def prime(x):
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


li = list(range(2, 246912))
memo = []

for i in li:
    if prime(i):
        memo.append(i)

n = int(input())

while True:
    count = 0
    if n == 0:
        break
    for i in memo:
        if n < i <= 2 * n:
            count += 1
    print(count)
    n = int(input())
