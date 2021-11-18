def camelcase(s):
    count = 0
    for i in range(len(s)):
        if i==0:
            count += 1
        if s[i].isupper():
            count += 1
    return count
