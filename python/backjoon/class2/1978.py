def is_prime_numberV2(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


n = int(input())

n_list = list(map(int, input().split()))
count = 0

for m in n_list:
    if m == 1:
        continue
    if is_prime_numberV2(m):
        count += 1

print(count)
