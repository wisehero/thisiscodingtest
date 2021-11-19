def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if sum(s[i:i + m]) == d:
            count += 1
    return count


d = 3
m = 2
s = [1, 1, 1, 1, 1, 1]

print(birthday(s, d, m))
