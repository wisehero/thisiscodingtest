while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    a = set()
    b = set()

    for _ in range(n):
        a.add(int(input()))

    for _ in range(m):
        b.add(int(input()))

    print(len(a.intersection(b)))
