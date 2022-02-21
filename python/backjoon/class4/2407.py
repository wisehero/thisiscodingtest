a, b = map(int, input().split())


def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


num_1 = fact(a)
num_2 = fact(b)
num_3 = fact(a - b)

ans = int(num_1 // (num_2 * num_3))
print(ans)
