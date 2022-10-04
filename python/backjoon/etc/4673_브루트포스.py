# d(n) =  n + n[0] + n[1]
table = [x for x in range(10001)]


# 양의 정수 n을 넣었을 때 만들어지는 숫자를 리턴
def solution(n):
    n_str = list(map(int, str(n)))
    number = 0
    if len(n_str) == 1:
        n_str.insert(0, 0)
    if n < 100:
        number = n + n_str[0] + n_str[1]
        return int(number)
    if n < 1000:
        number = n + n_str[0] + n_str[1] + n_str[2]
        return int(number)
    if n < 10000:
        number = n + n_str[0] + n_str[1] + n_str[2] + n_str[3]
        return int(number)
    return n


for i in range(1, 10001):
    m = solution(i)
    if m > 10000:
        continue
    else:
        table[m] = 0

for x in table:
    if x != 0:
        print(x)
