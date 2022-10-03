# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

n = input(int())
m = 2

while n != 1:
    if n % m == 0:
        print(m)
        n = n // m
    else:
        m += 1
