# 2920번

b = [1, 2, 3, 4, 5, 6, 7, 8]
br = sorted(b, reverse=True)
a = list(map(int, input().split()))

if a == b:
    print("ascending")
elif a == br:
    print("descending")
else:
    print("mixed")