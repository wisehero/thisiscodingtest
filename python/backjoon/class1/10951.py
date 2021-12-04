# 10951
# 두 정수 A와 B를 입력받은 다음, A + B를 출력하는 프로그램을 작성하시오.

while True:
    try:
        a, b = map(int, input().split())
        if a < 0 or b > 10:
            break
        print(a + b)
    except:
        exit()
