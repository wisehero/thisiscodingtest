a, b, c = map(int, input().split())

if a > 100 or b > 100 or c > 100:
    exit()
left = b - a
right = c - b

print(max(left - 1, right - 1))
