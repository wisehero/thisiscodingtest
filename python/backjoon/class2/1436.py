n = int(input())
cnt = 0
six_n = 666
while True:
    # 666을 포함하면 cnt를 1 증가 시킨다.
    if '666' in str(six_n):
        cnt += 1
    # cnt가 입력과 같다면 six_n을 출력
    if cnt == n:
        print(six_n)
        break
    # cnt가 같지 않다면 six_n을 증가. 다음 1666부터 출력하게됨
    six_n += 1
