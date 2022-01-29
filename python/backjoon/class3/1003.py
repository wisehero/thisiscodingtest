count = [0, 0]


def fibo(n):
    zero = 0
    one = 0
    if n == 0:
        count[0] += 1
        return count
    if n == 1:
        count[1] += 1
        return count
    else:
        fibo(n - 1) + fibo(n - 2)
    return count


table = []

for i in range(41):
    count = [0, 0]
    x, y = fibo(i)
    table.append((x, y))

print(table[3])