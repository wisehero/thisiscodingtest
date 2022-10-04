t = int(input())
cnt = 0

word_list = []
for _ in range(t):
    word_list.append(input())

for s in word_list:
    for j in range(len(s)):
        if s.count(s[j]) > 1:
            if abs(s.find(s[j]) - s.rfind(s[j])) > 1:
                if len(s[s.find(s[j]): s.rfind(s[j]) + 1]) == s.count(s[j]):
                    if j == len(s) - 1:
                        cnt += 1
                    continue

                else:
                    break
        if j == len(s) - 1:
            cnt += 1

print(cnt)
