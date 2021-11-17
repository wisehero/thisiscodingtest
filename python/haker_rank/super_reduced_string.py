# aab 의 경우 aa가 인접해있기 때문에 두 개를 다 날린다
# aaabccddd


s = str(input())
i = 0
while i < len(s) - 1:
    if s[i] == s[i + 1]:
        s = s[:i] + s[i + 2:]
        i = 0
    else:
        i += 1
print(s if s else 'Empty String')
