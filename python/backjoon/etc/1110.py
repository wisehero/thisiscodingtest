# 숫자 입력받기
s = input()
if len(s) == 1:
    s = "0" + s
# 입력받은 숫자를 x + y = z 형태로 바꾸기
s1 = str(s[0]) + "+" + str(s[1]) + "=" + str(int(s[0]) + int(s[1]))


cnt = 0

while True:
    if len(s1) == 5:
        s2 = s1[2] + s1[4]
        cnt += 1
        if s2 == s:
            print(cnt)
            break
        else:
            s1 = str(s2[0]) + "+" + str(s2[1]) + "=" + str(int(s2[0]) + int(s2[1]))

    if len(s1) == 6:
        s2 = s1[2] + s1[5]
        cnt += 1
        if s2 == s:
            print(cnt)
            break
        else:
            s1 = str(s2[0]) + "+" + str(s2[1]) + "=" + str(int(s2[0]) + int(s2[1]))
