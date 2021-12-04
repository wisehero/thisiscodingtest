a, b = input().split()

a = list(a)
b = list(b)
a[0], a[2] = a[2], a[0]
b[0], b[2] = b[2], b[0]
a = int(''.join(a))
b = int(''.join(b))
print(max(a, b))
