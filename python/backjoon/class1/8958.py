t = int(input())

for i in range(t):
    s = input()
    p = 0
    sum = 0
    for k in range(len(s)):
        if s[k] == 'O':
            p += 1
            sum += p
        else:
            p = 0
    print(sum)
